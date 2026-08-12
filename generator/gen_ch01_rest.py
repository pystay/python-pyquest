# -*- coding: utf-8 -*-
"""生成 CH01 简单 / 较难 两档各 30 道题（中等档由 gen_ch01_hard.py 生成）。

难度与 id 映射（递进命名）：
  超简单 ⭐     -> easy_30.json     (id 后缀 E，gen_ch01_easy.py 生成)
  简单   ⭐⭐   -> medium_30.json   (id 后缀 M，本脚本生成，第二轮清单版)
  中等   ⭐⭐⭐ -> hard_30.json     (id 后缀 H，gen_ch01_hard.py 生成)
  较难   ⭐⭐⭐⭐ -> expert_30.json   (id 后缀 X，本脚本生成)

关键机制：expected_output 与 test_cases 由脚本模拟运行 solution 自动生成。
"""
import io
import json
import os
import sys

META = {
    "M": ("简单", "⭐⭐", "print() 函数与变量的结合使用"),
    "X": ("较难", "⭐⭐⭐⭐", "print() 函数的基本使用"),
}


def run(code):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        exec(code, {})
    finally:
        sys.stdout = old
    return buf.getvalue()


def make_q(suffix, num, desc, template, hints, solution):
    diff, stars, topic = META[suffix]
    captured = run(solution)
    tests = ["assert captured_output == " + repr(captured)]
    exec(tests[0], {"captured_output": captured})
    return {
        "id": "CH01-%s-%03d" % (suffix, num),
        "topic": topic,
        "difficulty": diff,
        "stars": stars,
        "description": desc,
        "code_template": template,
        "expected_output": captured,
        "hints": hints,
        "test_cases": tests,
        "solution": solution,
    }


# ---------- 简单档（⭐⭐，变量定义 + print 填空，≤8 行，≤3 变量） ----------
# 覆盖第二轮清单指定的 12 种用法：字符串变量 / 整数变量 / 浮点变量 / 布尔变量 /
# 字符串拼接(+) / f-string / format() / 逗号分隔 / 算术运算 / 比较运算 /
# 一行多变量 / 变量重新赋值
SIMPLE = [
    (1, "定义字符串变量 name 为 'Bob' 并用 print() 输出。",
     "name = \"Bob\"\nprint(___)",
     "print 括号内填变量名 name。",
     "name = \"Bob\"\nprint(name)"),
    (2, "定义整数变量 score 为 92 并输出。",
     "score = 92\nprint(___)",
     "print 括号内填变量名 score。",
     "score = 92\nprint(score)"),
    (3, "定义浮点数变量 price 为 19.99 并输出。",
     "price = 19.99\nprint(___)",
     "print 括号内填变量名 price。",
     "price = 19.99\nprint(price)"),
    (4, "定义布尔变量 is_student 并随文字一起输出。",
     "is_student = True\nprint(\"Is student:\", ___)",
     "逗号后填变量名 is_student。",
     "is_student = True\nprint(\"Is student:\", is_student)"),
    (5, "用 + 拼接两个字符串变量后输出。",
     "first = \"Alice\"\nlast = \"Smith\"\nprint(___ + \" \" + ___)",
     "用 + 连接 first、空格和 last。",
     "first = \"Alice\"\nlast = \"Smith\"\nprint(first + \" \" + last)"),
    (6, "用 f-string 输出姓名和年龄。",
     "name = \"Alice\"\nage = 25\nprint(f\"{___} is {___} years old\")",
     "花括号内依次填 name、age。",
     "name = \"Alice\"\nage = 25\nprint(f\"{name} is {age} years old\")"),
    (7, "用 format() 输出两个数相加的等式。",
     "a = 3\nb = 7\nprint(\"{} + {} = {}\".format(___, ___, ___))",
     "依次填 a、b、a + b。",
     "a = 3\nb = 7\nprint(\"{} + {} = {}\".format(a, b, a + b))"),
    (8, "用逗号分隔同时输出姓名和分数。",
     "name = \"Tom\"\nscore = 88\nprint(___, ___)",
     "依次填 name、score。",
     "name = \"Tom\"\nscore = 88\nprint(name, score)"),
    (9, "变量参与算术运算后输出三个结果。",
     "x = 7\ny = 2\nprint(___, ___, ___)",
     "依次填 x + y、x - y、x * y。",
     "x = 7\ny = 2\nprint(x + y, x - y, x * y)"),
    (10, "变量参与比较运算后输出布尔结果。",
     "a = 10\nb = 5\nprint(___, ___)",
     "依次填 a > b、a == b。",
     "a = 10\nb = 5\nprint(a > b, a == b)"),
    (11, "定义三个变量并在一行 print() 中全部输出。",
     "x = 1\ny = 2\nz = 3\nprint(___, ___, ___)",
     "依次填 x、y、z。",
     "x = 1\ny = 2\nz = 3\nprint(x, y, z)"),
    (12, "变量重新赋值后再输出新值。",
     "x = 3\nx = ___ * 3\nprint(___)",
     "先填 x 再填 x，观察重新赋值。",
     "x = 3\nx = x * 3\nprint(x)"),
    (13, "用 + 拼接字符串与 str() 转换的数字。",
     "name = \"Alice\"\nage = 25\nprint(\"Name: \" + ___ + \", Age: \" + str(___))",
     "依次填 name、age。",
     "name = \"Alice\"\nage = 25\nprint(\"Name: \" + name + \", Age: \" + str(age))"),
    (14, "用 f-string 把浮点数保留两位小数输出。",
     "price = 19.99\nprint(f\"Price: {___:.2f}\")",
     "花括号内填 price。",
     "price = 19.99\nprint(f\"Price: {price:.2f}\")"),
    (15, "输出变量除法的商、整除和余数。",
     "a = 9\nb = 2\nprint(___ / b, ___ // b, ___ % b)",
     "三处都填变量 a。",
     "a = 9\nb = 2\nprint(a / b, a // b, a % b)"),
    (16, "定义布尔变量 is_ready 并随文字输出。",
     "is_ready = True\nprint(\"Ready:\", ___)",
     "逗号后填变量名 is_ready。",
     "is_ready = True\nprint(\"Ready:\", is_ready)"),
    (17, "变量参与幂运算后输出结果。",
     "base = 3\nexp = 4\nprint(___ ** ___)",
     "依次填 base、exp。",
     "base = 3\nexp = 4\nprint(base ** exp)"),
    (18, "字符串变量拼接后重新赋值并输出。",
     "msg = \"Good\"\nmsg = ___ + \" job\"\nprint(___)",
     "先填 msg 再填 msg。",
     "msg = \"Good\"\nmsg = msg + \" job\"\nprint(msg)"),
    (19, "用 format() 关键字参数输出姓名和年龄。",
     "name = \"Bob\"\nage = 30\nprint(\"{n} is {a} years old\".format(n=___, a=___))",
     "依次填 name、age。",
     "name = \"Bob\"\nage = 30\nprint(\"{n} is {a} years old\".format(n=name, a=age))"),
    (20, "交换两个变量的值后输出。",
     "a = 1\nb = 2\n___, ___ = b, a\nprint(a, b)",
     "用 a, b = b, a 交换。",
     "a = 1\nb = 2\na, b = b, a\nprint(a, b)"),
    (21, "用变量与数字相乘重复字符串并输出。",
     "symbol = \"*\"\nn = 5\nprint(___ * ___)",
     "依次填 symbol、n。",
     "symbol = \"*\"\nn = 5\nprint(symbol * n)"),
    (22, "两个浮点数变量相乘并输出面积。",
     "width = 2.5\nheight = 4.0\nprint(___ * ___)",
     "依次填 width、height。",
     "width = 2.5\nheight = 4.0\nprint(width * height)"),
    (23, "一个变量参与多个比较并输出结果。",
     "a = 5\nprint(___ > 3, a < 10, ___ == 5)",
     "两处都填变量 a。",
     "a = 5\nprint(a > 3, a < 10, a == 5)"),
    (24, "定义负数变量并输出。",
     "temp = -5\nprint(___)",
     "print 括号内填变量名 temp。",
     "temp = -5\nprint(temp)"),
    (25, "输出字符串变量和浮点数变量。",
     "product = \"Python\"\nversion = 3.12\nprint(___, ___)",
     "依次填 product、version。",
     "product = \"Python\"\nversion = 3.12\nprint(product, version)"),
    (26, "一行输出字符串、整数、浮点数三个变量。",
     "name = \"Ada\"\nage = 36\nheight = 1.7\nprint(___, ___, ___)",
     "依次填 name、age、height。",
     "name = \"Ada\"\nage = 36\nheight = 1.7\nprint(name, age, height)"),
    (27, "用 f-string 在花括号内写表达式并输出。",
     "x = 5\nprint(f\"{___} squared is {___ * x}\")",
     "依次填 x、x。",
     "x = 5\nprint(f\"{x} squared is {x * x}\")"),
    (28, "输出变量整除的商和余数。",
     "total = 17\nn = 5\nprint(___ // n, ___ % n)",
     "两处都填变量 total。",
     "total = 17\nn = 5\nprint(total // n, total % n)"),
    (29, "拼接两个字符串变量并加逗号输出。",
     "city = \"Beijing\"\ncountry = \"China\"\nprint(___ + \", \" + ___)",
     "依次填 city、country。",
     "city = \"Beijing\"\ncountry = \"China\"\nprint(city + \", \" + country)"),
    (30, "变量累加后输出最终结果。",
     "count = 0\ncount += 10\ncount += 5\nprint(___)",
     "print 括号内填变量名 count。",
     "count = 0\ncount += 10\ncount += 5\nprint(count)"),
]

# ---------- 较难档（⭐⭐⭐⭐，3+ 知识点，边缘情况与算法思维） ----------
HARD = [
    (1, "打印完整的九九乘法表。",
     "for i in range(___):\n    for j in range(1, i + 1):\n        print(f\"{j}x{i}={i * j:2d}\", end=\"  \")\n    print()",
     "外层 range 填 (1, 10)。",
     "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print(f\"{j}x{i}={i * j:2d}\", end=\"  \")\n    print()"),
    (2, "打印由星号组成的菱形。",
     "n = ___\nfor i in range(1, n + 1):\n    print(\" \" * (n - i) + \"*\" * (2 * i - 1))\nfor i in range(n - 1, 0, -1):\n    print(\" \" * (n - i) + \"*\" * (2 * i - 1))",
     "半宽 n 填 3，上下对称。",
     "n = 3\nfor i in range(1, n + 1):\n    print(\" \" * (n - i) + \"*\" * (2 * i - 1))\nfor i in range(n - 1, 0, -1):\n    print(\" \" * (n - i) + \"*\" * (2 * i - 1))"),
    (3, "打印杨辉三角前 5 行。",
     "rows = 5\ntriangle = []\nfor i in range(rows):\n    row = [1] * (i + 1)\n    for j in range(1, i):\n        row[j] = triangle[i - 1][j - 1] + ___\n    triangle.append(row)\nfor row in triangle:\n    print(\" \".join(map(str, row)))",
     "左上与正上方相加：triangle[i - 1][j]。",
     "rows = 5\ntriangle = []\nfor i in range(rows):\n    row = [1] * (i + 1)\n    for j in range(1, i):\n        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]\n    triangle.append(row)\nfor row in triangle:\n    print(\" \".join(map(str, row)))"),
    (4, "输出 2 到 50 之间的所有素数。",
     "for n in range(2, 51):\n    is_prime = True\n    for d in range(2, ___):\n        if n % d == 0:\n            is_prime = False\n            break\n    if is_prime:\n        print(n, end=\" \")",
     "只需试除到 sqrt(n)，填 int(n ** 0.5) + 1。",
     "for n in range(2, 51):\n    is_prime = True\n    for d in range(2, int(n ** 0.5) + 1):\n        if n % d == 0:\n            is_prime = False\n            break\n    if is_prime:\n        print(n, end=\" \")"),
    (5, "输出斐波那契数列前 10 项。",
     "a, b = 0, 1\ncount = 0\nwhile count < ___:\n    print(a, end=\" \")\n    a, b = b, a + b\n    count += 1",
     "输出项数填 10。",
     "a, b = 0, 1\ncount = 0\nwhile count < 10:\n    print(a, end=\" \")\n    a, b = b, a + b\n    count += 1"),
    (6, "打印居中的数字金字塔。",
     "n = 5\nfor i in range(1, n + 1):\n    print(\" \" * (___), end=\"\")\n    for j in range(1, i + 1):\n        print(j, end=\" \")\n    print()",
     "左侧空格数填 n - i。",
     "n = 5\nfor i in range(1, n + 1):\n    print(\" \" * (n - i), end=\"\")\n    for j in range(1, i + 1):\n        print(j, end=\" \")\n    print()"),
    (7, "演示冒泡排序每轮结果。",
     "nums = [5, 3, 8, 1]\nprint(\"Before:\", nums)\nfor i in range(len(nums) - 1):\n    for j in range(len(nums) - 1 - i):\n        if nums[j] > ___:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\n    print(\"Step\", i + 1, \":\", nums)\nprint(\"After:\", nums)",
     "与后一个元素比较：nums[j + 1]。",
     "nums = [5, 3, 8, 1]\nprint(\"Before:\", nums)\nfor i in range(len(nums) - 1):\n    for j in range(len(nums) - 1 - i):\n        if nums[j] > nums[j + 1]:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\n    print(\"Step\", i + 1, \":\", nums)\nprint(\"After:\", nums)"),
    (8, "输出所有三位水仙花数。",
     "for n in range(100, 1000):\n    a = n // 100\n    b = (n // 10) % 10\n    c = n % 10\n    if a ** 3 + b ** 3 + c ** 3 == ___:\n        print(n)",
     "立方和等于原数 n。",
     "for n in range(100, 1000):\n    a = n // 100\n    b = (n // 10) % 10\n    c = n % 10\n    if a ** 3 + b ** 3 + c ** 3 == n:\n        print(n)"),
    (9, "打印 5x5 空心正方形。",
     "n = 5\nfor i in range(n):\n    if i == 0 or i == n - 1:\n        print(\"*\" * n)\n    else:\n        print(\"*\" + \" \" * (n - 2) + ___)",
     "中间行末尾补 \"*\"。",
     "n = 5\nfor i in range(n):\n    if i == 0 or i == n - 1:\n        print(\"*\" * n)\n    else:\n        print(\"*\" + \" \" * (n - 2) + \"*\")"),
    (10, "判断字符串是否为回文。",
     "word = \"radar\"\nif word == ___:\n    print(word, \"is a palindrome\")\nelse:\n    print(word, \"is not a palindrome\")",
     "反转后比较：word[::-1]。",
     "word = \"radar\"\nif word == word[::-1]:\n    print(word, \"is a palindrome\")\nelse:\n    print(word, \"is not a palindrome\")"),
    (11, "统计字符串中字母和数字个数。",
     "text = \"PyQuest 2026!\"\nletters = 0\ndigits = 0\nfor ch in text:\n    if ___:\n        letters += 1\n    elif ch.isdigit():\n        digits += 1\nprint(\"Letters:\", letters, \"Digits:\", digits)",
     "字母判断用 ch.isalpha()。",
     "text = \"PyQuest 2026!\"\nletters = 0\ndigits = 0\nfor ch in text:\n    if ch.isalpha():\n        letters += 1\n    elif ch.isdigit():\n        digits += 1\nprint(\"Letters:\", letters, \"Digits:\", digits)"),
    (12, "输出数字的二进制、八进制、十六进制。",
     "n = 42\nprint(\"bin:\", ___)\nprint(\"oct:\", oct(n))\nprint(\"hex:\", hex(n))",
     "二进制用 bin(n)。",
     "n = 42\nprint(\"bin:\", bin(n))\nprint(\"oct:\", oct(n))\nprint(\"hex:\", hex(n))"),
    (13, "用辗转相除法求最大公约数。",
     "def gcd(a, b):\n    while ___:\n        a, b = b, a % b\n    return a\n\nprint(\"gcd(48, 36) =\", gcd(48, 36))",
     "while 条件填 b（余数非零继续）。",
     "def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\nprint(\"gcd(48, 36) =\", gcd(48, 36))"),
    (14, "输出 1000 以内的完数。",
     "for n in range(2, 1001):\n    total = 0\n    for d in range(1, n):\n        if n % d == 0:\n            total += d\n    if total == ___:\n        print(n)",
     "真因子和等于 n 即为完数。",
     "for n in range(2, 1001):\n    total = 0\n    for d in range(1, n):\n        if n % d == 0:\n            total += d\n    if total == n:\n        print(n)"),
    (15, "用函数输出 1 到 10 的阶乘表。",
     "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= ___\n    return result\n\nfor i in range(1, 11):\n    print(f\"{i}! = {factorial(i)}\")",
     "累乘循环变量 i。",
     "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n\nfor i in range(1, 11):\n    print(f\"{i}! = {factorial(i)}\")"),
    (16, "打印 5 行的空心等腰三角形。",
     "n = 5\nfor i in range(1, n + 1):\n    if i == n:\n        print(\" \" * (n - i) + \"*\" * (2 * i - 1))\n    elif i == 1:\n        print(\" \" * (n - i) + \"*\")\n    else:\n        print(\" \" * (n - i) + \"*\" + \" \" * (2 * i - 3) + ___)",
     "中间行末尾补 \"*\"。",
     "n = 5\nfor i in range(1, n + 1):\n    if i == n:\n        print(\" \" * (n - i) + \"*\" * (2 * i - 1))\n    elif i == 1:\n        print(\" \" * (n - i) + \"*\")\n    else:\n        print(\" \" * (n - i) + \"*\" + \" \" * (2 * i - 3) + \"*\")"),
    (17, "输出摄氏到华氏的温度转换表。",
     "print(\"C     F\")\nc = 0\nwhile c <= 100:\n    f = c * 9 / 5 + ___\n    print(f\"{c:3d}  {f:6.1f}\")\n    c += 20",
     "华氏偏移量填 32。",
     "print(\"C     F\")\nc = 0\nwhile c <= 100:\n    f = c * 9 / 5 + 32\n    print(f\"{c:3d}  {f:6.1f}\")\n    c += 20"),
    (18, "去除列表中的重复元素。",
     "nums = [3, 1, 2, 3, 4, 1, 5]\nseen = []\nfor n in nums:\n    if n not in ___:\n        seen.append(n)\nprint(seen)",
     "判断是否已在 seen 中。",
     "nums = [3, 1, 2, 3, 4, 1, 5]\nseen = []\nfor n in nums:\n    if n not in seen:\n        seen.append(n)\nprint(seen)"),
    (19, "用递归计算阶乘并输出。",
     "def fact(n):\n    if n <= 1:\n        return 1\n    return ___ * fact(n - 1)\n\nfor i in range(1, 7):\n    print(f\"{i}! = {fact(i)}\")",
     "递归式填 n * fact(n - 1)。",
     "def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nfor i in range(1, 7):\n    print(f\"{i}! = {fact(i)}\")"),
    (20, "演示二分查找的查找过程。",
     "nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\nlow, high = 0, len(nums) - 1\nfound = False\nwhile low <= high:\n    mid = (___ + high) // 2\n    print(\"Check index\", mid, \"->\", nums[mid])\n    if nums[mid] == target:\n        print(\"Found\", target, \"at index\", mid)\n        found = True\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\nif not found:\n    print(target, \"not found\")",
     "中点用 (low + high) // 2。",
     "nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\nlow, high = 0, len(nums) - 1\nfound = False\nwhile low <= high:\n    mid = (low + high) // 2\n    print(\"Check index\", mid, \"->\", nums[mid])\n    if nums[mid] == target:\n        print(\"Found\", target, \"at index\", mid)\n        found = True\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\nif not found:\n    print(target, \"not found\")"),
    (21, "输出 2000 到 2020 年间的闰年。",
     "for year in range(2000, 2021):\n    if (year % 4 == 0 and year % 100 != 0) or ___ == 0:\n        print(year)",
     "能被 400 整除也算闰年：year % 400。",
     "for year in range(2000, 2021):\n    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:\n        print(year)"),
    (22, "输出 1 到 5 的平方和立方表。",
     "print(f\"{'n':>3} {'n^2':>5} {'n^3':>5}\")\nfor n in range(1, 6):\n    print(f\"{n:>3} {n ** 2:>5} {___:>5}\")",
     "立方列填 n ** 3。",
     "print(f\"{'n':>3} {'n^2':>5} {'n^3':>5}\")\nfor n in range(1, 6):\n    print(f\"{n:>3} {n ** 2:>5} {n ** 3:>5}\")"),
    (23, "按分数从高到低输出字典内容。",
     "scores = {\"Alice\": 90, \"Bob\": 75, \"Cara\": 88}\nfor name, score in sorted(scores.items(), key=lambda x: x[1], ___=True):\n    print(name, score)",
     "降序参数填 reverse。",
     "scores = {\"Alice\": 90, \"Bob\": 75, \"Cara\": 88}\nfor name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):\n    print(name, score)"),
    (24, "生成并输出 1 到 20 的素数列表。",
     "primes = []\nfor n in range(2, 21):\n    for d in range(2, n):\n        if n % d == 0:\n            ___\n    else:\n        primes.append(n)\nprint(primes)",
     "被整除时 break 跳出内层循环。",
     "primes = []\nfor n in range(2, 21):\n    for d in range(2, n):\n        if n % d == 0:\n            break\n    else:\n        primes.append(n)\nprint(primes)"),
    (25, "打印 8x8 的黑白棋盘。",
     "for i in range(8):\n    for j in range(8):\n        if (i + j) % 2 == ___:\n            print(\"#\", end=\" \")\n        else:\n            print(\".\", end=\" \")\n    print()",
     "行列和为偶数时输出 #。",
     "for i in range(8):\n    for j in range(8):\n        if (i + j) % 2 == 0:\n            print(\"#\", end=\" \")\n        else:\n            print(\".\", end=\" \")\n    print()"),
    (26, "统计句子中每个单词的出现次数。",
     "text = \"the quick brown fox the lazy dog the\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + ___\nfor w, c in counts.items():\n    print(w, c)",
     "每次出现加 1。",
     "text = \"the quick brown fox the lazy dog the\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in counts.items():\n    print(w, c)"),
    (27, "用函数把十进制转为二进制。",
     "def to_binary(n):\n    if n == 0:\n        return \"0\"\n    bits = []\n    while n > 0:\n        bits.append(str(n % 2))\n        n //= ___\n    return \"\".join(reversed(bits))\n\nfor n in [0, 1, 5, 10, 42]:\n    print(f\"{n} -> {to_binary(n)}\")",
     "除以 2 取余，填 2。",
     "def to_binary(n):\n    if n == 0:\n        return \"0\"\n    bits = []\n    while n > 0:\n        bits.append(str(n % 2))\n        n //= 2\n    return \"\".join(reversed(bits))\n\nfor n in [0, 1, 5, 10, 42]:\n    print(f\"{n} -> {to_binary(n)}\")"),
    (28, "输出九九乘法表的奇数行。",
     "for i in range(1, 10, ___):\n    for j in range(1, i + 1):\n        print(f\"{j}x{i}={i * j}\", end=\"  \")\n    print()",
     "只取奇数行，步长填 2。",
     "for i in range(1, 10, 2):\n    for j in range(1, i + 1):\n        print(f\"{j}x{i}={i * j}\", end=\"  \")\n    print()"),
    (29, "统计 1 到 100 中奇数和偶数个数。",
     "odd = 0\neven = 0\nfor i in range(1, 101):\n    if i % 2 == ___:\n        even += 1\n    else:\n        odd += 1\nprint(\"Odd:\", odd, \"Even:\", even)",
     "偶数余数为 0。",
     "odd = 0\neven = 0\nfor i in range(1, 101):\n    if i % 2 == 0:\n        even += 1\n    else:\n        odd += 1\nprint(\"Odd:\", odd, \"Even:\", even)"),
    (30, "打印 A 到 E 的字母三角形。",
     "for i in range(5):\n    line = \"\"\n    for j in range(i + 1):\n        line += chr(65 + ___)\n    print(line)",
     "用 j 生成字母 A 起的序号。",
     "for i in range(5):\n    line = \"\"\n    for j in range(i + 1):\n        line += chr(65 + j)\n    print(line)"),
]


def build(suffix, data):
    return [make_q(suffix, num, desc, tpl, hint, sol)
            for num, desc, tpl, hint, sol in data]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH01_Hello_World")
    os.makedirs(out_dir, exist_ok=True)

    batches = {
        "medium_30.json": ("M", SIMPLE),   # 简单 ⭐⭐（较难档由 gen_ch01_expert.py 生成）
    }

    all_outs = []
    for fname, (suffix, data) in batches.items():
        questions = build(suffix, data)
        assert len(questions) == 30, "%s 必须 30 道，实际 %d" % (fname, len(questions))
        ids = [q["id"] for q in questions]
        assert ids == ["CH01-%s-%03d" % (suffix, i) for i in range(1, 31)], ids
        for q in questions:
            run(q["solution"])
            exec(q["test_cases"][0], {"captured_output": q["expected_output"]})
        all_outs.extend(q["expected_output"] for q in questions)

        payload = {"chapter": "CH01", "title": "Hello, World!",
                   "difficulty": questions[0]["difficulty"], "questions": questions}
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("已生成 %s（%d 道）" % (path, len(questions)))

    assert len(all_outs) == 30
    assert len(set(all_outs)) == 30, "30 道题的 expected_output 存在重复"
    print("OK: 简单档 30 道生成，expected_output 唯一，断言自校验通过")


if __name__ == "__main__":
    main()
