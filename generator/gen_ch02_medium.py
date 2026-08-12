# -*- coding: utf-8 -*-
"""生成 CH02 简单档（medium_30.json，id 后缀 M）30 道题。

第六轮清单规范：
  topic       = "变量赋值与数据类型转换"
  difficulty  = "简单"，stars = "⭐⭐"
  12 种类型转换场景各 ≥2 次 + 6 道补充；每题 2-3 处填空、模板 ≤8 行、单个转换函数
"""
import io
import json
import os
import sys

TOPIC = "变量赋值与数据类型转换"
DIFFICULTY = "简单"
STARS = "⭐⭐"
SUFFIX = "M"


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


MEDIUM = [
    # 场景 1：字符串 → 整数（2 道）
    (1, "把字符串 '123' 转成整数并赋值给 num_int 后输出。",
     "num_str = '123'\n___ = int(num_str)\nprint(___)",
     "定义变量 num_int 接收 int() 结果。",
     "num_str = '123'\nnum_int = int(num_str)\nprint(num_int)"),
    (2, "把字符串 '22' 转成整数 age，输出 age + 5。",
     "age_str = '22'\n___ = int(age_str)\nprint(___ + 5)",
     "用 int() 转换后参与运算。",
     "age_str = '22'\nage = int(age_str)\nprint(age + 5)"),
    # 场景 2：字符串 → 浮点数（2 道）
    (3, "把字符串 '3.14' 转成浮点数 pi 并输出。",
     "pi_str = '3.14'\n___ = float(pi_str)\nprint(___)",
     "用 float() 转换。",
     "pi_str = '3.14'\npi = float(pi_str)\nprint(pi)"),
    (4, "把字符串 '92.5' 转成浮点数 score，输出两倍。",
     "score_str = '92.5'\n___ = float(score_str)\nprint(___ * 2)",
     "用 float() 转换后乘 2。",
     "score_str = '92.5'\nscore = float(score_str)\nprint(score * 2)"),
    # 场景 3：整数 → 字符串（2 道）
    (5, "把整数 42 转成字符串 s 并输出。",
     "n = 42\n___ = str(n)\nprint(___)",
     "用 str() 转换。",
     "n = 42\ns = str(n)\nprint(s)"),
    (6, "把整数 count 转成字符串拼接进消息。",
     "count = 7\nmsg = \"Count: \" + ___(count)\nprint(___)",
     "str() 转换后才能与字符串拼接。",
     "count = 7\nmsg = \"Count: \" + str(count)\nprint(msg)"),
    # 场景 4：浮点数 → 字符串（2 道）
    (7, "把浮点数 9.99 转成字符串 s 并输出。",
     "price = 9.99\n___ = str(price)\nprint(___)",
     "用 str() 转换。",
     "price = 9.99\ns = str(price)\nprint(s)"),
    (8, "把浮点数 pi 转成字符串拼接输出。",
     "pi = 3.14\nmsg = \"Pi is \" + ___(pi)\nprint(___)",
     "str() 转换后拼接。",
     "pi = 3.14\nmsg = \"Pi is \" + str(pi)\nprint(msg)"),
    # 场景 5：整数 → 浮点数（2 道）
    (9, "把整数 5 转成浮点数 f 并输出。",
     "n = 5\n___ = float(n)\nprint(___)",
     "用 float() 转换。",
     "n = 5\nf = float(n)\nprint(f)"),
    (10, "把整数 x 转成浮点数参与除法。",
     "x = 10\n___ = float(x)\nprint(___ / 4)",
     "float(x) 转换后除以 4。",
     "x = 10\nf = float(x)\nprint(f / 4)"),
    # 场景 6：浮点数 → 整数（截断）（2 道）
    (11, "把浮点数 3.99 转成整数 n（截断）并输出。",
     "f = 3.99\n___ = int(f)\nprint(___)",
     "int() 截断小数部分。",
     "f = 3.99\nn = int(f)\nprint(n)"),
    (12, "把负数 -2.7 转成整数（截断）并输出。",
     "f = -2.7\n___ = int(f)\nprint(___)",
     "int() 向零截断。",
     "f = -2.7\nn = int(f)\nprint(n)"),
    # 场景 7：字符串 → 布尔（2 道）
    (13, "把非空字符串 'hi' 转成布尔并输出。",
     "s = \"hi\"\nb = ___(s)\nprint(\"str truthy:\", ___)",
     "非空字符串 bool() 为 True。",
     "s = \"hi\"\nb = bool(s)\nprint(\"str truthy:\", b)"),
    (14, "把空字符串转成布尔并输出。",
     "empty = \"\"\nb = ___(empty)\nprint(\"str falsy:\", ___)",
     "空字符串 bool() 为 False。",
     "empty = \"\"\nb = bool(empty)\nprint(\"str falsy:\", b)"),
    # 场景 8：数字 → 布尔（2 道）
    (15, "把非零数字 5 转成布尔并输出。",
     "n = 5\nb = ___(n)\nprint(\"num truthy:\", ___)",
     "非零数字 bool() 为 True。",
     "n = 5\nb = bool(n)\nprint(\"num truthy:\", b)"),
    (16, "把数字 0 转成布尔并输出。",
     "zero = 0\nb = ___(zero)\nprint(\"num falsy:\", ___)",
     "数字 0 bool() 为 False。",
     "zero = 0\nb = bool(zero)\nprint(\"num falsy:\", b)"),
    # 场景 9：type() 查看转换后类型（2 道）
    (17, "把字符串 '42' 转整数后用 type() 查看类型。",
     "s = \"42\"\n___ = int(s)\nprint(\"converted type:\", ___(n))",
     "type() 查看转换后的类型。",
     "s = \"42\"\nn = int(s)\nprint(\"converted type:\", type(n))"),
    (18, "把字符串 '3.5' 转浮点数后用 type() 查看类型。",
     "s = \"3.5\"\n___ = float(s)\nprint(___(f))",
     "type() 查看转换后的类型。",
     "s = \"3.5\"\nf = float(s)\nprint(type(f))"),
    # 场景 10：混合类型运算自动转换（2 道）
    (19, "整数与浮点数相加，观察自动转换。",
     "a = 3\nb = 2.5\nprint(___ + ___)",
     "int + float 结果为 float。",
     "a = 3\nb = 2.5\nprint(a + b)"),
    (20, "整数与浮点数相乘，观察自动转换。",
     "x = 10\ny = 3.0\nprint(___ * ___)",
     "int * float 结果为 float。",
     "x = 10\ny = 3.0\nprint(x * y)"),
    # 场景 11：模拟输入后转换（2 道）
    (21, "模拟 input 得到字符串 '1.8'，转浮点数后输出。",
     "height_str = '1.8'  # 模拟 input()\n___ = float(height_str)\nprint(___)",
     "把字符串转成浮点数。",
     "height_str = '1.8'  # 模拟 input()\nheight = float(height_str)\nprint(height)"),
    (22, "模拟 input 得到字符串 '8'，转整数后输出平方。",
     "num_str = '8'  # 模拟 input()\n___ = int(num_str)\nprint(___ ** 2)",
     "int() 转换后求平方。",
     "num_str = '8'  # 模拟 input()\nnum = int(num_str)\nprint(num ** 2)"),
    # 场景 12：转换前后类型对比（2 道）
    (23, "对比字符串 '123' 转换前后的类型。",
     "s = \"123\"\n___ = int(s)\nprint(type(s), ___(n))",
     "type() 对比 str 与 int。",
     "s = \"123\"\nprint(type(s), type(int(s)))"),
    (24, "对比浮点数 3.14 转换前后的类型。",
     "n = 3.14\n___ = str(n)\nprint(type(n), ___(s))",
     "type() 对比 float 与 str。",
     "n = 3.14\nprint(type(n), type(str(n)))"),
    # 补充 6 道
    (25, "把 None 转成布尔并输出。",
     "n = None\nb = ___(n)\nprint(\"None is falsy:\", ___)",
     "None 的 bool() 为 False。",
     "n = None\nb = bool(n)\nprint(\"None is falsy:\", b)"),
    (26, "把整数 25 转成字符串拼接输出。",
     "value = 25\nmsg = \"Value: \" + ___(value)\nprint(___)",
     "str() 转换后拼接。",
     "value = 25\nmsg = \"Value: \" + str(value)\nprint(msg)"),
    (27, "输出混合运算结果及其类型。",
     "a = 3\nb = 4.0\n___ = a + b\nprint(___(result), result)",
     "type() 查看 int+float 的结果类型。",
     "a = 3\nb = 4.0\nresult = a + b\nprint(type(result), result)"),
    (28, "把 7.9 转整数后加 1 并输出。",
     "f = 7.9\n___ = int(f)\nprint(___ + 1)",
     "int() 截断后加 1。",
     "f = 7.9\nn = int(f)\nprint(n + 1)"),
    (29, "字符串转整数再转回字符串并重复。",
     "s = \"123\"\n___ = int(s)\ns2 = ___(n)\nprint(s2 * 2)",
     "str() 转回字符串后可重复。",
     "s = \"123\"\nn = int(s)\ns2 = str(n)\nprint(s2 * 2)"),
    (30, "把两个数字字符串转整数后求和。",
     "a = \"15\"\nb = \"26\"\nprint(___ + ___)",
     "int() 转换两个字符串后相加。",
     "a = \"15\"\nb = \"26\"\nprint(int(a) + int(b))"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH02_Variables_Types")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in MEDIUM]
    assert len(questions) == 30, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH02-M-%03d" % i for i in range(1, 31)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 30, "expected_output 存在重复"
    for q in questions:
        assert q["code_template"].count("\n") <= 7, q["id"] + " 模板超过 8 行"
        assert q["code_template"].count("___") in (2, 3), q["id"] + " 填空数不在 2-3 处"
        exec(q["test_cases"][0], {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH02", "title": "变量和类型",
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "medium_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 简单档 30 道，id 唯一，expected_output 唯一，模板 ≤8 行、2-3 处填空")


if __name__ == "__main__":
    main()
