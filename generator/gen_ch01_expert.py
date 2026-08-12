# -*- coding: utf-8 -*-
"""生成 CH01 较难档（expert_30.json，id 后缀 X）30 道题。

第四轮清单规范：
  topic       = "print() 函数在复杂场景下的综合运用"
  difficulty  = "较难"，stars = "⭐⭐⭐⭐"
  10 种综合场景各 ≥2 次；实战场景 ≥8 类（列表/字典、图形、数据汇总、条件分支、
  自定义函数、异常处理、模拟真实数据、多步骤逻辑）；边缘情况（空容器 ≥6、边界值 ≥6、类型转换 ≥4）
  每题 test_cases 4 个 assert（精确匹配 + 换行数 + 去空白 + 首行匹配）
"""
import io
import json
import os
import sys

TOPIC = "print() 函数在复杂场景下的综合运用"
DIFFICULTY = "较难"
STARS = "⭐⭐⭐⭐"
SUFFIX = "X"


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
    first_line = captured.split("\n")[0]
    tests = [
        "assert captured_output == " + repr(captured),
        "assert captured_output.count(chr(10)) == %d" % captured.count("\n"),
    ]
    if captured.strip():
        tests.append("assert captured_output.strip() == " + repr(captured.strip()))
    if first_line:
        tests.append("assert captured_output.startswith(" + repr(first_line) + ")")
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


EXPERT = [
    # ---------- 场景 1：遍历列表并格式化输出 ----------
    (1, "给定学生姓名列表 students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']，"
        "遍历输出 '序号. 姓名'，序号从 1 开始，共 5 行。",
     "students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']\n"
     "# 请在此处编写代码：遍历列表并用 enumerate 输出带序号\n"
     "for ___ in enumerate(___, start=1):\n"
     "    print(f\"___. {name}\")",
     "用 enumerate(students, start=1) 同时取索引和姓名。",
     "# 遍历学生列表，输出带序号的姓名\n"
     "students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']\n"
     "for idx, name in enumerate(students, start=1):\n"
     "    print(f'{idx}. {name}')"),
    (2, "给定元组列表 data = [('Tom', 25), ('Ada', 36)]，遍历输出 '姓名 - 年龄' 两行。",
     "data = [('Tom', 25), ('Ada', 36)]\n"
     "# 请遍历元组列表并格式化输出\n"
     "for name, age in ___:\n"
     "    print(f\"{___} - {___}\")",
     "用 for name, age in data 解包元组。",
     "# 遍历元组列表，输出姓名与年龄\n"
     "data = [('Tom', 25), ('Ada', 36)]\n"
     "for name, age in data:\n"
     "    print(f'{name} - {age}')"),
    # ---------- 场景 2：遍历字典并格式化输出 ----------
    (3, "给定字典 scores = {'Alice': 90, 'Bob': 85, 'Cara': 88}，遍历输出 '姓名: 分数' 三行。",
     "scores = {'Alice': 90, 'Bob': 85, 'Cara': 88}\n"
     "# 请遍历字典的键值对\n"
     "for name, score in ___.items():\n"
     "    print(f\"{___}: {___}\")",
     "用 scores.items() 同时取键和值。",
     "# 遍历成绩字典，输出姓名与分数\n"
     "scores = {'Alice': 90, 'Bob': 85, 'Cara': 88}\n"
     "for name, score in scores.items():\n"
     "    print(f'{name}: {score}')"),
    (4, "给定字典 prices = {'apple': 3.5, 'milk': 5.0}，遍历输出 '商品 $价格' 两行，价格保留两位小数。",
     "prices = {'apple': 3.5, 'milk': 5.0}\n"
     "# 请遍历字典并格式化价格\n"
     "for item, price in ___.items():\n"
     "    print(f\"{___} ${___:.2f}\")",
     "用 items() 遍历，价格用 :.2f 保留两位小数。",
     "# 遍历价格字典，输出商品与价格\n"
     "prices = {'apple': 3.5, 'milk': 5.0}\n"
     "for item, price in prices.items():\n"
     "    print(f'{item} ${price:.2f}')"),
    # ---------- 场景 3：图形/图案输出 ----------
    (5, "用循环打印 5 行数字三角形（第 i 行有 i 个数字 i）。",
     "n = 5\n"
     "# 请用循环打印数字三角形\n"
     "for i in range(1, ___ + 1):\n"
     "    print(___ * i)",
     "把数字 i 转成字符串再乘以行号。",
     "# 打印数字三角形\n"
     "n = 5\n"
     "for i in range(1, n + 1):\n"
     "    print(str(i) * i)"),
    (6, "用循环打印 3 行宽的星号菱形（对称）。",
     "n = 3\n"
     "# 请打印上下对称的菱形：上半部分递增，下半部分递减\n"
     "for i in range(1, n + 1):\n"
     "    print(' ' * (n - i) + '*' * (2 * i - 1))\n"
     "for i in range(n - 1, 0, -1):\n"
     "    print(' ' * (n - i) + '*' * (2 * ___ - 1))",
     "下半部分用 range(n-1, 0, -1) 递减行号。",
     "# 打印星号菱形\n"
     "n = 3\n"
     "for i in range(1, n + 1):\n"
     "    print(' ' * (n - i) + '*' * (2 * i - 1))\n"
     "for i in range(n - 1, 0, -1):\n"
     "    print(' ' * (n - i) + '*' * (2 * i - 1))"),
    (7, "打印 1 到 9 的九九乘法表（每行到 i 列，结果右对齐宽度 2）。",
     "# 请打印九九乘法表\n"
     "for i in range(1, ___):\n"
     "    for j in range(1, i + 1):\n"
     "        print(f\"{j}x{i}={i * j:___}\", end='  ')\n"
     "    print()",
     "外层 1..9，内层 1..i，结果用 :2d 对齐。",
     "# 打印九九乘法表\n"
     "for i in range(1, 10):\n"
     "    for j in range(1, i + 1):\n"
     "        print(f'{j}x{i}={i * j:2d}', end='  ')\n"
     "    print()"),
    # ---------- 场景 4：数据汇总与格式化输出 ----------
    (8, "给定 nums = [88, 92, 76, 95, 84]，输出总和、平均值（1 位小数）、最大值、最小值四行。",
     "nums = [88, 92, 76, 95, 84]\n"
     "# 请计算并输出汇总统计\n"
     "total = sum(___)\n"
     "avg = total / len(___)\n"
     "print(f\"Sum: {___}\")\n"
     "print(f\"Average: {___:.1f}\")\n"
     "print(f\"Max: {max(nums)}\")\n"
     "print(f\"Min: {min(nums)}\")",
     "sum/len/max/min 四个内置函数。",
     "# 统计列表的总和、平均值、最大最小值\n"
     "nums = [88, 92, 76, 95, 84]\n"
     "total = sum(nums)\n"
     "avg = total / len(nums)\n"
     "print(f'Sum: {total}')\n"
     "print(f'Average: {avg:.1f}')\n"
     "print(f'Max: {max(nums)}')\n"
     "print(f'Min: {min(nums)}')"),
    (9, "给定空列表 nums = []，处理空列表并输出 'No data'，否则输出总和。",
     "nums = []\n"
     "# 请处理空列表边界情况\n"
     "if ___:\n"
     "    print(f\"Sum: {sum(nums)}\")\n"
     "else:\n"
     "    print(___)\n",
     "空列表为假值，用 if nums 判断。",
     "# 空列表边界处理\n"
     "nums = []\n"
     "if nums:\n"
     "    print(f'Sum: {sum(nums)}')\n"
     "else:\n"
     "    print('No data')"),
    # ---------- 场景 5：多条件判断与输出 ----------
    (10, "给定 score = 96，按 90/80/70/60 分档输出等级（A/B/C/D/F），考虑边界值。",
     "score = ___\n"
     "# 请用多条件分支输出成绩等级\n"
     "if score >= 90:\n"
     "    grade = 'A'\n"
     "elif score >= ___:\n"
     "    grade = 'B'\n"
     "elif score >= 70:\n"
     "    grade = 'C'\n"
     "elif score >= 60:\n"
     "    grade = 'D'\n"
     "else:\n"
     "    grade = 'F'\n"
     "print(f\"Grade: {___}\")",
     "按分数区间逐级判断，边界值用 >=。",
     "# 按分数输出成绩等级\n"
     "score = 96\n"
     "if score >= 90:\n"
     "    grade = 'A'\n"
     "elif score >= 80:\n"
     "    grade = 'B'\n"
     "elif score >= 70:\n"
     "    grade = 'C'\n"
     "elif score >= 60:\n"
     "    grade = 'D'\n"
     "else:\n"
     "    grade = 'F'\n"
     "print(f'Grade: {grade}')"),
    (11, "对 n 取 -1、0、1 三个边界值，输出正/负/零判断。",
     "# 请对边界值 -1、0、1 分类输出\n"
     "def classify(n):\n"
     "    if n < ___:\n"
     "        return 'negative'\n"
     "    elif n == 0:\n"
     "        return 'zero'\n"
     "    else:\n"
     "        return 'positive'\n"
     "for n in [___]:\n"
     "    print(n, classify(n))",
     "负数/零/正数三个分支，测试 -1、0、1。",
     "# 边界值分类\n"
     "def classify(n):\n"
     "    if n < 0:\n"
     "        return 'negative'\n"
     "    elif n == 0:\n"
     "        return 'zero'\n"
     "    else:\n"
     "        return 'positive'\n"
     "for n in [-1, 0, 1]:\n"
     "    print(n, classify(n))"),
    (12, "给定密码 'abc123'，按长度、字母/数字组合输出密码强度。",
     "password = 'abc123'\n"
     "# 请按规则判断密码强度并输出\n"
     "if len(password) < 6:\n"
     "    strength = 'Weak: too short'\n"
     "elif password.isalpha():\n"
     "    strength = 'Weak: no digits'\n"
     "elif password.isdigit():\n"
     "    strength = 'Medium: no letters'\n"
     "else:\n"
     "    strength = 'Strong'\n"
     "print(f\"{password}: {___}\")",
     "先判断长度边界，再判断是否含字母/数字。",
     "# 密码强度判断\n"
     "password = 'abc123'\n"
     "if len(password) < 6:\n"
     "    strength = 'Weak: too short'\n"
     "elif password.isalpha():\n"
     "    strength = 'Weak: no digits'\n"
     "elif password.isdigit():\n"
     "    strength = 'Medium: no letters'\n"
     "else:\n"
     "    strength = 'Strong'\n"
     "print(f'{password}: {strength}')"),
    # ---------- 场景 6：异常处理与输出 ----------
    (13, "给定 data = ['10', 'abc', '20']，逐个转 int 输出两倍值，转换失败输出 'Invalid: 原值'。",
     "data = ['10', 'abc', '20']\n"
     "# 请用 try-except 处理类型转换异常\n"
     "for s in ___:\n"
     "    try:\n"
     "        print(int(___ ) * 2)\n"
     "    except ValueError:\n"
     "        print(f\"Invalid: {___}\")",
     "int(s) 可能抛 ValueError，用 except 捕获。",
     "# 异常处理：类型转换失败时提示\n"
     "data = ['10', 'abc', '20']\n"
     "for s in data:\n"
     "    try:\n"
     "        print(int(s) * 2)\n"
     "    except ValueError:\n"
     "        print(f'Invalid: {s}')"),
    (14, "定义 safe_divide(a, b)，除数为 0 时返回错误提示，测试 (10,2)、(10,0)、(7,3)。",
     "# 请实现安全的除法并输出三组结果\n"
     "def safe_divide(a, b):\n"
     "    if b == 0:\n"
     "        return 'Error: division by zero'\n"
     "    return ___ / b\n"
     "for pair in [(10, 2), (10, 0), (7, 3)]:\n"
     "    print(f\"{pair[0]} / {pair[1]} = {safe_divide(pair[0], pair[1])}\")",
     "先判断除零边界，再执行除法。",
     "# 安全的除法（处理除零）\n"
     "def safe_divide(a, b):\n"
     "    if b == 0:\n"
     "        return 'Error: division by zero'\n"
     "    return a / b\n"
     "for pair in [(10, 2), (10, 0), (7, 3)]:\n"
     "    print(f'{pair[0]} / {pair[1]} = {safe_divide(pair[0], pair[1])}')"),
    (15, "给定 mixed = [1, '2', 3.5, '4', 'x']，累加可转 float 的值，失败时输出 'Skipped: 原值'。",
     "mixed = [1, '2', 3.5, '4', 'x']\n"
     "total = 0.0\n"
     "# 请用 try-except 跳过无法转换的值\n"
     "for m in ___:\n"
     "    try:\n"
     "        total += float(___)\n"
     "    except ValueError:\n"
     "        print(f\"Skipped: {___}\")\n"
     "print(f\"Total: {total}\")",
     "float() 转换失败抛 ValueError。",
     "# 类型转换 + 异常处理\n"
     "mixed = [1, '2', 3.5, '4', 'x']\n"
     "total = 0.0\n"
     "for m in mixed:\n"
     "    try:\n"
     "        total += float(m)\n"
     "    except ValueError:\n"
     "        print(f'Skipped: {m}')\n"
     "print(f'Total: {total}')"),
    # ---------- 场景 7：文件读取与输出（模拟） ----------
    (16, "给定配置行 lines = ['# config', 'name=PyQuest', 'version=1.0', '']，过滤注释和空行后输出有效行。",
     "lines = ['# config', 'name=PyQuest', 'version=1.0', '']\n"
     "# 请过滤以 # 开头的注释行和空行\n"
     "for line in ___:\n"
     "    if line and not line.___('#'):\n"
     "        print(line)",
     "空字符串为假值，用 startswith('#') 判断注释。",
     "# 模拟读取配置文件并过滤注释\n"
     "lines = ['# config', 'name=PyQuest', 'version=1.0', '']\n"
     "for line in lines:\n"
     "    if line and not line.startswith('#'):\n"
     "        print(line)"),
    (17, "给定日志 logs 列表，包含 INFO/ERROR/DEBUG，只输出含 ERROR 或 INFO 的行。",
     "logs = ['INFO: start', 'ERROR: crash', 'INFO: done', 'DEBUG: x=1']\n"
     "# 请过滤日志，ERROR 加 [ALERT] 前缀\n"
     "for log in ___:\n"
     "    if 'ERROR' in log:\n"
     "        print(f\"[ALERT] {___}\")\n"
     "    elif 'INFO' in log:\n"
     "        print(___)\n",
     "用 in 判断日志级别关键字。",
     "# 日志过滤器\n"
     "logs = ['INFO: start', 'ERROR: crash', 'INFO: done', 'DEBUG: x=1']\n"
     "for log in logs:\n"
     "    if 'ERROR' in log:\n"
     "        print(f'[ALERT] {log}')\n"
     "    elif 'INFO' in log:\n"
     "        print(log)"),
    # ---------- 场景 8：用户输入与输出（模拟） ----------
    (18, "模拟输入姓名 'Tom' 和年龄 17，处理空姓名边界，非空时输出问候并按年龄输出 Adult 或 Minor。",
     "name = 'Tom'  # 模拟 input()\n"
     "age = 17       # 模拟 input() 转 int\n"
     "# 请处理空姓名边界并输出问候与年龄判断\n"
     "if not ___:\n"
     "    print('Empty name')\n"
     "else:\n"
     "    print(f\"Hello {___}!\")\n"
     "    if age >= 18:\n"
     "        print('Adult')\n"
     "    else:\n"
     "        print('Minor')",
     "空字符串为假值；年龄边界 18 用 >= 判断。",
     "# 模拟用户输入（含空值边界）\n"
     "name = 'Tom'  # 模拟 input()\n"
     "age = 17       # 模拟 input() 转 int\n"
     "if not name:\n"
     "    print('Empty name')\n"
     "else:\n"
     "    print(f'Hello {name}!')\n"
     "    if age >= 18:\n"
     "        print('Adult')\n"
     "    else:\n"
     "        print('Minor')"),
    (19, "模拟猜数字：secret = 7，猜测序列 [3, 5, 7]，每次输出高低或正确提示。",
     "secret = 7\n"
     "guesses = [3, 5, 7]\n"
     "# 请逐次比较猜测并提示\n"
     "for i, guess in enumerate(___, start=1):\n"
     "    if guess < ___:\n"
     "        print(f\"Guess {i}: too low\")\n"
     "    elif guess > secret:\n"
     "        print(f\"Guess {i}: too high\")\n"
     "    else:\n"
     "        print(f\"Guess {i}: correct!\")\n"
     "        break",
     "enumerate 带序号，猜中后 break。",
     "# 猜数字游戏（模拟输入）\n"
     "secret = 7\n"
     "guesses = [3, 5, 7]\n"
     "for i, guess in enumerate(guesses, start=1):\n"
     "    if guess < secret:\n"
     "        print(f'Guess {i}: too low')\n"
     "    elif guess > secret:\n"
     "        print(f'Guess {i}: too high')\n"
     "    else:\n"
     "        print(f'Guess {i}: correct!')\n"
     "        break"),
    # ---------- 场景 9：列表推导式与输出 ----------
    (20, "给定 nums = [1..6]，用列表推导式筛选偶数并求平方，输出结果列表。",
     "nums = [1, 2, 3, 4, 5, 6]\n"
     "# 请用列表推导式筛选偶数并平方\n"
     "squares = [n * n for n in ___ if ___ % 2 == 0]\n"
     "print(___)",
     "推导式格式：[表达式 for n in 列表 if 条件]。",
     "# 列表推导式：偶数平方\n"
     "nums = [1, 2, 3, 4, 5, 6]\n"
     "squares = [n * n for n in nums if n % 2 == 0]\n"
     "print(squares)"),
    (21, "给定字符串 '1,2,3,4,5'，split 后转 int 列表，输出总和与 '-' 连接的结果。",
     "s = '1,2,3,4,5'\n"
     "# 请拆分、类型转换并汇总\n"
     "nums = [int(x) for x in s.___(',')]\n"
     "print(f\"Sum: {sum(___ )}\")\n"
     "print(f\"Joined: {'-'.join(map(str, nums))}\")",
     "split(',') 后 int() 转换，join 前要 map(str)。",
     "# 字符串拆分、类型转换与汇总\n"
     "s = '1,2,3,4,5'\n"
     "nums = [int(x) for x in s.split(',')]\n"
     "print(f'Sum: {sum(nums)}')\n"
     "print(f'Joined: {\"-\".join(map(str, nums))}')"),
    # ---------- 场景 10：自定义函数封装 ----------
    (22, "定义 format_student(name, score) 返回 '姓名: 分数'，处理空列表边界，对两名学生调用并输出。",
     "# 请定义格式化函数，处理空列表并调用\n"
     "def format_student(name, score):\n"
     "    return f\"{___}: {___}\"\n"
     "students = [('Alice', 90), ('Bob', 85)]\n"
     "if not ___:\n"
     "    print('No students')\n"
     "else:\n"
     "    for name, score in students:\n"
     "        print(format_student(name, score))",
     "空列表先判断；函数返回格式化字符串，循环调用。",
     "# 自定义函数封装输出逻辑（含空列表边界）\n"
     "def format_student(name, score):\n"
     "    return f'{name}: {score}'\n"
     "students = [('Alice', 90), ('Bob', 85)]\n"
     "if not students:\n"
     "    print('No students')\n"
     "else:\n"
     "    for name, score in students:\n"
     "        print(format_student(name, score))"),
    (23, "定义 process_numbers(nums) 返回偶数个数与偶数和，对 1..8 调用并输出。",
     "# 请定义统计函数并调用\n"
     "def process_numbers(nums):\n"
     "    evens = [n for n in ___ if n % 2 == 0]\n"
     "    return len(___), sum(evens)\n"
     "nums = [1, 2, 3, 4, 5, 6, 7, 8]\n"
     "count, total = process_numbers(___)\n"
     "print(f\"Even count: {___}, Even sum: {___}\")",
     "函数返回元组，调用时解包。",
     "# 自定义函数：统计偶数\n"
     "def process_numbers(nums):\n"
     "    evens = [n for n in nums if n % 2 == 0]\n"
     "    return len(evens), sum(evens)\n"
     "nums = [1, 2, 3, 4, 5, 6, 7, 8]\n"
     "count, total = process_numbers(nums)\n"
     "print(f'Even count: {count}, Even sum: {total}')"),
    (24, "定义 fib(n) 生成斐波那契前 n 项，调用 fib(10) 输出列表。",
     "# 请定义斐波那契函数\n"
     "def fib(n):\n"
     "    seq = [0, 1]\n"
     "    while len(seq) < ___:\n"
     "        seq.append(seq[___] + seq[-2])\n"
     "    return seq[:n]\n"
     "print(fib(___))",
     "递推 seq[-1] + seq[-2]，切片取前 n 项。",
     "# 自定义函数：斐波那契序列\n"
     "def fib(n):\n"
     "    seq = [0, 1]\n"
     "    while len(seq) < n:\n"
     "        seq.append(seq[-1] + seq[-2])\n"
     "    return seq[:n]\n"
     "print(fib(10))"),
    # ---------- 补充实战：排行榜 / 成绩单 / 购物车 / 文本统计 ----------
    (25, "给定成绩字典，按分数降序输出排行榜 '名次. 姓名 - 分数'，空字典输出 'No data'。",
     "scores = {'Alice': 90, 'Bob': 85, 'Cara': 95, 'Dan': 88}\n"
     "# 请按分数降序输出排行榜\n"
     "if not ___:\n"
     "    print('No data')\n"
     "else:\n"
     "    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=___)\n"
     "    for i, (name, score) in enumerate(ranking, ___):\n"
     "        print(f\"{i}. {name} - {score}\")",
     "sorted 按分数降序，enumerate 加名次，空字典先判断。",
     "# 成绩排行榜（降序 + 空处理）\n"
     "scores = {'Alice': 90, 'Bob': 85, 'Cara': 95, 'Dan': 88}\n"
     "if not scores:\n"
     "    print('No data')\n"
     "else:\n"
     "    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)\n"
     "    for i, (name, score) in enumerate(ranking, 1):\n"
     "        print(f'{i}. {name} - {score}')"),
    (26, "给定商品列表 [(名称, 单价)]，输出对齐清单与总价，空列表输出 'Empty cart'。",
     "products = [('apple', 3.5), ('milk', 5.0), ('bread', 4.5)]\n"
     "# 请输出商品清单与总价\n"
     "if not ___:\n"
     "    print('Empty cart')\n"
     "else:\n"
     "    print(f\"{'Item':<8}{'Price':>8}\")\n"
     "    total = 0\n"
     "    for name, price in products:\n"
     "        print(f\"{name:<8}{price:>8.2f}\")\n"
     "        total += ___\n"
     "    print(f\"Total: {___:.2f}\")",
     "空列表先判断；对齐用 <8 和 >8.2f。",
     "# 商品清单（对齐 + 空处理）\n"
     "products = [('apple', 3.5), ('milk', 5.0), ('bread', 4.5)]\n"
     "if not products:\n"
     "    print('Empty cart')\n"
     "else:\n"
     "    print(f\"{'Item':<8}{'Price':>8}\")\n"
     "    total = 0\n"
     "    for name, price in products:\n"
     "        print(f'{name:<8}{price:>8.2f}')\n"
     "        total += price\n"
     "    print(f'Total: {total:.2f}')"),
    (27, "给定成绩列表，统计 A/B/C/D/F 各档人数并输出 '等级: 柱条 (人数)'，空列表输出 'No scores'。",
     "scores = [55, 72, 88, 91, 63, 77, 85, 95, 68, 80]\n"
     "# 请统计各等级人数并绘制柱条\n"
     "if not ___:\n"
     "    print('No scores')\n"
     "else:\n"
     "    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}\n"
     "    for s in scores:\n"
     "        if s >= 90:\n"
     "            grades['A'] += 1\n"
     "        elif s >= 80:\n"
     "            grades['B'] += 1\n"
     "        elif s >= 70:\n"
     "            grades['C'] += 1\n"
     "        elif s >= 60:\n"
     "            grades['D'] += 1\n"
     "        else:\n"
     "            grades['F'] += 1\n"
     "    for grade, count in grades.items():\n"
     "        print(f\"{grade}: {'#' * count} ({count})\")",
     "多条件分档计数，用 '#' * count 画柱条。",
     "# 成绩等级分布（多条件 + 空处理）\n"
     "scores = [55, 72, 88, 91, 63, 77, 85, 95, 68, 80]\n"
     "if not scores:\n"
     "    print('No scores')\n"
     "else:\n"
     "    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}\n"
     "    for s in scores:\n"
     "        if s >= 90:\n"
     "            grades['A'] += 1\n"
     "        elif s >= 80:\n"
     "            grades['B'] += 1\n"
     "        elif s >= 70:\n"
     "            grades['C'] += 1\n"
     "        elif s >= 60:\n"
     "            grades['D'] += 1\n"
     "        else:\n"
     "            grades['F'] += 1\n"
     "    for grade, count in grades.items():\n"
     "        print(f'{grade}: {\"#\" * count} ({count})')"),
    (28, "给定文本，统计单词数、字符数、唯一单词数并输出三行报告。",
     "text = 'the quick brown fox jumps over the lazy dog'\n"
     "# 请统计并输出文本报告\n"
     "words = text.___()\n"
     "print(f\"Words: {len(words)}\")\n"
     "print(f\"Characters: {len(text)}\")\n"
     "print(f\"Unique words: {len(set(words))}\")",
     "split() 分词，set 去重求唯一单词数。",
     "# 文本统计报告\n"
     "text = 'the quick brown fox jumps over the lazy dog'\n"
     "words = text.split()\n"
     "print(f'Words: {len(words)}')\n"
     "print(f'Characters: {len(text)}')\n"
     "print(f'Unique words: {len(set(words))}')"),
    (29, "给定购物车 [(商品, 单价, 数量)]，输出小计与总计，总价超 20 输出 'Free shipping!'。",
     "cart = [('apple', 3.5, 2), ('milk', 5.0, 1), ('bread', 4.5, 3)]\n"
     "# 请计算购物车小计与总计\n"
     "total = 0\n"
     "print(f\"{'Item':<10}{'Qty':>4}{'Subtotal':>10}\")\n"
     "for name, price, qty in ___:\n"
     "    subtotal = price * qty\n"
     "    total += ___\n"
     "    print(f\"{name:<10}{qty:>4}{subtotal:>10.2f}\")\n"
     "print(f\"Grand total: {___:.2f}\")\n"
     "if total > 20:\n"
     "    print('Free shipping!')\n"
     "else:\n"
     "    print('Shipping: $5')",
     "元组解包 (name, price, qty)，累计小计。",
     "# 购物车结算（含运费判断）\n"
     "cart = [('apple', 3.5, 2), ('milk', 5.0, 1), ('bread', 4.5, 3)]\n"
     "total = 0\n"
     "print(f\"{'Item':<10}{'Qty':>4}{'Subtotal':>10}\")\n"
     "for name, price, qty in cart:\n"
     "    subtotal = price * qty\n"
     "    total += subtotal\n"
     "    print(f'{name:<10}{qty:>4}{subtotal:>10.2f}')\n"
     "print(f'Grand total: {total:.2f}')\n"
     "if total > 20:\n"
     "    print('Free shipping!')\n"
     "else:\n"
     "    print('Shipping: $5')"),
    (30, "定义 print_bar(value, max_value) 返回条形图，对字典 {'A':8,'B':5,'C':3} 输出每项的条形与数值。",
     "# 请定义条形图函数并输出\n"
     "def print_bar(value, max_value, width=10):\n"
     "    filled = int(value / max_value * width)\n"
     "    return '#' * filled + '.' * (width - filled)\n"
     "data = {'A': 8, 'B': 5, 'C': 3}\n"
     "max_v = max(data.___())\n"
     "for key, value in data.items():\n"
     "    print(f\"{key}: {print_bar(value, max_v)} ({___})\")",
     "按占比填充 '#' 与 '.'，max() 取最大值。",
     "# 横向条形图（自定义函数 + 字典遍历）\n"
     "def print_bar(value, max_value, width=10):\n"
     "    filled = int(value / max_value * width)\n"
     "    return '#' * filled + '.' * (width - filled)\n"
     "data = {'A': 8, 'B': 5, 'C': 3}\n"
     "max_v = max(data.values())\n"
     "for key, value in data.items():\n"
     "    print(f'{key}: {print_bar(value, max_v)} ({value})')"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH01_Hello_World")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in EXPERT]
    assert len(questions) == 30, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH01-X-%03d" % i for i in range(1, 31)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 30, "expected_output 存在重复"
    for q in questions:
        assert len(q["test_cases"]) >= 3, q["id"] + " 断言不足"
        for t in q["test_cases"]:
            exec(t, {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH01", "title": "Hello, World!",
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "expert_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 较难档 30 道，id 唯一，expected_output 唯一，每题断言 >= 3")


if __name__ == "__main__":
    main()
