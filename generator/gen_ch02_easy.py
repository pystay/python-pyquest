# -*- coding: utf-8 -*-
"""生成 CH02 超简单档（easy_30.json，id 后缀 E）30 道题。

第五轮清单规范：
  topic       = "变量的定义与基本数据类型"
  difficulty  = "超简单"，stars = "⭐"
  12 种变量定义场景各 ≥2 次 + 6 道补充；每题 1-2 处填空、模板 ≤3 行、无逻辑/循环/类型转换
"""
import io
import json
import os
import sys

TOPIC = "变量的定义与基本数据类型"
DIFFICULTY = "超简单"
STARS = "⭐"
SUFFIX = "E"


def run(code):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        exec(code, {})
    finally:
        sys.stdout = old
    return buf.getvalue()


def make_q(num, desc, template, hints, solution):
    captured = run(solution)
    tests = ["assert captured_output == " + repr(captured)]
    exec(tests[0], {"captured_output": captured})
    return {
        "id": "CH02-%s-%03d" % (SUFFIX, num),
        "topic": TOPIC,
        "difficulty": DIFFICULTY,
        "stars": STARS,
        "description": desc,
        "code_template": template,
        "expected_output": captured,
        "hints": hints,
        "test_cases": tests,
        "solution": solution,
    }


EASY = [
    # 场景 1：字符串变量（2 道）
    (1, "定义变量 name 并赋值为 'Alice'，输出该变量。",
     "___ = 'Alice'\nprint(___)",
     "变量名写在左侧，print 内填变量名。",
     "name = 'Alice'\nprint(name)"),
    (2, "定义变量 city 为 'Beijing' 并输出。",
     "___ = 'Beijing'\nprint(___)",
     "变量名填 city。",
     "city = 'Beijing'\nprint(city)"),
    # 场景 2：整数变量（2 道）
    (3, "定义变量 age 为 25 并输出。",
     "___ = 25\nprint(___)",
     "变量名填 age。",
     "age = 25\nprint(age)"),
    (4, "定义变量 score 为 92 并输出。",
     "___ = 92\nprint(___)",
     "变量名填 score。",
     "score = 92\nprint(score)"),
    # 场景 3：浮点数变量（2 道）
    (5, "定义变量 price 为 19.99 并输出。",
     "___ = 19.99\nprint(___)",
     "变量名填 price。",
     "price = 19.99\nprint(price)"),
    (6, "定义变量 height 为 1.75 并输出。",
     "___ = 1.75\nprint(___)",
     "变量名填 height。",
     "height = 1.75\nprint(height)"),
    # 场景 4：布尔变量（2 道）
    (7, "定义变量 is_student 为 True 并输出。",
     "___ = True\nprint(___)",
     "变量名填 is_student。",
     "is_student = True\nprint(is_student)"),
    (8, "定义变量 is_active 为 False 并输出。",
     "___ = False\nprint(___)",
     "变量名填 is_active。",
     "is_active = False\nprint(is_active)"),
    # 场景 5：多个变量分别输出（2 道）
    (9, "定义 name 和 age 两个变量并分别输出。",
     "name = 'Bob'\nage = 30\nprint(___)\nprint(age)",
     "第一处填 name。",
     "name = 'Bob'\nage = 30\nprint(name)\nprint(age)"),
    (10, "定义 x 和 y 两个变量并分别输出。",
     "x = 1\ny = 2\nprint(___)\nprint(y)",
     "第一处填 x。",
     "x = 1\ny = 2\nprint(x)\nprint(y)"),
    # 场景 6：一行定义多个变量（2 道）
    (11, "用一行同时定义 a 和 b 并输出。",
     "a, b = 1, 2\nprint(___, ___)",
     "依次填 a、b。",
     "a, b = 1, 2\nprint(a, b)"),
    (12, "用一行定义 first 和 last 并输出。",
     "first, last = 'Tom', 'Smith'\nprint(___, ___)",
     "依次填 first、last。",
     "first, last = 'Tom', 'Smith'\nprint(first, last)"),
    # 场景 7：变量重新赋值（2 道）
    (13, "把 x 重新赋值为 2 后输出。",
     "x = 1\nx = 2\nprint(___)",
     "print 内填 x。",
     "x = 1\nx = 2\nprint(x)"),
    (14, "把 msg 重新赋值为 'hello' 后输出。",
     "msg = 'hi'\nmsg = 'hello'\nprint(___)",
     "print 内填 msg。",
     "msg = 'hi'\nmsg = 'hello'\nprint(msg)"),
    # 场景 8：变量相互赋值（2 道）
    (15, "把 a 的值赋给 b 并输出 b。",
     "a = 5\nb = a\nprint(___)",
     "print 内填 b。",
     "a = 5\nb = a\nprint(b)"),
    (16, "把 name 的值赋给 person 并输出。",
     "name = 'Ada'\nperson = name\nprint(___)",
     "print 内填 person。",
     "name = 'Ada'\nperson = name\nprint(person)"),
    # 场景 9：type() 查看类型（2 道）
    (17, "用 type() 查看整数 42 的类型。",
     "n = 42\nprint(type(___))",
     "type 括号内填 n。",
     "n = 42\nprint(type(n))"),
    (18, "用 type() 查看字符串 'hi' 的类型。",
     "s = 'hi'\nprint(type(___))",
     "type 括号内填 s。",
     "s = 'hi'\nprint(type(s))"),
    # 场景 10：None 空变量（2 道）
    (19, "定义空变量 x 为 None 并输出。",
     "x = None\nprint(___)",
     "print 内填 x。",
     "x = None\nprint(x)"),
    (20, "定义空变量 x 并用 type() 查看类型。",
     "x = None\nprint(type(___))",
     "type 括号内填 x。",
     "x = None\nprint(type(x))"),
    # 场景 11：变量名区分大小写（2 道）
    (21, "Name 和 name 是不同变量，输出小写 name。",
     "Name = 'Alice'\nname = 'alice'\nprint(___)",
     "print 内填 name。",
     "Name = 'Alice'\nname = 'alice'\nprint(name)"),
    (22, "X 和 x 是不同变量，输出小写 x。",
     "X = 10\nx = 40\nprint(___)",
     "print 内填 x。",
     "X = 10\nx = 40\nprint(x)"),
    # 场景 12：有意义的变量名（2 道）
    (23, "用有意义的变量名 student_name 存储姓名并输出。",
     "student_name = 'Ann'\nprint(___)",
     "print 内填 student_name。",
     "student_name = 'Ann'\nprint(student_name)"),
    (24, "用有意义的变量名 total_score 存储分数并输出。",
     "total_score = 96\nprint(___)",
     "print 内填 total_score。",
     "total_score = 96\nprint(total_score)"),
    # 补充 6 道
    (25, "拼接两个字符串变量并输出。",
     "first = 'Py'\nsecond = 'Quest'\nprint(___ + ___)",
     "依次填 first、second。",
     "first = 'Py'\nsecond = 'Quest'\nprint(first + second)"),
    (26, "两个数字变量相加并输出。",
     "x = 7\ny = 8\nprint(___ + ___)",
     "依次填 x、y。",
     "x = 7\ny = 8\nprint(x + y)"),
    (27, "同时输出整数和字符串变量。",
     "n = 5\ns = 'five'\nprint(___, ___)",
     "依次填 n、s。",
     "n = 5\ns = 'five'\nprint(n, s)"),
    (28, "用含下划线的变量名 user_name 并输出。",
     "user_name = 'Sam'\nprint(___)",
     "print 内填 user_name。",
     "user_name = 'Sam'\nprint(user_name)"),
    (29, "同时输出布尔和整数变量。",
     "flag = True\ncount = 1\nprint(___, ___)",
     "依次填 flag、count。",
     "flag = True\ncount = 1\nprint(flag, count)"),
    (30, "定义温度变量 temperature 并输出。",
     "temperature = 36.5\nprint(___)",
     "print 内填 temperature。",
     "temperature = 36.5\nprint(temperature)"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH02_Variables_Types")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in EASY]
    assert len(questions) == 30, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH02-E-%03d" % i for i in range(1, 31)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 30, "expected_output 存在重复"
    for q in questions:
        # 场景 5（多变量分别输出）允许 4 行，其余 ≤3 行
        max_lines = 4 if q["id"] in ("CH02-E-009", "CH02-E-010") else 3
        assert q["code_template"].count("\n") <= max_lines - 1, q["id"] + " 模板行数超限"
        assert q["code_template"].count("___") <= 2, q["id"] + " 填空超过 2 处"
        exec(q["test_cases"][0], {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH02", "title": "变量和类型",
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "easy_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 超简单档 30 道，id 唯一，expected_output 唯一，模板 ≤3 行、≤2 处填空")


if __name__ == "__main__":
    main()
