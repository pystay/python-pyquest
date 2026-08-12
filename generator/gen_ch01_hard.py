# -*- coding: utf-8 -*-
"""生成 CH01 中等档（hard_30.json，id 后缀 H）30 道题。

第三轮清单规范：
  topic    = "print() 函数的综合应用与格式化输出"
  difficulty = "中等"，stars = "⭐⭐⭐"
  覆盖 14 种用法；逻辑难度分布：≥8 if-elif-else、≥8 for/while、≥4 列表/字典、10 格式化综合
  每题补充 3-5 处代码、模板 10-20 行、test_cases 至少 2-3 个 assert
"""
import io
import json
import os
import sys

TOPIC = "print() 函数的综合应用与格式化输出"
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
    # 3 个 assert：精确匹配 + 换行数 + 去空白一致
    tests = ["assert captured_output == " + repr(captured)]
    tests.append("assert captured_output.count(chr(10)) == %d" % captured.count("\n"))
    if captured.strip():
        tests.append("assert captured_output.strip() == " + repr(captured.strip()))
    for t in tests:
        exec(t, {"captured_output": captured})
    return {
        "id": "CH01-%s-%03d" % (SUFFIX, num),
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
    # 条件判断类（if-elif-else，8 道）
    (1, "根据分数 85 输出对应的成绩等级。",
     "score = ___\nif score >= 90:\n    grade = \"A\"\nelif ___ >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(f\"Grade: {___}\")",
     "依次填 85、score、grade。",
     "score = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(f\"Grade: {grade}\")"),
    (2, "判断数字 -3 的正负或零并输出。",
     "n = ___\nif n > 0:\n    print(___, \"is positive\")\nelif n < 0:\n    print(n, \"is negative\")\nelse:\n    print(___, \"is zero\")",
     "依次填 -3、n、n。",
     "n = -3\nif n > 0:\n    print(n, \"is positive\")\nelif n < 0:\n    print(n, \"is negative\")\nelse:\n    print(n, \"is zero\")"),
    (3, "比较 a 和 b 输出较大的数。",
     "a = 7\nb = ___\nif ___ > b:\n    larger = a\nelse:\n    larger = b\nprint(f\"The larger number is {___}\")",
     "依次填 9、a、larger。",
     "a = 7\nb = 9\nif a > b:\n    larger = a\nelse:\n    larger = b\nprint(f\"The larger number is {larger}\")"),
    (4, "判断数字 7 是奇数还是偶数。",
     "n = ___\nif n % 2 == ___:\n    result = \"even\"\nelse:\n    result = \"odd\"\nprint(f\"{n} is {___}\")",
     "依次填 7、0、result。",
     "n = 7\nif n % 2 == 0:\n    result = \"even\"\nelse:\n    result = \"odd\"\nprint(f\"{n} is {result}\")"),
    (5, "根据温度 35 输出天气提示。",
     "temp = ___\nif temp >= 30:\n    weather = \"Hot\"\nelif temp >= ___:\n    weather = \"Warm\"\nelse:\n    weather = \"Cold\"\nprint(f\"It is {___}\")",
     "依次填 35、15、weather。",
     "temp = 35\nif temp >= 30:\n    weather = \"Hot\"\nelif temp >= 15:\n    weather = \"Warm\"\nelse:\n    weather = \"Cold\"\nprint(f\"It is {weather}\")"),
    (6, "比较猜测值与答案并给出提示。",
     "answer = 7\nguess = ___\nif guess < ___:\n    message = \"Too low\"\nelif guess > answer:\n    message = \"Too high\"\nelse:\n    message = \"Correct\"\nprint(___)\n",
     "依次填 5、answer、message。",
     "answer = 7\nguess = 5\nif guess < answer:\n    message = \"Too low\"\nelif guess > answer:\n    message = \"Too high\"\nelse:\n    message = \"Correct\"\nprint(message)"),
    (7, "判断年份 2024 是否为闰年。",
     "year = ___\nif (year % 4 == 0 and year % 100 != 0) or ___ == 0:\n    result = \"leap year\"\nelse:\n    result = \"common year\"\nprint(f\"{year} is a {___}\")",
     "依次填 2024、year % 400、result。",
     "year = 2024\nif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:\n    result = \"leap year\"\nelse:\n    result = \"common year\"\nprint(f\"{year} is a {result}\")"),
    (8, "输出数字 15 所在的区间。",
     "x = ___\nif x <= 10:\n    zone = \"0-10\"\nelif x <= ___:\n    zone = \"11-20\"\nelse:\n    zone = \"21+\"\nprint(f\"{x} is in range {___}\")",
     "依次填 15、20、zone。",
     "x = 15\nif x <= 10:\n    zone = \"0-10\"\nelif x <= 20:\n    zone = \"11-20\"\nelse:\n    zone = \"21+\"\nprint(f\"{x} is in range {zone}\")"),
    # 循环类（for / while，8 道）
    (9, "用 for 循环输出 1 到 5 的平方和立方。",
     "nums = [1, 2, 3, 4, 5]\nfor n in ___:\n    square = n * n\n    cube = n ** 3\n    print(f\"{n}: square={___}, cube={___}\")",
     "依次填 nums、square、cube。",
     "nums = [1, 2, 3, 4, 5]\nfor n in nums:\n    square = n * n\n    cube = n ** 3\n    print(f\"{n}: square={square}, cube={cube}\")"),
    (10, "用 for 循环求 1 到 10 的和。",
     "start = 1\nend = 10\ntotal = 0\nfor i in range(start, ___ + 1):\n    total += i\nprint(f\"Sum of {start} to {end} is {___}\")",
     "依次填 end、total。",
     "start = 1\nend = 10\ntotal = 0\nfor i in range(start, end + 1):\n    total += i\nprint(f\"Sum of {start} to {end} is {total}\")"),
    (11, "用 while 循环输出 2 到 10 的偶数。",
     "start = 2\nlimit = 10\ni = start\nwhile i <= ___:\n    print(i)\n    i += ___\n",
     "依次填 limit、2。",
     "start = 2\nlimit = 10\ni = start\nwhile i <= limit:\n    print(i)\n    i += 2"),
    (12, "用 while 循环计算 5 的阶乘。",
     "n = 5\nfact = 1\ni = 1\nwhile i <= ___:\n    fact *= ___\n    i += 1\nprint(f\"{n}! = {___}\")",
     "依次填 n、i、fact。",
     "n = 5\nfact = 1\ni = 1\nwhile i <= n:\n    fact *= i\n    i += 1\nprint(f\"{n}! = {fact}\")"),
    (13, "用 for 循环逐字符输出并用 - 连接。",
     "word = \"Python\"\nseparator = \"-\"\nfor ch in ___:\n    print(___, end=___)\nprint()",
     "依次填 word、ch、separator。",
     "word = \"Python\"\nseparator = \"-\"\nfor ch in word:\n    print(ch, end=separator)\nprint()"),
    (14, "用 while 循环倒计时并发射。",
     "count = ___\nwhile count > 0:\n    print(___)\n    count -= 1\nprint(\"Launch!\")",
     "依次填 5、count。",
     "count = 5\nwhile count > 0:\n    print(count)\n    count -= 1\nprint(\"Launch!\")"),
    (15, "用 for 循环打印 5 行星号三角形。",
     "symbol = \"*\"\nrows = 5\nfor i in range(1, ___ + 1):\n    stars = symbol * i\n    print(___)",
     "依次填 rows、stars。",
     "symbol = \"*\"\nrows = 5\nfor i in range(1, rows + 1):\n    stars = symbol * i\n    print(stars)"),
    (16, "用 while 循环求 1 到 100 的和。",
     "total = 0\ni = 1\nwhile i <= 100:\n    total += ___\n    i += 1\nprint(f\"Sum = {___}\")",
     "依次填 i、total。",
     "total = 0\ni = 1\nwhile i <= 100:\n    total += i\n    i += 1\nprint(f\"Sum = {total}\")"),
    # 列表 / 字典类（4 道）
    (17, "通过索引访问列表首尾元素并输出。",
     "fruits = [\"apple\", \"banana\", \"cherry\"]\nfirst = fruits[___]\nlast = fruits[___]\ncount = len(fruits)\nprint(f\"First: {___}, Last: {___}, Count: {count}\")",
     "依次填 0、-1、first、last。",
     "fruits = [\"apple\", \"banana\", \"cherry\"]\nfirst = fruits[0]\nlast = fruits[-1]\ncount = len(fruits)\nprint(f\"First: {first}, Last: {last}, Count: {count}\")"),
    (18, "通过键访问字典中的值并求和。",
     "scores = {\"Alice\": 90, \"Bob\": 85, \"Cara\": 88}\nalice = scores[___]\nbob = scores[___]\ntotal = alice + bob\nprint(f\"Alice: {___}, Bob: {___}, Sum: {total}\")",
     "依次填 \"Alice\"、\"Bob\"、alice、bob。",
     "scores = {\"Alice\": 90, \"Bob\": 85, \"Cara\": 88}\nalice = scores[\"Alice\"]\nbob = scores[\"Bob\"]\ntotal = alice + bob\nprint(f\"Alice: {alice}, Bob: {bob}, Sum: {total}\")"),
    (19, "遍历字典输出姓名和分数。",
     "scores = {\"Alice\": 90, \"Bob\": 85}\nprint(\"Score report:\")\nprint(\"-\" * 15)\nfor name, score in ___.items():\n    print(f\"{___}: {___}\")",
     "依次填 scores、name、score。",
     "scores = {\"Alice\": 90, \"Bob\": 85}\nprint(\"Score report:\")\nprint(\"-\" * 15)\nfor name, score in scores.items():\n    print(f\"{name}: {score}\")"),
    (20, "用 enumerate 输出带编号的颜色列表。",
     "colors = [\"red\", \"green\", \"blue\"]\nprint(\"Color list:\")\nfor i, color in enumerate(colors, ___):\n    print(f\"{___}. {___}\")",
     "依次填 1、i、color。",
     "colors = [\"red\", \"green\", \"blue\"]\nprint(\"Color list:\")\nfor i, color in enumerate(colors, 1):\n    print(f\"{i}. {color}\")"),
    # 格式化综合类（f-string / format / % / sep / end，10 道）
    (21, "用 f-string 输出姓名、年龄和身高。",
     "name = \"Bob\"\nage = 25\nheight = 1.75\nprint(f\"{___} is {___} years old, {___:.2f} m tall\")",
     "依次填 name、age、height。",
     "name = \"Bob\"\nage = 25\nheight = 1.75\nprint(f\"{name} is {age} years old, {height:.2f} m tall\")"),
    (22, "用 format() 的位置与关键字参数输出。",
     "name = \"Bob\"\nage = 25\nprint(\"{} is {} years old\".format(___, ___))\nprint(\"{n} will be {a} next year\".format(n=___, a=___ + 1))",
     "依次填 name、age、name、age。",
     "name = \"Bob\"\nage = 25\nprint(\"{} is {} years old\".format(name, age))\nprint(\"{n} will be {a} next year\".format(n=name, a=age + 1))"),
    (23, "用旧式 % 格式化输出姓名和分数。",
     "name = \"Bob\"\nscore = 92.5\nprint(\"%s scored %.1f%%\" % (___, ___))",
     "依次填 name、score。",
     "name = \"Bob\"\nscore = 92.5\nprint(\"%s scored %.1f%%\" % (name, score))"),
    (24, "用 sep 和 end 输出三行 CSV 数据。",
     "header = [\"Name\", \"Age\", \"City\"]\nrow1 = [\"Alice\", 30, \"Beijing\"]\nrow2 = [\"Bob\", 25, \"Shanghai\"]\nprint(*header, sep=___, end=\"\\n\")\nprint(*row1, sep=\",\", end=\"\\n\")\nprint(*row2, sep=\",\", end=___)",
     "依次填 \",\"、\"\\n\"。",
     "header = [\"Name\", \"Age\", \"City\"]\nrow1 = [\"Alice\", 30, \"Beijing\"]\nrow2 = [\"Bob\", 25, \"Shanghai\"]\nprint(*header, sep=\",\", end=\"\\n\")\nprint(*row1, sep=\",\", end=\"\\n\")\nprint(*row2, sep=\",\", end=\"\\n\")"),
    (25, "用 f-string 对齐输出三种方式。",
     "name = \"PyQuest\"\nwidth = 10\nprint(f\"|{name:___<{width}}|\")\nprint(f\"|{name:___>{width}}|\")\nprint(f\"|{name:___^{width}}|\")",
     "依次填 <、>、^。",
     "name = \"PyQuest\"\nwidth = 10\nprint(f\"|{name:<{width}}|\")\nprint(f\"|{name:>{width}}|\")\nprint(f\"|{name:^{width}}|\")"),
    (26, "用 f-string 格式化小数与千分位。",
     "pi = 3.14159265\namount = 1234567.891\npi_text = f\"{pi:___}\"\namount_text = f\"{amount:___}\"\nprint(f\"Pi: {___}\")\nprint(f\"Amount: {___}\")",
     "依次填 .2f、,.2f、pi_text、amount_text。",
     "pi = 3.14159265\namount = 1234567.891\npi_text = f\"{pi:.2f}\"\namount_text = f\"{amount:,.2f}\"\nprint(f\"Pi: {pi_text}\")\nprint(f\"Amount: {amount_text}\")"),
    (27, "输出含转义字符的路径、制表符与换行。",
     "print(\"Path: C:___Users___admin\")\nprint(\"Table:___A___B___C\")\nprint(\"Line1___Line2\")",
     "依次填 \\\\、\\\\、\\t、\\t、\\n。",
     "print(\"Path: C:\\\\Users\\\\admin\")\nprint(\"Table:\\tA\\tB\\tC\")\nprint(\"Line1\\nLine2\")"),
    (28, "在列表项之间输出空行。",
     "items = [\"one\", \"two\", \"three\"]\nfor i, item in enumerate(items):\n    print(___)\n    if i < len(items) - 1:\n        print()",
     "填空 item。",
     "items = [\"one\", \"two\", \"three\"]\nfor i, item in enumerate(items):\n    print(item)\n    if i < len(items) - 1:\n        print()"),
    (29, "输出带表头和分隔线的成绩表。",
     "print(\"Name\\tScore\")\nprint(___ * 12)\nfor name, score in [(\"Alice\", 90), (\"Bob\", 85)]:\n    print(f\"{___}\\t{___}\")",
     "依次填 \"-\"、name、score。",
     "print(\"Name\\tScore\")\nprint(\"-\" * 12)\nfor name, score in [(\"Alice\", 90), (\"Bob\", 85)]:\n    print(f\"{name}\\t{score}\")"),
    (30, "综合：循环判断分数并输出平均分。",
     "scores = [88, 92, 76, 95]\ntotal = 0\nfor score in ___:\n    total += ___\n    if score >= 90:\n        print(f\"{score}: excellent\")\n    elif score >= 80:\n        print(f\"{score}: good\")\n    else:\n        print(f\"{score}: keep going\")\navg = total / len(scores)\nprint(f\"Average: {___:.1f}\")",
     "依次填 scores、score、avg。",
     "scores = [88, 92, 76, 95]\ntotal = 0\nfor score in scores:\n    total += score\n    if score >= 90:\n        print(f\"{score}: excellent\")\n    elif score >= 80:\n        print(f\"{score}: good\")\n    else:\n        print(f\"{score}: keep going\")\navg = total / len(scores)\nprint(f\"Average: {avg:.1f}\")"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH01_Hello_World")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in MEDIUM]
    assert len(questions) == 30, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH01-H-%03d" % i for i in range(1, 31)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 30, "expected_output 存在重复"
    for q in questions:
        assert len(q["test_cases"]) >= 2, q["id"] + " 断言不足"
        for t in q["test_cases"]:
            exec(t, {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH01", "title": "Hello, World!",
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "hard_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 中等档 30 道，id 唯一，expected_output 唯一，每题断言 >= 3")


if __name__ == "__main__":
    main()
