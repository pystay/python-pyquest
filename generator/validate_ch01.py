# -*- coding: utf-8 -*-
"""CH01 全量校验：四档 120 道题。

校验项：
  1. 四个 JSON 文件齐全，各 30 道
  2. id 连续唯一（CH01-E/S/M/H-001..030）
  3. 字段完整、topic/difficulty/stars 与难度档一致
  4. 每道题 solution 模拟运行输出 == expected_output
  5. test_cases 断言全部通过（captured_output 机制）
  6. 120 道题 expected_output 全部唯一
"""
import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "questions", "CH01_Hello_World")

EXPECT = {
    "easy_30.json": ("E", "超简单", "⭐", "print() 函数的基本使用"),
    "medium_30.json": ("M", "简单", "⭐⭐", "print() 函数与变量的结合使用"),
    "hard_30.json": ("H", "中等", "⭐⭐⭐", "print() 函数的基本使用"),
    "expert_30.json": ("X", "较难", "⭐⭐⭐⭐", "print() 函数的基本使用"),
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
    all_outs = []
    for fname, (suffix, diff, stars, topic) in EXPECT.items():
        path = os.path.join(DIR, fname)
        assert os.path.exists(path), "缺少文件: %s" % fname
        data = json.load(open(path, encoding="utf-8"))
        qs = data["questions"]
        assert len(qs) == 30, "%s 应有 30 道，实际 %d" % (fname, len(qs))
        for i, q in enumerate(qs, 1):
            assert set(q) == REQUIRED, "%s 字段不完整" % q.get("id")
            assert q["id"] == "CH01-%s-%03d" % (suffix, i), q["id"]
            assert q["topic"] == topic, q["id"]
            assert q["difficulty"] == diff, q["id"]
            assert q["stars"] == stars, q["id"]
            assert "___" in q["code_template"], q["id"] + " 模板缺少 ___ 占位符"
            assert q["test_cases"], q["id"] + " 缺少 test_cases"
            captured = run(q["solution"])
            assert captured == q["expected_output"], (
                "%s solution 输出 %r != expected_output %r"
                % (q["id"], captured, q["expected_output"]))
            for case in q["test_cases"]:
                exec(case, {"captured_output": captured})
            all_outs.append(q["expected_output"])
    assert len(set(all_outs)) == 120, "120 道题 expected_output 存在重复"
    print("OK: CH01 四档 120 道题全部通过校验（运行输出、断言、去重、格式）")


if __name__ == "__main__":
    main()
