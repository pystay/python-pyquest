# -*- coding: utf-8 -*-
"""全库校验：遍历 questions/ 下所有章节，校验每章题库。

校验项（每章）：
  1. easy/medium/hard/expert 四个 JSON 文件齐全（各 ≥1 道）
  2. id 连续唯一（CHxx-E/M/H/X-001..N）
  3. 字段完整、difficulty/stars 与档位一致
  4. solution 模拟运行输出 == expected_output
  5. test_cases 断言全部通过（captured_output 机制）
  6. 每章所有题 expected_output 全部唯一
"""
import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, "questions")

EXPECT = {
    "easy_30.json": ("E", "超简单", "⭐"),
    "medium_30.json": ("M", "简单", "⭐⭐"),
    "hard_30.json": ("H", "中等", "⭐⭐⭐"),
    "expert_30.json": ("X", "较难", "⭐⭐⭐⭐"),
}
REQUIRED = {"id", "topic", "difficulty", "stars", "description",
            "code_template", "expected_output", "hints", "test_cases", "solution"}


def run(code):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        exec(code, {})
    finally:
        sys.stdout = old
    return buf.getvalue()


def main():
    chapters = sorted(glob.glob(os.path.join(QDIR, "*")))
    chapters = [c for c in chapters if os.path.isdir(c)]
    assert chapters, "questions/ 下没有章节目录"
    total = 0
    for ch_dir in chapters:
        ch_name = os.path.basename(ch_dir)
        all_outs = []
        for fname, (suffix, diff, stars) in EXPECT.items():
            path = os.path.join(ch_dir, fname)
            assert os.path.exists(path), "缺少文件: %s" % path
            data = json.load(open(path, encoding="utf-8"))
            qs = data["questions"]
            assert len(qs) > 0, "%s 为空" % path
            for i, q in enumerate(qs, 1):
                assert set(q) == REQUIRED, "%s 字段不完整" % q.get("id")
                assert q["id"].endswith("-%s-%03d" % (suffix, i)), q["id"]
                assert q["difficulty"] == diff, q["id"]
                assert q["stars"] == stars, q["id"]
                assert "___" in q["code_template"], q["id"] + " 模板缺少占位符"
                assert q["test_cases"], q["id"] + " 缺少 test_cases"
                captured = run(q["solution"])
                assert captured == q["expected_output"], (
                    "%s solution 输出 %r != expected_output %r"
                    % (q["id"], captured, q["expected_output"]))
                for case in q["test_cases"]:
                    exec(case, {"captured_output": captured})
                all_outs.append(q["expected_output"])
        assert len(set(all_outs)) == len(all_outs), "%s 的 expected_output 存在重复" % ch_name
        total += len(all_outs)
        print("OK: %s %d 道通过" % (ch_name, len(all_outs)))
    print("全库校验通过：%d 章，%d 道题" % (len(chapters), total))


if __name__ == "__main__":
    main()
