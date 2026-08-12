# -*- coding: utf-8 -*-
"""多章题库生成共享框架。

用法：每章一个数据脚本，import 本框架并调用 gen_chapter()。
关键机制：expected_output 与 test_cases 由脚本模拟运行 solution 自动生成，
并对每章 120 道做 expected_output 去重与断言自校验。
"""
import io
import json
import os
import re
import sys

KW = re.compile(r"^[A-Za-z_]\w*=")


def _is_literal(s):
    s = s.strip()
    if not s:
        return True
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return True
    if s in ("True", "False", "None"):
        return True
    try:
        float(s)
        return True
    except ValueError:
        return False


def _split_top_level(s, sep=","):
    """按顶层逗号分割（忽略引号与括号内的逗号）。"""
    parts = []
    depth = 0
    cur = ""
    quote = None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            cur += ch
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return parts


def auto_template(solution):
    """solution 缺占位符时，自动挖空最后一个 print 的第一个非字面量位置参数。"""
    lines = solution.split("\n")
    idx = None
    for li, line in enumerate(lines):
        p = line.rfind("print(")
        if p >= 0:
            idx = (li, p)
    if idx is None:
        return solution
    li, p = idx
    line = lines[li]
    # p 指向 'print(' 的 'p'，其 '(' 在 p+5；从 p+6 开始匹配到对应 ')'（跳过引号内容）
    depth = 1
    start = p + 6
    end = None
    quote = None
    for i in range(start, len(line)):
        ch = line[i]
        if quote:
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                end = i
                break
    if end is None:
        return solution
    arg_zone = line[start:end]
    parts = [pt for pt in _split_top_level(arg_zone) if not KW.match(pt.strip())]
    if not parts:
        return solution  # 无位置参数（如空行 print()）
    target = None
    for pt in parts:
        if not _is_literal(pt):
            target = pt
            break
    if target is None:
        target = parts[0]
    new_zone = arg_zone.replace(target, "___", 1)
    lines[li] = line[:start] + new_zone + line[end:]
    return "\n".join(lines)


def run(code, max_ops=2000000):
    """执行代码，返回捕获的 stdout。带指令数上限防止死循环挂起。"""
    state = {"count": 0}

    def tracer(frame, event, arg):
        if event == "line":
            state["count"] += 1
            if state["count"] > max_ops:
                raise RuntimeError("代码执行步数超限（疑似死循环）")
        return tracer

    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        sys.settrace(tracer)
        exec(code, {})
    finally:
        sys.settrace(None)
        sys.stdout = old
    return buf.getvalue()


def make_q(topic, suffix, num, desc, template, hints, solution):
    if "___" not in template:
        template = auto_template(solution)
    captured = run(solution)
    tests = ["assert captured_output == " + repr(captured)]
    exec(tests[0], {"captured_output": captured})  # 断言自校验
    return {
        "id": "%s-%03d" % (suffix, num),
        "topic": topic,
        "difficulty": "",
        "stars": "",
        "description": desc,
        "code_template": template,
        "expected_output": captured,
        "hints": hints,
        "test_cases": tests,
        "solution": solution,
    }


def gen_chapter(root, chapter_id, chapter_title, out_dir_name, diff_spec,
                topic_spec, batches, total=120):
    """生成一章 4 档题库。

    参数：
      root       项目根目录
      chapter_id 章节 id（如 "CH02"）
      chapter_title 章节标题（如 "变量和类型"）
      out_dir_name 输出目录名（如 "CH02_Variables_Types"）
      diff_spec  {后缀: (difficulty, stars)}，如 {"E": ("超简单", "⭐"), ...}
      topic_spec {后缀: topic}，如 {"E": "变量和类型", ...}
      batches   {文件名: (后缀, [(num, desc, tpl, hint, sol), ...])}
    """
    out_dir = os.path.join(root, "questions", out_dir_name)
    os.makedirs(out_dir, exist_ok=True)

    all_outs = []
    for fname, (suffix, data) in batches.items():
        topic = topic_spec[suffix]
        difficulty, stars = diff_spec[suffix]
        questions = []
        for num, desc, tpl, hint, sol in data:
            q = make_q(topic, suffix, num, desc, tpl, hint, sol)
            q["id"] = "%s-%s-%03d" % (chapter_id, suffix, num)
            q["difficulty"] = difficulty
            q["stars"] = stars
            questions.append(q)
        assert len(questions) == 30, "%s 必须 30 道，实际 %d" % (fname, len(questions))
        ids = [q["id"] for q in questions]
        assert ids == ["%s-%s-%03d" % (chapter_id, suffix, i) for i in range(1, 31)], ids
        for q in questions:
            run(q["solution"])  # 再跑一次确认可执行
            exec(q["test_cases"][0], {"captured_output": q["expected_output"]})
        all_outs.extend(q["expected_output"] for q in questions)

        payload = {"chapter": chapter_id, "title": chapter_title,
                   "difficulty": difficulty, "questions": questions}
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("已生成 %s（%d 道）" % (path, len(questions)))

    assert len(all_outs) == total
    assert len(set(all_outs)) == total, "%s 的 %d 道 expected_output 存在重复" % (chapter_id, total)
    print("OK: %s 四档 120 道全部生成，expected_output 唯一，断言自校验通过" % chapter_id)
