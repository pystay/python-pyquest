# -*- coding: utf-8 -*-
"""生成 CH13 元组 (Tuples) 题库（4 档 × 30 = 120 道）。

id 后缀沿用递进命名：E=超简单 / M=简单 / H=中等 / X=较难。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import gen_chapter  # noqa: E402

CHAPTER = "CH13"
TITLE = "元组 (Tuples)"
OUT_DIR = "CH13_Tuples"
DIFF = {"E": ("超简单", "⭐"), "M": ("简单", "⭐⭐"),
        "H": ("中等", "⭐⭐⭐"), "X": ("较难", "⭐⭐⭐⭐")}
TOPIC = {"E": TITLE, "M": TITLE, "H": TITLE, "X": TITLE}

EASY = [
    (1, "创建元组并输出。", "t = (1, 2, 3)\nprint(___)", "print 内填 t。", "t = (1, 2, 3)\nprint(t)"),
    (2, "用索引访问元组元素。", "t = (\"a\", \"b\", \"c\")\nprint(t[___])", "索引填 1。", "t = (\"a\", \"b\", \"c\")\nprint(t[1])"),
    (3, "用负索引访问元组最后一个元素。", "t = (10, 20, 30)\nprint(t[___])", "索引填 -1。", "t = (10, 20, 30)\nprint(t[-1])"),
    (4, "用切片截取元组。", "t = (1, 2, 3, 4)\nprint(t[1:3])", "切片填 1:3。", "t = (1, 2, 3, 4)\nprint(t[1:3])"),
    (5, "把元组解包到变量。", "point = (3, 4)\nx, y = ___\nprint(x, y)", "解包填 point。", "point = (3, 4)\nx, y = point\nprint(x, y)"),
    (6, "用 len() 求元组长度。", "t = (1, 2, 3, 4, 5)\nprint(len(___))", "len 内填 t。", "t = (1, 2, 3, 4, 5)\nprint(len(t))"),
    (7, "访问嵌套元组元素。", "t = ((1, 2), (3, 4))\nprint(t[1][0])", "填空嵌套索引。", "t = ((1, 2), (3, 4))\nprint(t[1][0])"),
    (8, "拼接两个元组。", "a = (1, 2)\nb = (3, 4)\nprint(___ + ___)", "依次填 a、b。", "a = (1, 2)\nb = (3, 4)\nprint('Sum:', a + b)"),
    (9, "重复元组。", "t = (0,)\nprint(___ * 3)", "填 t。", "t = (0,)\nprint(t * 3)"),
    (10, "遍历元组逐行输出。", "for v in (1, 2, 3):\n    print(___)\n", "输出变量 v。", "for v in (1, 2, 3):\n    print(v)"),
    (11, "用 in 判断元素在元组中。", "t = (1, 2, 3)\nprint(2 in ___)", "填 t。", "t = (1, 2, 3)\nprint(2 in t)"),
    (12, "用 count() 统计元素次数。", "t = (1, 2, 2, 3)\nprint(t.count(___))", "统计 2。", "t = (1, 2, 2, 3)\nprint(t.count(2))"),
    (13, "用 index() 查找元素位置。", "t = (10, 20, 30)\nprint(t.index(___))", "查找 20。", "t = (10, 20, 30)\nprint(t.index(20))"),
    (14, "创建单元素元组。", "t = (5, 6, 7, 8)\nprint(len(___))", "len 内填 t。", "t = (5, 6, 7, 8)\nprint(len(t))"),
    (15, "创建空元组。", "t = ()\nprint(len(___))", "len 内填 t。", "t = ()\nprint(len(t))"),
    (16, "元组转列表。", "t = (1, 2, 3)\nprint(list(___))", "list 内填 t。", "t = (1, 2, 3)\nprint(list(t))"),
    (17, "列表转元组。", "nums = [4, 5, 6]\nprint(tuple(___))", "tuple 内填 nums。", "nums = [4, 5, 6]\nprint(tuple(nums))"),
    (18, "比较两个元组。", "a = (1, 2)\nb = (1, 3)\nprint(___ < ___)", "依次填 a、b。", "a = (1, 3)\nb = (1, 2)\nprint(a < b)"),
    (19, "元组作为字典键。", "d = {(1, 2): \"point\"}\nprint(d[(1, 2)])", "填空键访问。", "d = {(1, 2): \"point\"}\nprint(d[(1, 2)])"),
    (20, "三值解包。", "t = (1, 2, 3)\na, b, c = ___\nprint(a, b, c)", "解包填 t。", "t = (1, 2, 3)\na, b, c = t\nprint(a, b, c)"),
    (21, "元组不可变验证（重新绑定）。", "t = (1, 2)\nt = (3, 4)\nprint(t)", "填空重新绑定。", "t = (1, 2)\nt = (3, 4)\nprint(t)"),
    (22, "元组解包交换变量。", "a, b = 1, 2\na, b = b, a\nprint(a, b)", "填空元组交换。", "a, b = 1, 2\na, b = b, a\nprint(a, b)"),
    (23, "元组内混合类型。", "t = (1, \"two\", 3.0)\nprint(t[1])", "索引填 1。", "t = (1, \"two\", 3.0)\nprint(t[1])"),
    (24, "切片步长取元组。", "t = (1, 2, 3, 4, 5)\nprint(t[::2])", "切片填 ::2。", "t = (1, 2, 3, 4, 5)\nprint(t[::2])"),
    (25, "元组反转切片。", "t = (1, 2, 3)\nprint(t[___])", "切片填 ::-1。", "t = (1, 2, 3)\nprint(t[::-1])"),
    (26, "解包时使用占位变量。", "t = (1, 2, 3)\na, _, c = ___\nprint(a, c)", "解包填 t。", "t = (1, 2, 3)\na, _, c = t\nprint(a, c)"),
    (27, "元组求和（sum）。", "t = (4, 5, 6)\nprint(sum(___))", "sum 内填 t。", "t = (4, 5, 6)\nprint(sum(t))"),
    (28, "元组最大值。", "t = (3, 9, 5)\nprint(max(___))", "max 内填 t。", "t = (3, 9, 5)\nprint(max(t))"),
    (29, "元组最小值。", "t = (10, 20, 6)\nprint(min(___))", "min 内填 t。", "t = (10, 20, 6)\nprint(min(t))"),
    (30, "综合：解包并输出。", "t = (\"Alice\", 20)\nname, age = ___\nprint(name, age)", "解包填 t。", "t = (\"Alice\", 20)\nname, age = t\nprint(name, age)"),
]

SIMPLE = [
    (1, "元组解包做运算。", "t = (3, 5)\na, b = t\nprint(f\"Sum: {a + b}\")", "填空解包求和。", "t = (3, 5)\na, b = t\nprint(f\"Sum: {a + b}\")"),
    (2, "元组返回并解包。", "def point():\n    return (5, 6)\n\nx, y = point()\nprint(x, y)", "填空解包返回。", "def point():\n    return (5, 6)\n\nx, y = point()\nprint(x, y)"),
    (3, "嵌套元组解包。", "data = ((1, 2), (3, 4))\n(a, b), (c, d) = data\nprint(a, b, c, d)", "填空嵌套解包。", "data = ((1, 2), (3, 4))\n(a, b), (c, d) = data\nprint(a, b, c, d)"),
    (4, "元组列表遍历解包。", "points = [(1, 2), (5, 6)]\nfor x, y in points:\n    print(x + y)", "填空遍历解包。", "points = [(1, 2), (5, 6)]\nfor x, y in points:\n    print(x + y)"),
    (5, "元组转列表并排序。", "t = (3, 1, 2, 4, 5)\nlst = list(t)\nlst.sort()\nprint(lst)", "填空转换排序。", "t = (3, 1, 2, 4, 5)\nlst = list(t)\nlst.sort()\nprint(lst)"),
    (6, "列表转元组后输出。", "nums = [7, 8, 9]\nt = tuple(nums)\nprint(t)", "填空转换。", "nums = [7, 8, 9]\nt = tuple(nums)\nprint(t)"),
    (7, "元组拼接与重复。", "a = (1, 2)\nb = (3,)\nprint(a + b + b)", "填空拼接重复。", "a = (1, 2)\nb = (3,)\nprint(a + b + b)"),
    (8, "元组切片反转。", "t = (1, 2, 3, 4, 5)\nprint(t[::-2])", "填空步长反转。", "t = (1, 2, 3, 4, 5)\nprint(t[::-2])"),
    (9, "元组成员统计。", "t = (1, 2, 2, 3, 2)\nprint(f\"Twos: {t.count(2)}\")", "填空 count。", "t = (1, 2, 2, 3, 2)\nprint(f\"Twos: {t.count(2)}\")"),
    (10, "元组最大最小和。", "t = (4, 9, 2)\nprint(max(t), min(t), sum(t))", "填空极值与和。", "t = (4, 9, 2)\nprint(max(t), min(t), sum(t))"),
    (11, "元组作为字典键使用。", "points = {(0, 0): \"origin\", (1, 1): \"unit\"}\nprint(points[(1, 1)])", "填空键访问。", "points = {(0, 0): \"origin\", (1, 1): \"unit\"}\nprint(points[(1, 1)])"),
    (12, "元组遍历带索引。", "t = (\"a\", \"b\", \"c\")\nfor i, v in enumerate(t):\n    print(i, v)", "填空 enumerate。", "t = (\"a\", \"b\", \"c\")\nfor i, v in enumerate(t):\n    print(i, v)"),
    (13, "元组解包字符串。", "t = (\"Py\", \"Quest\")\nfirst, second = t\nprint(first + second)", "填空解包拼接。", "t = (\"Py\", \"Quest\")\nfirst, second = t\nprint(first + second)"),
    (14, "用星号解包中间元素。", "t = (1, 2, 3, 4, 5)\nfirst, *rest = t\nprint(first, rest)", "填空星号解包。", "t = (1, 2, 3, 4, 5)\nfirst, *rest = t\nprint(first, rest)"),
    (15, "元组比较大小。", "a = (1, 2)\nb = (1, 1)\nprint('Greater:', a > b)", "填空元组比较。", "a = (1, 2)\nb = (1, 1)\nprint('Greater:', a > b)"),
    (16, "元组 join 字符串。", "t = (\"2024\", \"08\", \"12\")\nprint(\"-\".join(t))", "填空 join。", "t = (\"2024\", \"08\", \"12\")\nprint(\"-\".join(t))"),
    (17, "元组条件判断。", "t = (1, 2, 3)\nif 2 in t:\n    print(\"found\")\nelse:\n    print(\"missing\")", "填空 in 判断。", "t = (1, 2, 3)\nif 2 in t:\n    print(\"found\")\nelse:\n    print(\"missing\")"),
    (18, "元组切片赋值新元组。", "t = (1, 2, 3, 4)\npart = t[1:4]\nprint(part)", "填空切片。", "t = (1, 2, 3, 4)\npart = t[1:4]\nprint(part)"),
    (19, "元组长度统计。", "t = (\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\")\nprint(len(t))", "填空长度。", "t = (\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\")\nprint(len(t))"),
    (20, "元组中查找索引。", "t = (10, 20, 30, 40)\nprint(f\"Index: {t.index(30)}\")", "填空 index。", "t = (10, 20, 30, 40)\nprint(f\"Index: {t.index(30)}\")"),
    (21, "解包多返回值。", "def stats():\n    return (4, 5, 6)\n\na, b, c = stats()\nprint(a, b, c)", "填空三值解包。", "def stats():\n    return (4, 5, 6)\n\na, b, c = stats()\nprint(a, b, c)"),
    (22, "元组生成器转元组。", "t = tuple(i * i for i in range(1, 4))\nprint(t)", "填空生成器。", "t = tuple(i * i for i in range(1, 4))\nprint(t)"),
    (23, "元组元素求和与平均。", "t = (10, 20, 30)\navg = sum(t) / len(t)\nprint(f\"Average: {avg}\")", "填空平均。", "t = (10, 20, 30)\navg = sum(t) / len(t)\nprint(f\"Average: {avg}\")"),
    (24, "元组转字符串列表。", "t = (\"a\", \"b\")\nprint(list(t))", "填空转换。", "t = (\"a\", \"b\")\nprint(list(t))"),
    (25, "解包时忽略中间值。", "t = (1, 2, 3, 4)\nfirst, *_, last = t\nprint(first, last)", "填空忽略解包。", "t = (1, 2, 3, 4)\nfirst, *_, last = t\nprint(first, last)"),
    (26, "元组乘法解包重复。", "t = (\"ab\",)\nprint(t * 2)", "填空重复。", "t = (\"ab\",)\nprint(t * 2)"),
    (27, "嵌套元组遍历。", "matrix = ((2, 2), (4, 4))\nfor row in matrix:\n    print(sum(row))", "填空行求和。", "matrix = ((2, 2), (4, 4))\nfor row in matrix:\n    print(sum(row))"),
    (28, "元组是否可哈希验证。", "t = (1, 2)\nprint('Hashable:', hash(t) is not None)", "填空 hash 验证。", "t = (1, 2)\nprint('Hashable:', hash(t) is not None)"),
    (29, "元组解包变量交换。", "a, b = 10, 20\na, b = b, a\nprint(a, b)", "填空交换。", "a, b = 10, 20\na, b = b, a\nprint(a, b)"),
    (30, "综合：元组统计函数。", "def tstats(t):\n    return len(t), sum(t), max(t)\n\nn, s, m = tstats((2, 4, 6))\nprint(n, s, m)", "填空元组统计。", "def tstats(t):\n    return len(t), sum(t), max(t)\n\nn, s, m = tstats((2, 4, 6))\nprint(n, s, m)"),
]

MEDIUM = [
    (1, "元组实现坐标距离。", "def distance(p1, p2):\n    x1, y1 = p1\n    x2, y2 = p2\n    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5\n\nprint(f\"Dist: {distance((0, 0), (3, 4))}\")", "填空坐标距离。", "def distance(p1, p2):\n    x1, y1 = p1\n    x2, y2 = p2\n    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5\n\nprint(f\"Dist: {distance((0, 0), (3, 4))}\")"),
    (2, "元组列表按第二元素排序。", "pairs = [(1, 3), (2, 1), (3, 2)]\nsorted_pairs = sorted(pairs, key=lambda t: t[1])\nprint(sorted_pairs)", "填空按键排序。", "pairs = [(1, 3), (2, 1), (3, 2)]\nsorted_pairs = sorted(pairs, key=lambda t: t[1])\nprint(sorted_pairs)"),
    (3, "元组打包与解包。", "def make_pair():\n    return 1, 2\n\na, b = make_pair()\nprint('Sum:', a + b)", "填空打包返回。", "def make_pair():\n    return 1, 2\n\na, b = make_pair()\nprint('Sum:', a + b)"),
    (4, "zip 生成元组对。", "names = (\"Alice\", \"Bob\")\nscores = (90, 85)\nfor name, score in zip(names, scores):\n    print(name, score)", "填空 zip 元组。", "names = (\"Alice\", \"Bob\")\nscores = (90, 85)\nfor name, score in zip(names, scores):\n    print(name, score)"),
    (5, "元组解包做多变量运算。", "t = (2, 3, 4)\na, b, c = t\nprint(a * b + c)", "填空解包运算。", "t = (2, 3, 4)\na, b, c = t\nprint(a * b + c)"),
    (6, "元组列表求平均分。", "records = ((\"Math\", 90), (\"Eng\", 80), (\"Sci\", 85))\ntotal = sum(score for _, score in records)\nprint(f\"Average: {total / len(records)}\")", "填空成绩平均。", "records = ((\"Math\", 90), (\"Eng\", 80), (\"Sci\", 85))\ntotal = sum(score for _, score in records)\nprint(f\"Average: {total / len(records)}\")"),
    (7, "元组转字典。", "pairs = ((\"a\", 1), (\"b\", 2))\nd = dict(pairs)\nprint(d)", "填空转字典。", "pairs = ((\"a\", 1), (\"b\", 2))\nd = dict(pairs)\nprint(d)"),
    (8, "元组不可变与复制。", "t = (1, 2, 3)\ncopy = t[:]\nprint('Equal:', copy == t)", "填空复制比较。", "t = (1, 2, 3)\ncopy = t[:]\nprint('Equal:', copy == t)"),
    (9, "嵌套元组转列表。", "t = ((1, 2), (3, 4))\nflat = [n for row in t for n in row]\nprint(flat)", "填空扁平化。", "t = ((1, 2), (3, 4))\nflat = [n for row in t for n in row]\nprint(flat)"),
    (10, "元组元素计数统计。", "t = (1, 1, 2, 3, 3, 3)\ncounts = {}\nfor n in t:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)", "填空频次统计。", "t = (1, 1, 2, 3, 3, 3)\ncounts = {}\nfor n in t:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)"),
    (11, "元组切片反转拼接。", "t = (1, 2, 3, 4)\nresult = t[::-1] + t\nprint(result)", "填空反转拼接。", "t = (1, 2, 3, 4)\nresult = t[::-1] + t\nprint(result)"),
    (12, "元组列表筛选。", "points = [(1, 2), (3, -1), (-2, 4)]\npositive = [p for p in points if p[0] > 0]\nprint(positive)", "填空筛选。", "points = [(1, 2), (3, -1), (-2, 4)]\npositive = [p for p in points if p[0] > 0]\nprint(positive)"),
    (13, "元组解包循环变量。", "data = ((1, \"a\"), (2, \"b\"))\nfor num, ch in data:\n    print(f\"{num}: {ch}\")", "填空解包循环。", "data = ((1, \"a\"), (2, \"b\"))\nfor num, ch in data:\n    print(f\"{num}: {ch}\")"),
    (14, "元组成员判断与输出。", "t = (1, 3, 5, 7)\nif 4 in t:\n    print(\"present\")\nelse:\n    print(\"absent\")", "填空成员判断。", "t = (1, 3, 5, 7)\nif 4 in t:\n    print(\"present\")\nelse:\n    print(\"absent\")"),
    (15, "元组拼接多个。", "t = (1,) + (2,)\nprint(t)", "填空连续拼接。", "t = (1,) + (2,)\nprint(t)"),
    (16, "元组中找最大差值对。", "t = (3, 9, 1, 6)\nprint('Diff:', max(t) - min(t))", "填空差值。", "t = (3, 9, 1, 6)\nprint('Diff:', max(t) - min(t))"),
    (17, "元组与列表互转链。", "t = (1, 2, 3)\nlst = list(t)\nlst.append(5)\nt2 = tuple(lst)\nprint(t2)", "填空互转链。", "t = (1, 2, 3)\nlst = list(t)\nlst.append(5)\nt2 = tuple(lst)\nprint(t2)"),
    (18, "元组生成并判断。", "t = tuple(range(2, 11, 2))\nprint(len(t), t[0], t[-1])", "填空 range 元组。", "t = tuple(range(2, 11, 2))\nprint(len(t), t[0], t[-1])"),
    (19, "解包统计元组。", "t = (5, 8, 3)\na, b, c = t\nlargest = max(a, b, c)\nprint('Largest:', largest)", "填空解包取最大。", "t = (5, 8, 3)\na, b, c = t\nlargest = max(a, b, c)\nprint('Largest:', largest)"),
    (20, "元组列表转置。", "pairs = [(1, 2), (3, 4)]\nfirsts = [p[0] for p in pairs]\nseconds = [p[1] for p in pairs]\nprint(firsts, seconds)", "填空转置收集。", "pairs = [(1, 2), (3, 4)]\nfirsts = [p[0] for p in pairs]\nseconds = [p[1] for p in pairs]\nprint(firsts, seconds)"),
    (21, "元组切片步长求和。", "t = (1, 2, 3, 4, 5, 6, 7)\nprint(sum(t[::2]))", "填空步长求和。", "t = (1, 2, 3, 4, 5, 6, 7)\nprint(sum(t[::2]))"),
    (22, "元组作为函数参数解包。", "def add(a, b):\n    return a + b\n\npair = (3, 4)\nprint('Sum:', add(*pair))", "填空参数解包。", "def add(a, b):\n    return a + b\n\npair = (3, 4)\nprint('Sum:', add(*pair))"),
    (23, "元组比较链。", "t1 = (1, 2)\nt2 = (1, 3)\nt3 = (1, 1)\nprint('Chain:', t2 > t1 > t3)", "填空比较链。", "t1 = (1, 2)\nt2 = (1, 3)\nt3 = (1, 1)\nprint('Chain:', t2 > t1 > t3)"),
    (24, "元组不可变性演示。", "t = (1, [2, 3])\nt[1].append(4)\nprint(t)", "填空可变元素。", "t = (1, [2, 3])\nt[1].append(4)\nprint(t)"),
    (25, "元组索引与切片综合。", "t = (10, 20, 30, 40, 50)\nprint(t[1:4], t[-2:])", "填空综合切片。", "t = (10, 20, 30, 40, 50)\nprint(t[1:4], t[-2:])"),
    (26, "元组列表统计。", "scores = ((90, 80), (85, 95))\navg_first = sum(s[0] for s in scores) / len(scores)\nprint(f\"Avg: {avg_first}\")", "填空列平均。", "scores = ((90, 80), (85, 95))\navg_first = sum(s[0] for s in scores) / len(scores)\nprint(f\"Avg: {avg_first}\")"),
    (27, "元组元素顺序判断。", "t = (1, 2, 3)\nsorted_t = tuple(sorted(t))\nprint('Sorted:', t == sorted_t)", "填空顺序判断。", "t = (1, 2, 3)\nsorted_t = tuple(sorted(t))\nprint('Sorted:', t == sorted_t)"),
    (28, "元组解包生成列表。", "pairs = [(1, 2), (3, 4)]\nsums = [a + b for a, b in pairs]\nprint(sums)", "填空解包推导。", "pairs = [(1, 2), (3, 4)]\nsums = [a + b for a, b in pairs]\nprint(sums)"),
    (29, "元组查找邻近元素。", "t = (1, 3, 5, 7)\nidx = t.index(5)\nprint(t[idx - 1], t[idx + 1])", "填空邻近元素。", "t = (1, 3, 5, 7)\nidx = t.index(5)\nprint(t[idx - 1], t[idx + 1])"),
    (30, "综合：元组处理函数。", "def process(t):\n    return t[0] + t[-1], len(t)\n\ns, n = process((1, 2, 3, 4))\nprint(s, n)", "填空元组处理。", "def process(t):\n    return t[0] + t[-1], len(t)\n\ns, n = process((1, 2, 3, 4))\nprint(s, n)"),
]

HARD = [
    (1, "元组实现向量加法。", "def add_vectors(v1, v2):\n    return tuple(a + b for a, b in zip(v1, v2))\n\nprint(add_vectors((1, 2), (3, 4)))", "填空向量加法。", "def add_vectors(v1, v2):\n    return tuple(a + b for a, b in zip(v1, v2))\n\nprint(add_vectors((1, 2), (3, 4)))"),
    (2, "元组实现点积。", "def dot(v1, v2):\n    return sum(a * b for a, b in zip(v1, v2))\n\nprint(f\"Dot: {dot((1, 2, 3), (4, 5, 6))}\")", "填空点积。", "def dot(v1, v2):\n    return sum(a * b for a, b in zip(v1, v2))\n\nprint(f\"Dot: {dot((1, 2, 3), (4, 5, 6))}\")"),
    (3, "元组实现坐标旋转。", "def rotate90(p):\n    x, y = p\n    return (-y, x)\n\np = (1, 0)\nfor _ in range(3):\n    p = rotate90(p)\nprint(p)", "填空坐标旋转。", "def rotate90(p):\n    x, y = p\n    return (-y, x)\n\np = (1, 0)\nfor _ in range(3):\n    p = rotate90(p)\nprint(p)"),
    (4, "元组实现分数表示。", "def simplify(f):\n    num, den = f\n    a, b = num, den\n    while b:\n        a, b = b, a % b\n    return (num // a, den // a)\n\nprint('Simplified:', simplify((12, 18)))", "填空分数化简。", "def simplify(f):\n    num, den = f\n    a, b = num, den\n    while b:\n        a, b = b, a % b\n    return (num // a, den // a)\n\nprint('Simplified:', simplify((12, 18)))"),
    (5, "元组实现日期比较。", "def compare(d1, d2):\n    if d1 > d2:\n        return \"later\"\n    elif d1 < d2:\n        return \"earlier\"\n    return \"same\"\n\nprint(compare((2026, 8, 12), (2026, 9, 1)))", "填空日期比较。", "def compare(d1, d2):\n    if d1 > d2:\n        return \"later\"\n    elif d1 < d2:\n        return \"earlier\"\n    return \"same\"\n\nprint(compare((2026, 8, 12), (2026, 9, 1)))"),
    (6, "元组实现多项式表示。", "def poly_value(coeffs, x):\n    result = 0\n    for c in coeffs:\n        result = result * x + c\n    return result\n\nprint(f\"Value: {poly_value((1, 2, 3), 2)}\")", "填空多项式求值。", "def poly_value(coeffs, x):\n    result = 0\n    for c in coeffs:\n        result = result * x + c\n    return result\n\nprint(f\"Value: {poly_value((1, 2, 3), 2)}\")"),
    (7, "元组实现 LRU 键记录。", "def add_pair(pairs, key, value):\n    return pairs + ((key, value),)\n\npairs = ()\npairs = add_pair(pairs, \"a\", 1)\npairs = add_pair(pairs, \"b\", 2)\nprint(pairs)", "填空元组追加。", "def add_pair(pairs, key, value):\n    return pairs + ((key, value),)\n\npairs = ()\npairs = add_pair(pairs, \"a\", 1)\npairs = add_pair(pairs, \"b\", 2)\nprint(pairs)"),
    (8, "元组实现曼哈顿距离。", "def manhattan(p1, p2):\n    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])\n\nprint(f\"Distance: {manhattan((1, 1), (4, 5))}\")", "填空曼哈顿距离。", "def manhattan(p1, p2):\n    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])\n\nprint(f\"Distance: {manhattan((1, 1), (4, 5))}\")"),
    (9, "元组实现二进制转十进制。", "def bin_tuple_to_dec(bits):\n    result = 0\n    for bit in bits:\n        result = result * 2 + bit\n    return result\n\nprint('Decimal:', bin_tuple_to_dec((1, 0, 1)))", "填空二进制转换。", "def bin_tuple_to_dec(bits):\n    result = 0\n    for bit in bits:\n        result = result * 2 + bit\n    return result\n\nprint('Decimal:', bin_tuple_to_dec((1, 0, 1)))"),
    (10, "元组实现分组。", "def chunk_tuple(t, size):\n    return tuple(t[i:i + size] for i in range(0, len(t), size))\n\nprint(chunk_tuple((1, 2, 3, 4, 5), 2))", "填空分块。", "def chunk_tuple(t, size):\n    return tuple(t[i:i + size] for i in range(0, len(t), size))\n\nprint(chunk_tuple((1, 2, 3, 4, 5), 2))"),
    (11, "元组实现滑动窗口和。", "def window_sums(t, k):\n    return tuple(sum(t[i:i + k]) for i in range(len(t) - k + 1))\n\nprint(window_sums((1, 2, 3, 4), 2))", "填空窗口和。", "def window_sums(t, k):\n    return tuple(sum(t[i:i + k]) for i in range(len(t) - k + 1))\n\nprint(window_sums((1, 2, 3, 4), 2))"),
    (12, "元组实现排列对生成。", "def all_pairs(t):\n    return tuple((a, b) for i, a in enumerate(t) for b in t[i + 1:])\n\nprint(all_pairs((1, 2, 3)))", "填空排列对。", "def all_pairs(t):\n    return tuple((a, b) for i, a in enumerate(t) for b in t[i + 1:])\n\nprint(all_pairs((1, 2, 3)))"),
    (13, "元组实现字典键集合。", "def tuple_keys(d):\n    return tuple(sorted(d.keys()))\n\nprint(tuple_keys({(1, 2): \"a\", (3, 4): \"b\"}))", "填空元组键。", "def tuple_keys(d):\n    return tuple(sorted(d.keys()))\n\nprint(tuple_keys({(1, 2): \"a\", (3, 4): \"b\"}))"),
    (14, "元组实现矩阵行和。", "def row_sums(m):\n    return tuple(sum(row) for row in m)\n\nprint(row_sums(((1, 2), (3, 4), (5, 6))))", "填空行和。", "def row_sums(m):\n    return tuple(sum(row) for row in m)\n\nprint(row_sums(((1, 2), (3, 4), (5, 6))))"),
    (15, "元组实现坐标最近点。", "def closest_point(points, target):\n    def dist(p):\n        return (p[0] - target[0]) ** 2 + (p[1] - target[1]) ** 2\n    return min(points, key=dist)\n\nprint(closest_point(((1, 1), (4, 5), (2, 2)), (0, 0)))", "填空最近点。", "def closest_point(points, target):\n    def dist(p):\n        return (p[0] - target[0]) ** 2 + (p[1] - target[1]) ** 2\n    return min(points, key=dist)\n\nprint(closest_point(((1, 1), (4, 5), (2, 2)), (0, 0)))"),
    (16, "元组实现数字位数拆分。", "def split_digits(n):\n    return tuple(int(d) for d in str(n))\n\nprint(split_digits(123456))", "填空位数拆分。", "def split_digits(n):\n    return tuple(int(d) for d in str(n))\n\nprint(split_digits(123456))"),
    (17, "元组实现合并去重。", "def merge_tuple(t1, t2):\n    return tuple(sorted(set(t1 + t2)))\n\nprint(merge_tuple((1, 2, 3), (5, 6, 7)))", "填空合并去重。", "def merge_tuple(t1, t2):\n    return tuple(sorted(set(t1 + t2)))\n\nprint(merge_tuple((1, 2, 3), (5, 6, 7)))"),
    (18, "元组实现最大值索引。", "def max_index(t):\n    return t.index(max(t))\n\nprint('Index:', max_index((4, 9, 2, 7)))", "填空最大索引。", "def max_index(t):\n    return t.index(max(t))\n\nprint('Index:', max_index((4, 9, 2, 7)))"),
    (19, "元组实现分数加法。", "def add_fractions(f1, f2):\n    n1, d1 = f1\n    n2, d2 = f2\n    return (n1 * d2 + n2 * d1, d1 * d2)\n\nprint(add_fractions((1, 2), (1, 3)))", "填空分数加法。", "def add_fractions(f1, f2):\n    n1, d1 = f1\n    n2, d2 = f2\n    return (n1 * d2 + n2 * d1, d1 * d2)\n\nprint(add_fractions((1, 2), (1, 3)))"),
    (20, "元组实现回文元组。", "def is_pal_tuple(t):\n    return t == t[::-1]\n\nprint(is_pal_tuple((1, 2, 2, 1)), is_pal_tuple((1, 2, 3)))", "填空回文元组。", "def is_pal_tuple(t):\n    return t == t[::-1]\n\nprint(is_pal_tuple((1, 2, 2, 1)), is_pal_tuple((1, 2, 3)))"),
    (21, "元组实现累计和。", "def cumulative(t):\n    result = []\n    total = 0\n    for n in t:\n        total += n\n        result.append(total)\n    return tuple(result)\n\nprint(cumulative((1, 2, 3, 4)))", "填空累计和。", "def cumulative(t):\n    result = []\n    total = 0\n    for n in t:\n        total += n\n        result.append(total)\n    return tuple(result)\n\nprint(cumulative((1, 2, 3, 4)))"),
    (22, "元组实现交集。", "def tuple_intersect(t1, t2):\n    return tuple(sorted(set(t1) & set(t2)))\n\nprint('Intersection:', tuple_intersect((1, 2, 3), (2, 3, 4)))", "填空交集。", "def tuple_intersect(t1, t2):\n    return tuple(sorted(set(t1) & set(t2)))\n\nprint('Intersection:', tuple_intersect((1, 2, 3), (2, 3, 4)))"),
    (23, "元组实现两两乘积。", "def pair_products(t):\n    return tuple(a * b for a, b in zip(t, t[1:]))\n\nprint(pair_products((2, 3, 4, 5)))", "填空两两乘积。", "def pair_products(t):\n    return tuple(a * b for a, b in zip(t, t[1:]))\n\nprint(pair_products((2, 3, 4, 5)))"),
    (24, "元组实现索引映射。", "def indexed(t):\n    return tuple((i, v) for i, v in enumerate(t))\n\nprint(indexed((\"a\", \"b\")))", "填空索引映射。", "def indexed(t):\n    return tuple((i, v) for i, v in enumerate(t))\n\nprint(indexed((\"a\", \"b\")))"),
    (25, "元组实现可哈希集合操作。", "def add_point(points, p):\n    return tuple(sorted(set(points) | {p}))\n\npoints = ((1, 1), (2, 2))\npoints = add_point(points, (3, 3))\nprint(points)", "填空集合操作。", "def add_point(points, p):\n    return tuple(sorted(set(points) | {p}))\n\npoints = ((1, 1), (2, 2))\npoints = add_point(points, (3, 3))\nprint(points)"),
    (26, "元组实现最大值滑动。", "def sliding_max(t, k):\n    return tuple(max(t[i:i + k]) for i in range(len(t) - k + 1))\n\nprint(sliding_max((1, 3, 2, 5, 4), 2))", "填空滑动最大。", "def sliding_max(t, k):\n    return tuple(max(t[i:i + k]) for i in range(len(t) - k + 1))\n\nprint(sliding_max((1, 3, 2, 5, 4), 2))"),
    (27, "元组实现分类统计。", "def classify(nums):\n    evens = tuple(n for n in nums if n % 2 == 0)\n    odds = tuple(n for n in nums if n % 2 == 1)\n    return evens, odds\n\ne, o = classify((1, 2, 3, 4, 5))\nprint(e, o)", "填空分类返回。", "def classify(nums):\n    evens = tuple(n for n in nums if n % 2 == 0)\n    odds = tuple(n for n in nums if n % 2 == 1)\n    return evens, odds\n\ne, o = classify((1, 2, 3, 4, 5))\nprint(e, o)"),
    (28, "元组实现数字签名校验。", "def checksum(t):\n    return sum(v * (i + 1) for i, v in enumerate(t)) % 10\n\nprint('Checksum:', checksum((3, 1, 4)))", "填空校验和。", "def checksum(t):\n    return sum(v * (i + 1) for i, v in enumerate(t)) % 10\n\nprint('Checksum:', checksum((3, 1, 4)))"),
    (29, "元组实现范围判断。", "def in_box(p, box):\n    x1, y1, x2, y2 = box\n    return x1 <= p[0] <= x2 and y1 <= p[1] <= y2\n\nprint('In box:', in_box((3, 3), (1, 1, 5, 5)))", "填空范围判断。", "def in_box(p, box):\n    x1, y1, x2, y2 = box\n    return x1 <= p[0] <= x2 and y1 <= p[1] <= y2\n\nprint('In box:', in_box((3, 3), (1, 1, 5, 5)))"),
    (30, "综合：元组矩阵转置。", "def transpose(m):\n    rows = len(m)\n    cols = len(m[0])\n    return tuple(tuple(m[i][j] for i in range(rows)) for j in range(cols))\n\nprint(transpose(((1, 2, 3), (4, 5, 6))))", "填空转置。", "def transpose(m):\n    rows = len(m)\n    cols = len(m[0])\n    return tuple(tuple(m[i][j] for i in range(rows)) for j in range(cols))\n\nprint(transpose(((1, 2, 3), (4, 5, 6))))"),
]

BATCHES = {
    "easy_30.json": ("E", EASY),
    "medium_30.json": ("M", SIMPLE),
    "hard_30.json": ("H", MEDIUM),
    "expert_30.json": ("X", HARD),
}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gen_chapter(root, CHAPTER, TITLE, OUT_DIR, DIFF, TOPIC, BATCHES)


if __name__ == "__main__":
    main()
