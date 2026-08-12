# -*- coding: utf-8 -*-
"""生成 CH02 中等档（hard_30.json，id 后缀 H）20 道题。

第七轮清单规范：
  topic       = "变量在运算、比较和逻辑中的综合应用"
  difficulty  = "中等"，stars = "⭐⭐⭐"
  10 种综合场景各 ≥2 次；逻辑难度：≥6 if-elif-else、≥6 循环、≥4 列表/字典、≥4 复杂表达式
  每题 3 个 assert（精确匹配 + 换行数 + 去空白）
"""
import io
import json
import os
import sys

TOPIC = "变量在运算、比较和逻辑中的综合应用"
DIFFICULTY = "中等"
STARS = "⭐⭐⭐"
SUFFIX = "H"


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
    tests = [
        "assert captured_output == " + repr(captured),
        "assert captured_output.count(chr(10)) == %d" % captured.count("\n"),
    ]
    if captured.strip():
        tests.append("assert captured_output.strip() == " + repr(captured.strip()))
    for t in tests:
        exec(t, {"captured_output": captured})
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
    # 场景 1：算术运算组合（2 道）
    (1, "定义 a=10、b=3，把六种算术运算结果存入列表并逐行输出。",
     "a = 10\nb = 3\n# 请把 a+b、a-b、a*b、a/b、a//b、a%b 存入列表并逐行输出\n___ = [a + b, a - b, a * b, a / b, a // b, a % b]\nfor r in ___:\n    print(r)",
     "先算六种结果存列表，再遍历输出。",
     "a = 10\nb = 3\nresults = [a + b, a - b, a * b, a / b, a // b, a % b]\nfor r in results:\n    print(r)"),
    (2, "定义 x=7、y=2，一次输出六种算术运算结果。",
     "x = 7\ny = 2\nprint(___, ___, ___, ___, ___, ___)",
     "依次填 x+y、x-y、x*y、x**y、x//y、x%y。",
     "x = 7\ny = 2\nprint(x + y, x - y, x * y, x ** y, x // y, x % y)"),
    # 场景 2：比较运算（2 道）
    (3, "定义 a=5、b=8，输出两组比较结果并按大小输出提示。",
     "a = 5\nb = 8\nprint(___ > b, a < ___)\nif a < b:\n    print(\"b is bigger\")\nelse:\n    print(\"a is bigger\")",
     "依次填 a、b；if-else 判断大小。",
     "a = 5\nb = 8\nprint(a > b, a < b)\nif a < b:\n    print(\"b is bigger\")\nelse:\n    print(\"a is bigger\")"),
    (4, "定义 x=10、y=10，输出四种比较运算结果。",
     "x = 10\ny = 10\nprint(___ == ___, x >= ___, ___ <= y, x != y)",
     "依次填 x、y、y、x。",
     "x = 10\ny = 10\nprint(x == y, x >= y, x <= y, x != y)"),
    # 场景 3：逻辑运算（2 道）
    (5, "定义 a=True、b=False，用 if-elif-else 判断逻辑组合并输出。",
     "a = True\nb = False\nif a ___ b:\n    print(\"both\")\nelif a ___ b:\n    print(\"one\")\nelse:\n    print(\"none\")",
     "依次填 and、or。",
     "a = True\nb = False\nif a and b:\n    print(\"both\")\nelif a or b:\n    print(\"one\")\nelse:\n    print(\"none\")"),
    (6, "定义 x=5，输出三组逻辑与比较混合运算结果。",
     "x = 5\nprint(___ > 3 ___ x < 10, x == 5 ___ x > 10, ___ (x < 0))",
     "依次填 x、and、or、not。",
     "x = 5\nprint(x > 3 and x < 10, x == 5 or x > 10, not (x < 0))"),
    # 场景 4：混合运算综合（2 道）
    (7, "定义 a=4、b=6，用混合表达式做条件判断并输出。",
     "a = 4\nb = 6\nif (___ + b) > 9 ___ a < b:\n    print(\"big and ordered\")\nelse:\n    print(\"other\")",
     "依次填 a、and。",
     "a = 4\nb = 6\nif (a + b) > 9 and a < b:\n    print(\"big and ordered\")\nelse:\n    print(\"other\")"),
    (8, "定义 x=3、y=4，输出三个复杂表达式的结果。",
     "x = 3\ny = 4\nprint(___ ** 2 + y ** 2, (___ + y) ** 2 // 5, (x + ___) % 5)",
     "依次填 x、x、y。",
     "x = 3\ny = 4\nprint(x ** 2 + y ** 2, (x + y) ** 2 // 5, (x + y) % 5)"),
    # 场景 5：条件判断（2 道）
    (9, "定义 score=85，用 if-elif-else 输出成绩等级。",
     "score = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(f\"Grade: {___}\")",
     "输出变量 grade。",
     "score = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(f\"Grade: {grade}\")"),
    (10, "定义 n=-3，用 if-elif-else 判断正负零并输出。",
     "n = ___\nif n > 0:\n    print(n, \"is positive\")\nelif n < 0:\n    print(n, \"is negative\")\nelse:\n    print(n, \"is zero\")",
     "填 -3。",
     "n = -3\nif n > 0:\n    print(n, \"is positive\")\nelif n < 0:\n    print(n, \"is negative\")\nelse:\n    print(n, \"is zero\")"),
    # 场景 6：循环累加/累乘（2 道）
    (11, "用 for 循环累加 1 到 10 并输出总和。",
     "total = 0\nfor i in range(1, 11):\n    total += i\nprint(f\"Sum: {___}\")",
     "输出 total。",
     "total = 0\nfor i in range(1, 11):\n    total += i\nprint(f\"Sum: {total}\")"),
    (12, "用 while 循环累乘 1 到 5 并输出结果。",
     "product = 1\ni = 1\nwhile i <= 5:\n    ___ *= i\n    i += 1\nprint(f\"Product: {___}\")",
     "依次填 product、product。",
     "product = 1\ni = 1\nwhile i <= 5:\n    product *= i\n    i += 1\nprint(f\"Product: {product}\")"),
    # 场景 7：类型自动转换（2 道）
    (13, "遍历混合类型列表，输出每个值与类型名。",
     "for v in [3, 2.0]:\n    print(v, type(___).__name__)",
     "type 内填 v。",
     "for v in [3, 2.0]:\n    print(v, type(v).__name__)"),
    (14, "定义 n=10，输出除法、整除和混合乘法的结果。",
     "n = 10\nprint(n / ___, n // ___, n * 1.5)",
     "依次填 4、4。",
     "n = 10\nprint(n / 4, n // 4, n * 1.5)"),
    # 场景 8：round() 精度（2 道）
    (15, "定义 pi=3.14159，用 round() 保留两位小数输出。",
     "pi = 3.14159\nprint(f\"Rounded: {___(pi, 2)}\")",
     "round(pi, 2) 保留两位。",
     "pi = 3.14159\nprint(f\"Rounded: {round(pi, 2)}\")"),
    (16, "遍历浮点数列表，逐行用 round() 保留两位小数。",
     "for v in [2.675, 3.14159]:\n    print(round(___, 2))",
     "round 内填 v。",
     "for v in [2.675, 3.14159]:\n    print(round(v, 2))"),
    # 场景 9：列表/字典存储与访问（2 道）
    (17, "定义 a=5、b=3，把运算结果存入列表并按条件输出。",
     "a = 5\nb = 3\nnums = [a + b, a - b, a * b]\nif nums[2] > 10:\n    print(___, \"big product\")\nelse:\n    print(nums)",
     "输出 nums。",
     "a = 5\nb = 3\nnums = [a + b, a - b, a * b]\nif nums[2] > 10:\n    print(nums, \"big product\")\nelse:\n    print(nums)"),
    (18, "定义 a=10、b=20，把运算结果存入字典并按键访问。",
     "a = 10\nb = 20\nd = {\"sum\": a + b, \"diff\": b - a}\nprint(d[___], d[___])",
     "依次填 \"sum\"、\"diff\"。",
     "a = 10\nb = 20\nd = {\"sum\": a + b, \"diff\": b - a}\nprint(d[\"sum\"], d[\"diff\"])"),
    # 场景 10：多变量同步更新（2 道）
    (19, "a=1、b=2，用循环同步更新两变量并输出。",
     "a, b = 1, 2\nfor _ in range(3):\n    ___, ___ = b, a + b\nprint(a, b)",
     "斐波那契式同步更新。",
     "a, b = 1, 2\nfor _ in range(3):\n    a, b = b, a + b\nprint(a, b)"),
    (20, "循环累加并把每次结果收集到列表输出。",
     "total = 0\nsums = []\nfor i in range(1, 6):\n    total += i\n    sums.___(total)\nprint(sums)",
     "append 收集。",
     "total = 0\nsums = []\nfor i in range(1, 6):\n    total += i\n    sums.append(total)\nprint(sums)"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH02_Variables_Types")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in MEDIUM]
    assert len(questions) == 20, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH02-H-%03d" % i for i in range(1, 21)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 20, "expected_output 存在重复"
    for q in questions:
        assert len(q["test_cases"]) >= 2, q["id"]
        for t in q["test_cases"]:
            exec(t, {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH02", "title": "变量和类型",
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "hard_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 中等档 20 道，id 唯一，expected_output 唯一")


if __name__ == "__main__":
    main()
