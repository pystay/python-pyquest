# -*- coding: utf-8 -*-
"""生成 CH14 字典 (Dictionaries) 题库（4 档 × 30 = 120 道）。

id 后缀沿用递进命名：E=超简单 / M=简单 / H=中等 / X=较难。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import gen_chapter  # noqa: E402

CHAPTER = "CH14"
TITLE = "字典 (Dictionaries)"
OUT_DIR = "CH14_Dictionaries"
DIFF = {"E": ("超简单", "⭐"), "M": ("简单", "⭐⭐"),
        "H": ("中等", "⭐⭐⭐"), "X": ("较难", "⭐⭐⭐⭐")}
TOPIC = {"E": TITLE, "M": TITLE, "H": TITLE, "X": TITLE}

EASY = [
    (1, "创建字典并输出。", "d = {\"a\": 1, \"b\": 2}\nprint(___)", "print 内填 d。", "d = {\"a\": 1, \"b\": 2}\nprint(d)"),
    (2, "按键访问字典值。", "d = {\"name\": \"Alice\"}\nprint(d[___])", "键填 \"name\"。", "d = {\"name\": \"Alice\"}\nprint(d[\"name\"])"),
    (3, "用 get() 访问字典值。", "d = {\"x\": 10}\nprint(d.get(___))", "填 \"x\"。", "d = {\"x\": 10}\nprint(d.get(\"x\"))"),
    (4, "添加新键值对。", "d = {\"a\": 1}\nd[___] = 2\nprint(d)", "新键填 \"b\"。", "d = {\"a\": 1}\nd[\"c\"] = 2\nprint(d)"),
    (5, "修改字典值。", "d = {\"a\": 1}\nd[___] = 100\nprint(d)", "修改键填 \"a\"。", "d = {\"a\": 1}\nd[\"a\"] = 100\nprint(d)"),
    (6, "删除字典键。", "d = {\"a\": 1, \"b\": 2}\ndel d[___]\nprint(d)", "删除键填 \"a\"。", "d = {\"a\": 1, \"b\": 2}\ndel d[\"a\"]\nprint(d)"),
    (7, "用 len() 求字典长度。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nprint(len(___))", "len 内填 d。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nprint(len(d))"),
    (8, "输出字典所有键。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.___()))", "方法名填 keys。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.keys()))"),
    (9, "输出字典所有值。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.___()))", "方法名填 values。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.values()))"),
    (10, "输出字典键值对。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.___()))", "方法名填 items。", "d = {\"a\": 1, \"b\": 2}\nprint(list(d.items()))"),
    (11, "用 in 判断键是否存在。", "d = {\"a\": 1}\nprint(\"a\" in ___)", "填 d。", "d = {\"a\": 1}\nprint(\"a\" in d)"),
    (12, "遍历字典键。", "for k in {\"x\": 1, \"y\": 2}:\n    print(___)\n", "输出变量 k。", "for k in {\"x\": 1, \"y\": 2}:\n    print(k)"),
    (13, "遍历字典值。", "d = {\"a\": 1, \"b\": 2}\nfor v in d.___():\n    print(v)", "方法名填 values。", "d = {\"a\": 1, \"b\": 2}\nfor v in d.values():\n    print(v)"),
    (14, "遍历键值对。", "d = {\"a\": 1, \"b\": 2}\nfor k, v in d.___():\n    print(k, v)", "方法名填 items。", "d = {\"a\": 1, \"b\": 2}\nfor k, v in d.items():\n    print(k, v)"),
    (15, "用 pop() 删除并返回。", "d = {\"a\": 1, \"b\": 2}\nprint(d.pop(___))\nprint(d)", "删除键填 \"a\"。", "d = {\"a\": 1, \"b\": 2}\nprint(d.pop(\"a\"))\nprint(d)"),
    (16, "创建空字典。", "d = {}\nprint(len(___))", "len 内填 d。", "d = {}\nprint(len(d))"),
    (17, "字典值参与运算。", "d = {\"a\": 3, \"b\": 4}\nprint(d[___] + d[___])", "依次填 \"a\"、\"b\"。", "d = {\"a\": 3, \"b\": 4}\nprint(d[\"a\"] + d[\"b\"])"),
    (18, "get() 带默认值。", "d = {\"a\": 1}\nprint(d.get(\"b\", 5))", "填空默认值。", "d = {\"a\": 1}\nprint(d.get(\"b\", 5))"),
    (19, "update() 更新字典。", "d = {\"a\": 1}\nd.update({\"b\": 5})\nprint(d)", "填空 update。", "d = {\"a\": 1}\nd.update({\"b\": 5})\nprint(d)"),
    (20, "字典 setdefault。", "d = {\"a\": 1}\nd.setdefault(\"c\", 3)\nprint(d)", "填空 setdefault。", "d = {\"a\": 1}\nd.setdefault(\"c\", 3)\nprint(d)"),
    (21, "布尔值作字典值。", "d = {\"ok\": False}\nprint(d[___])", "键填 \"ok\"。", "d = {\"ok\": False}\nprint(d[\"ok\"])"),
    (22, "字符串字典值拼接。", "d = {\"greet\": \"Hello\"}\nprint(d[___] + \"!\")", "键填 \"greet\"。", "d = {\"greet\": \"Hello\"}\nprint(d[\"greet\"] + \"!\")"),
    (23, "整数键的字典。", "d = {1: \"one\", 2: \"two\"}\nprint(d[___])", "键填 1。", "d = {1: \"one\", 2: \"two\"}\nprint(d[1])"),
    (24, "字典 keys 判断。", "d = {\"a\": 1, \"b\": 2}\nprint(\"b\" in d.___())", "方法名填 keys。", "d = {\"a\": 1, \"b\": 2}\nprint(\"a\" in d.keys(), \"c\" in d.keys())"),
    (25, "嵌套字典访问。", "d = {\"user\": {\"name\": \"Bob\"}}\nprint(d[\"user\"][___])", "内层键填 \"name\"。", "d = {\"user\": {\"name\": \"Bob\"}}\nprint(d[\"user\"][\"name\"])"),
    (26, "字典解包（**）。", "d = {\"a\": 1}\nprint({**d, \"b\": 9})", "填空解包。", "d = {\"a\": 1}\nprint({**d, \"b\": 9})"),
    (27, "字典值统计（sum）。", "d = {\"a\": 10, \"b\": 20}\nprint(sum(d.___()))", "方法名填 values。", "d = {\"a\": 10, \"b\": 20}\nprint(sum(d.values()))"),
    (28, "字典最大值。", "d = {\"a\": 5, \"b\": 9}\nprint(max(d.___()))", "方法名填 values。", "d = {\"a\": 5, \"b\": 9}\nprint(max(d.values()))"),
    (29, "字典清空。", "d = {\"a\": 1}\nd.clear()\nprint(d)", "填空 clear。", "d = {\"a\": 1}\nd.clear()\nprint(d)"),
    (30, "综合：创建与访问。", "d = {\"name\": \"Ada\", \"age\": 36}\nprint(d[___], d[___])", "依次填 \"name\"、\"age\"。", "d = {\"name\": \"Ada\", \"age\": 36}\nprint(d[\"name\"], d[\"age\"])"),
]

SIMPLE = [
    (1, "统计列表元素频率。", "nums = [1, 2, 2, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)", "填空频率统计。", "nums = [1, 2, 2, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)"),
    (2, "用字典记录学生分数。", "scores = {\"Alice\": 90, \"Bob\": 85}\nfor name, score in scores.items():\n    print(f\"{name}: {score}\")", "填空遍历输出。", "scores = {\"Alice\": 90, \"Bob\": 85}\nfor name, score in scores.items():\n    print(f\"{name}: {score}\")"),
    (3, "合并两个字典。", "d1 = {\"a\": 1}\nd2 = {\"b\": 4}\nd1.update(d2)\nprint(d1)", "填空 update 合并。", "d1 = {\"a\": 1}\nd2 = {\"b\": 4}\nd1.update(d2)\nprint(d1)"),
    (4, "字典按键排序输出。", "d = {\"b\": 1, \"a\": 2, \"c\": 3}\nfor k in sorted(d):\n    print(k, d[k])", "填空排序遍历。", "d = {\"b\": 1, \"a\": 2, \"c\": 3}\nfor k in sorted(d):\n    print(k, d[k])"),
    (5, "字典按值排序。", "d = {\"a\": 3, \"b\": 1, \"c\": 2}\nsorted_d = sorted(d.items(), key=lambda x: x[1])\nprint(sorted_d)", "填空按值排序。", "d = {\"a\": 3, \"b\": 1, \"c\": 2}\nsorted_d = sorted(d.items(), key=lambda x: x[1])\nprint(sorted_d)"),
    (6, "get() 安全访问。", "d = {\"a\": 1}\nprint(d.get(\"b\", \"missing\"))", "填空安全访问。", "d = {\"a\": 1}\nprint(d.get(\"b\", \"missing\"))"),
    (7, "统计字符串字符频率。", "text = \"hello\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nprint(counts)", "填空字符频率。", "text = \"hello\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nprint(counts)"),
    (8, "字典推导式。", "squares = {n: n * n for n in range(1, 4)}\nprint(squares)", "填空推导式。", "squares = {n: n * n for n in range(1, 4)}\nprint(squares)"),
    (9, "统计单词个数。", "text = \"the cat the dog\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint(counts)", "填空单词频率。", "text = \"the cat the dog\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint(counts)"),
    (10, "字典值汇总。", "d = {\"a\": 10, \"b\": 20, \"c\": 30}\nprint(f\"Total: {sum(d.values())}\")", "填空值汇总。", "d = {\"a\": 10, \"b\": 20, \"c\": 30}\nprint(f\"Total: {sum(d.values())}\")"),
    (11, "pop 与默认值。", "d = {\"a\": 1}\nprint(d.pop(\"b\", 11))", "填空 pop 默认。", "d = {\"a\": 1}\nprint(d.pop(\"b\", 11))"),
    (12, "字典键值对数量与类型。", "d = {\"a\": 1, \"b\": 2}\nprint(len(d), type(d).__name__)", "填空统计。", "d = {\"a\": 1, \"b\": 2}\nprint(len(d), type(d).__name__)"),
    (13, "更新并输出字典。", "d = {\"a\": 1, \"b\": 2}\nd[\"c\"] = 3\nd[\"a\"] = 10\nprint(d)", "填空增改。", "d = {\"a\": 1, \"b\": 2}\nd[\"c\"] = 3\nd[\"a\"] = 10\nprint(d)"),
    (14, "嵌套字典遍历。", "users = {\"alice\": {\"age\": 20}, \"bob\": {\"age\": 25}}\nfor name, info in users.items():\n    print(name, info[\"age\"])", "填空嵌套遍历。", "users = {\"alice\": {\"age\": 20}, \"bob\": {\"age\": 25}}\nfor name, info in users.items():\n    print(name, info[\"age\"])"),
    (15, "字典成员判断。", "d = {\"a\": 1, \"b\": 2}\nif \"b\" in d:\n    print(\"found\")\nelse:\n    print(\"missing\")", "填空成员判断。", "d = {\"a\": 1, \"b\": 2}\nif \"b\" in d:\n    print(\"found\")\nelse:\n    print(\"missing\")"),
    (16, "值求和与平均。", "d = {\"a\": 80, \"b\": 90}\navg = sum(d.values()) / len(d)\nprint(f\"Average: {avg}\")", "填空平均。", "d = {\"a\": 80, \"b\": 90}\navg = sum(d.values()) / len(d)\nprint(f\"Average: {avg}\")"),
    (17, "用字典做计数器。", "counts = {}\nfor item in [\"a\", \"b\", \"a\", \"a\", \"b\", \"b\", \"b\"]:\n    counts[item] = counts.get(item, 0) + 1\nprint(counts)", "填空计数。", "counts = {}\nfor item in [\"a\", \"b\", \"a\", \"a\", \"b\", \"b\", \"b\"]:\n    counts[item] = counts.get(item, 0) + 1\nprint(counts)"),
    (18, "字典反转键值。", "d = {\"a\": 1, \"b\": 2}\nreversed_d = {v: k for k, v in d.items()}\nprint(reversed_d)", "填空反转。", "d = {\"a\": 1, \"b\": 2}\nreversed_d = {v: k for k, v in d.items()}\nprint(reversed_d)"),
    (19, "遍历输出键值对。", "d = {\"x\": 1, \"y\": 2, \"z\": 3}\nfor k, v in d.items():\n    print(f\"{k} = {v}\")", "填空格式化输出。", "d = {\"x\": 1, \"y\": 2, \"z\": 3}\nfor k, v in d.items():\n    print(f\"{k} = {v}\")"),
    (20, "setdefault 计数器。", "counts = {}\nfor ch in \"aba\":\n    counts.setdefault(ch, 0)\n    counts[ch] += 1\nprint(counts)", "填空 setdefault。", "counts = {}\nfor ch in \"aba\":\n    counts.setdefault(ch, 0)\n    counts[ch] += 1\nprint(counts)"),
    (21, "字典求最大值的键。", "d = {\"a\": 3, \"b\": 7, \"c\": 5}\nprint(max(d, key=d.get))", "填空最大键。", "d = {\"a\": 3, \"b\": 7, \"c\": 5}\nprint(max(d, key=d.get))"),
    (22, "合并两个列表为字典。", "keys = [\"a\", \"b\"]\nvalues = [1, 8]\nd = dict(zip(keys, values))\nprint(d)", "填空 zip 转字典。", "keys = [\"a\", \"b\"]\nvalues = [1, 8]\nd = dict(zip(keys, values))\nprint(d)"),
    (23, "字典值求和筛选。", "d = {\"a\": 5, \"b\": 12, \"c\": 8}\ntotal = sum(v for v in d.values() if v > 6)\nprint(f\"Sum: {total}\")", "填空筛选求和。", "d = {\"a\": 5, \"b\": 12, \"c\": 8}\ntotal = sum(v for v in d.values() if v > 6)\nprint(f\"Sum: {total}\")"),
    (24, "字典删除并确认。", "d = {\"a\": 1, \"b\": 2}\ndel d[\"a\"]\nprint(\"a\" in d, \"b\" in d)", "填空删除判断。", "d = {\"a\": 1, \"b\": 2}\ndel d[\"a\"]\nprint(\"a\" in d, \"b\" in d)"),
    (25, "字典默认值工厂。", "def default_factory():\n    return \"N/A\"\n\nd = {}\nvalue = d.get(\"name\", default_factory())\nprint(value)", "填空默认函数。", "def default_factory():\n    return \"N/A\"\n\nd = {}\nvalue = d.get(\"name\", default_factory())\nprint(value)"),
    (26, "统计正负值。", "d = {\"pos\": 0, \"neg\": 0}\nfor n in [3, -1, 5, -2]:\n    if n > 0:\n        d[\"pos\"] += 1\n    else:\n        d[\"neg\"] += 1\nprint(d)", "填空分类计数。", "d = {\"pos\": 0, \"neg\": 0}\nfor n in [3, -1, 5, -2]:\n    if n > 0:\n        d[\"pos\"] += 1\n    else:\n        d[\"neg\"] += 1\nprint(d)"),
    (27, "字典键排序取前。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nfirst_keys = sorted(d)[:3]\nprint(first_keys)", "填空排序切片。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nfirst_keys = sorted(d)[:3]\nprint(first_keys)"),
    (28, "多字典值运算。", "d1 = {\"a\": 2}\nd2 = {\"a\": 12}\nprint(d1[\"a\"] + d2[\"a\"])", "填空跨字典运算。", "d1 = {\"a\": 2}\nd2 = {\"a\": 12}\nprint(d1[\"a\"] + d2[\"a\"])"),
    (29, "字典更新与查询。", "d = {\"count\": 0}\nd[\"count\"] += 1\nd[\"count\"] += 1\nprint(d[\"count\"])", "填空累加。", "d = {\"count\": 0}\nd[\"count\"] += 1\nd[\"count\"] += 1\nprint(d[\"count\"])"),
    (30, "综合：字典构建与遍历。", "items = [(\"x\", 1), (\"y\", 2)]\nd = dict(items)\nfor k in d:\n    print(k, d[k])", "填空构建遍历。", "items = [(\"x\", 1), (\"y\", 2)]\nd = dict(items)\nfor k in d:\n    print(k, d[k])"),
]

MEDIUM = [
    (1, "统计单词频次并输出前 2。", "text = \"the cat and the dog and the bird\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2]:\n    print(w, c)", "填空词频排序。", "text = \"the cat and the dog and the bird\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2]:\n    print(w, c)"),
    (2, "字典实现商品价格表。", "prices = {\"apple\": 3.5, \"milk\": 5.0, \"bread\": 4.5}\ntotal = sum(prices.values())\nprint(f\"Total: {total}\")", "填空价格汇总。", "prices = {\"apple\": 3.5, \"milk\": 5.0, \"bread\": 4.5}\ntotal = sum(prices.values())\nprint(f\"Total: {total}\")"),
    (3, "字典合并覆盖。", "d1 = {\"a\": 1, \"b\": 2}\nd2 = {\"b\": 20, \"c\": 30}\nd1.update(d2)\nprint(d1)", "填空合并覆盖。", "d1 = {\"a\": 1, \"b\": 2}\nd2 = {\"b\": 20, \"c\": 30}\nd1.update(d2)\nprint(d1)"),
    (4, "统计字母大小写分类。", "text = \"Hello World\"\ncounts = {\"upper\": 0, \"lower\": 0}\nfor ch in text:\n    if ch.isupper():\n        counts[\"upper\"] += 1\n    elif ch.islower():\n        counts[\"lower\"] += 1\nprint(counts)", "填空大小写统计。", "text = \"Hello World\"\ncounts = {\"upper\": 0, \"lower\": 0}\nfor ch in text:\n    if ch.isupper():\n        counts[\"upper\"] += 1\n    elif ch.islower():\n        counts[\"lower\"] += 1\nprint(counts)"),
    (5, "字典按值降序取最大 3。", "d = {\"a\": 5, \"b\": 9, \"c\": 3, \"d\": 7}\ntop3 = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]\nprint(top3)", "填空降序取 3。", "d = {\"a\": 5, \"b\": 9, \"c\": 3, \"d\": 7}\ntop3 = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]\nprint(top3)"),
    (6, "字典构建成绩报告。", "scores = {\"Alice\": 92, \"Bob\": 78, \"Cara\": 88}\nfor name, score in scores.items():\n    grade = \"A\" if score >= 90 else \"B\" if score >= 80 else \"C\"\n    print(f\"{name}: {score} ({grade})\")", "填空成绩报告。", "scores = {\"Alice\": 92, \"Bob\": 78, \"Cara\": 88}\nfor name, score in scores.items():\n    grade = \"A\" if score >= 90 else \"B\" if score >= 80 else \"C\"\n    print(f\"{name}: {score} ({grade})\")"),
    (7, "嵌套字典处理。", "data = {\"user\": {\"name\": \"Tom\", \"age\": 25}}\nname = data[\"user\"][\"name\"]\nage = data[\"user\"][\"age\"]\nprint(name, age)", "填空嵌套访问。", "data = {\"user\": {\"name\": \"Tom\", \"age\": 25}}\nname = data[\"user\"][\"name\"]\nage = data[\"user\"][\"age\"]\nprint(name, age)"),
    (8, "字典推导过滤。", "nums = [1, 2, 3, 4, 5]\nsquares = {n: n * n for n in nums if n % 2 == 0}\nprint(squares)", "填空过滤推导。", "nums = [1, 2, 3, 4, 5]\nsquares = {n: n * n for n in nums if n % 2 == 0}\nprint(squares)"),
    (9, "统计并输出最频繁字符。", "text = \"banana\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nmost = max(counts, key=counts.get)\nprint(f\"Most: {most}\")", "填空众数字符。", "text = \"banana\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nmost = max(counts, key=counts.get)\nprint(f\"Most: {most}\")"),
    (10, "字典键值互换（唯一值）。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nswapped = {v: k for k, v in d.items()}\nprint(swapped)", "填空键值互换。", "d = {\"a\": 1, \"b\": 2, \"c\": 3}\nswapped = {v: k for k, v in d.items()}\nprint(swapped)"),
    (11, "字典存列表并操作。", "d = {\"nums\": [1, 2, 3]}\nd[\"nums\"].append(4)\nprint(d[\"nums\"])", "填空列表操作。", "d = {\"nums\": [1, 2, 3]}\nd[\"nums\"].append(4)\nprint(d[\"nums\"])"),
    (12, "统计数字分类。", "nums = [1, 2, 3, 4, 5, 6]\ncounts = {\"even\": 0, \"odd\": 0}\nfor n in nums:\n    key = \"even\" if n % 2 == 0 else \"odd\"\n    counts[key] += 1\nprint(counts)", "填空分类计数。", "nums = [1, 2, 3, 4, 5, 6]\ncounts = {\"even\": 0, \"odd\": 0}\nfor n in nums:\n    key = \"even\" if n % 2 == 0 else \"odd\"\n    counts[key] += 1\nprint(counts)"),
    (13, "字典求值最大键。", "d = {\"a\": 10, \"b\": 20, \"c\": 15}\nbest_key = max(d, key=d.get)\nprint(f\"Best: {best_key}\")", "填空最大值键。", "d = {\"a\": 10, \"b\": 20, \"c\": 15}\nbest_key = max(d, key=d.get)\nprint(f\"Best: {best_key}\")"),
    (14, "更新嵌套字典。", "config = {\"server\": {\"port\": 8080}}\nconfig[\"server\"][\"port\"] = 9090\nprint(config)", "填空嵌套修改。", "config = {\"server\": {\"port\": 8080}}\nconfig[\"server\"][\"port\"] = 9090\nprint(config)"),
    (15, "按值范围分类。", "scores = {\"a\": 55, \"b\": 85, \"c\": 95}\ngrades = {}\nfor name, s in scores.items():\n    if s >= 90:\n        grades[name] = \"A\"\n    elif s >= 70:\n        grades[name] = \"B\"\n    else:\n        grades[name] = \"C\"\nprint(grades)", "填空等级分类。", "scores = {\"a\": 55, \"b\": 85, \"c\": 95}\ngrades = {}\nfor name, s in scores.items():\n    if s >= 90:\n        grades[name] = \"A\"\n    elif s >= 70:\n        grades[name] = \"B\"\n    else:\n        grades[name] = \"C\"\nprint(grades)"),
    (16, "字典求值总和与平均。", "d = {\"a\": 20, \"b\": 30, \"c\": 40}\nprint(f\"Sum: {sum(d.values())}, Avg: {sum(d.values()) / len(d)}\")", "填空总和平均。", "d = {\"a\": 20, \"b\": 30, \"c\": 40}\nprint(f\"Sum: {sum(d.values())}, Avg: {sum(d.values()) / len(d)}\")"),
    (17, "dict 构造多样式。", "d1 = dict(a=1, b=2)\nd2 = dict([(\"c\", 3)])\nprint(d1, d2)", "填空构造。", "d1 = dict(a=1, b=2)\nd2 = dict([(\"c\", 3)])\nprint(d1, d2)"),
    (18, "统计键长度分组。", "words = [\"a\", \"bb\", \"ccc\"]\nlengths = {}\nfor w in words:\n    lengths[w] = len(w)\nprint(lengths)", "填空长度映射。", "words = [\"a\", \"bb\", \"ccc\"]\nlengths = {}\nfor w in words:\n    lengths[w] = len(w)\nprint(lengths)"),
    (19, "字典求最大差值。", "d = {\"a\": 3, \"b\": 9, \"c\": 1}\nprint(max(d.values()) - min(d.values()))", "填空极值差。", "d = {\"a\": 3, \"b\": 9, \"c\": 1}\nprint(max(d.values()) - min(d.values()))"),
    (20, "defaultdict 雏形。", "counts = {}\nfor w in [\"a\", \"b\", \"a\"]:\n    counts.setdefault(w, [])\n    counts[w].append(1)\nprint(counts)", "填空列表值。", "counts = {}\nfor w in [\"a\", \"b\", \"a\"]:\n    counts.setdefault(w, [])\n    counts[w].append(1)\nprint(counts)"),
    (21, "字典按键分组。", "nums = [1, 2, 3, 4]\ngroups = {}\nfor n in nums:\n    key = \"big\" if n > 2 else \"small\"\n    groups.setdefault(key, []).append(n)\nprint(groups)", "填空分组收集。", "nums = [1, 2, 3, 4]\ngroups = {}\nfor n in nums:\n    key = \"big\" if n > 2 else \"small\"\n    groups.setdefault(key, []).append(n)\nprint(groups)"),
    (22, "合并键值累加。", "d = {}\nfor pair in [(\"a\", 1), (\"a\", 2), (\"b\", 3)]:\n    k, v = pair\n    d[k] = d.get(k, 0) + v\nprint(d)", "填空累加合并。", "d = {}\nfor pair in [(\"a\", 1), (\"a\", 2), (\"b\", 3)]:\n    k, v = pair\n    d[k] = d.get(k, 0) + v\nprint(d)"),
    (23, "字典值格式化输出。", "d = {\"name\": \"PyQuest\", \"version\": \"1.0\"}\nprint(f\"{d['name']} v{d['version']}\")", "填空格式化。", "d = {\"name\": \"PyQuest\", \"version\": \"1.0\"}\nprint(f\"{d['name']} v{d['version']}\")"),
    (24, "统计并输出频次表。", "nums = [1, 1, 2, 2, 2, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nfor n in sorted(counts):\n    print(f\"{n}: {counts[n]}\")", "填空频次表。", "nums = [1, 1, 2, 2, 2, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nfor n in sorted(counts):\n    print(f\"{n}: {counts[n]}\")"),
    (25, "字典解包合并。", "a = {\"x\": 1}\nb = {\"y\": 2}\nc = {**a, **b}\nprint(c)", "填空解包合并。", "a = {\"x\": 1}\nb = {\"y\": 2}\nc = {**a, **b}\nprint(c)"),
    (26, "多字典值累加。", "d = {\"count\": 0}\nfor _ in range(5):\n    d[\"count\"] += 2\nprint(f\"Count: {d['count']}\")", "填空累加。", "d = {\"count\": 0}\nfor _ in range(5):\n    d[\"count\"] += 2\nprint(f\"Count: {d['count']}\")"),
    (27, "字典存坐标。", "points = {(0, 0): \"origin\", (1, 2): \"p1\"}\nprint(points[(1, 2)])", "填空坐标键。", "points = {(0, 0): \"origin\", (1, 2): \"p1\"}\nprint(points[(1, 2)])"),
    (28, "按条件重建字典。", "d = {\"a\": 1, \"b\": 4, \"c\": 9}\nsquares = {k: v for k, v in d.items() if v % 2 == 0}\nprint(squares)", "填空条件重建。", "d = {\"a\": 1, \"b\": 4, \"c\": 9}\nsquares = {k: v for k, v in d.items() if v % 2 == 0}\nprint(squares)"),
    (29, "统计各长度单词数。", "words = [\"hi\", \"hello\", \"hey\"]\ncounts = {}\nfor w in words:\n    counts[len(w)] = counts.get(len(w), 0) + 1\nprint(counts)", "填空长度统计。", "words = [\"hi\", \"hello\", \"hey\"]\ncounts = {}\nfor w in words:\n    counts[len(w)] = counts.get(len(w), 0) + 1\nprint(counts)"),
    (30, "综合：字典报表。", "sales = {\"mon\": 100, \"tue\": 150, \"wed\": 120}\ntotal = sum(sales.values())\nbest_day = max(sales, key=sales.get)\nprint(f\"Total: {total}, Best: {best_day}\")", "填空综合报表。", "sales = {\"mon\": 100, \"tue\": 150, \"wed\": 120}\ntotal = sum(sales.values())\nbest_day = max(sales, key=sales.get)\nprint(f\"Total: {total}, Best: {best_day}\")"),
]

HARD = [
    (1, "实现简易 LRU 缓存。", "class LRUCache:\n    def __init__(self, capacity):\n        self.cache = {}\n        self.capacity = capacity\n    def get(self, key):\n        return self.cache.get(key, -1)\n    def put(self, key, value):\n        if len(self.cache) >= self.capacity and key not in self.cache:\n            self.cache.pop(next(iter(self.cache)))\n        self.cache[key] = value\n\ncache = LRUCache(2)\ncache.put(\"a\", 1)\ncache.put(\"b\", 2)\ncache.put(\"c\", 3)\nprint(cache.get(\"a\"), cache.get(\"c\"))", "填空 LRU 雏形。", "class LRUCache:\n    def __init__(self, capacity):\n        self.cache = {}\n        self.capacity = capacity\n    def get(self, key):\n        return self.cache.get(key, -1)\n    def put(self, key, value):\n        if len(self.cache) >= self.capacity and key not in self.cache:\n            self.cache.pop(next(iter(self.cache)))\n        self.cache[key] = value\n\ncache = LRUCache(2)\ncache.put(\"a\", 1)\ncache.put(\"b\", 2)\ncache.put(\"c\", 3)\nprint(cache.get(\"a\"), cache.get(\"c\"))"),
    (2, "词频统计并输出完整排行。", "text = \"apple banana apple cherry banana apple\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nranking = sorted(counts.items(), key=lambda x: x[1], reverse=True)\nfor w, c in ranking:\n    print(f\"{w}: {c}\")", "填空词频排行。", "text = \"apple banana apple cherry banana apple\"\nwords = text.split()\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nranking = sorted(counts.items(), key=lambda x: x[1], reverse=True)\nfor w, c in ranking:\n    print(f\"{w}: {c}\")"),
    (3, "两字典求交集值。", "d1 = {\"a\": 1, \"b\": 2, \"c\": 3}\nd2 = {\"b\": 20, \"c\": 30, \"d\": 40}\ncommon = {k: d1[k] + d2[k] for k in d1 if k in d2}\nprint(common)", "填空交集求和。", "d1 = {\"a\": 1, \"b\": 2, \"c\": 3}\nd2 = {\"b\": 20, \"c\": 30, \"d\": 40}\ncommon = {k: d1[k] + d2[k] for k in d1 if k in d2}\nprint(common)"),
    (4, "字典实现数字转汉字（简化）。", "digit_map = {0: \"零\", 1: \"一\", 2: \"二\", 3: \"三\"}\nn = 13\nresult = \"\".join(digit_map[int(d)] for d in str(n))\nprint(result)", "填空数字映射。", "digit_map = {0: \"零\", 1: \"一\", 2: \"二\", 3: \"三\"}\nn = 13\nresult = \"\".join(digit_map[int(d)] for d in str(n))\nprint(result)"),
    (5, "深度合并两个字典。", "def deep_merge(d1, d2):\n    result = dict(d1)\n    for k, v in d2.items():\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\n            result[k] = deep_merge(result[k], v)\n        else:\n            result[k] = v\n    return result\n\nprint(deep_merge({\"a\": {\"x\": 1}}, {\"a\": {\"y\": 2}}))", "填空深度合并。", "def deep_merge(d1, d2):\n    result = dict(d1)\n    for k, v in d2.items():\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\n            result[k] = deep_merge(result[k], v)\n        else:\n            result[k] = v\n    return result\n\nprint(deep_merge({\"a\": {\"x\": 1}}, {\"a\": {\"y\": 2}}))"),
    (6, "统计并输出字母频次分布。", "text = \"abracadabra\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nfor ch in sorted(counts):\n    print(f\"{ch}: {'#' * counts[ch]}\")", "填空频次柱状。", "text = \"abracadabra\"\ncounts = {}\nfor ch in text:\n    counts[ch] = counts.get(ch, 0) + 1\nfor ch in sorted(counts):\n    print(f\"{ch}: {'#' * counts[ch]}\")"),
    (7, "字典实现分组求和。", "transactions = [(\"food\", 30), (\"transport\", 20), (\"food\", 40), (\"fun\", 50)]\ntotals = {}\nfor category, amount in transactions:\n    totals[category] = totals.get(category, 0) + amount\nprint(totals)", "填空分组求和。", "transactions = [(\"food\", 30), (\"transport\", 20), (\"food\", 40), (\"fun\", 50)]\ntotals = {}\nfor category, amount in transactions:\n    totals[category] = totals.get(category, 0) + amount\nprint(totals)"),
    (8, "嵌套字典构建成绩单。", "students = [(\"Alice\", \"Math\", 92), (\"Alice\", \"Eng\", 88), (\"Bob\", \"Math\", 78)]\nreport = {}\nfor name, subject, score in students:\n    report.setdefault(name, {})[subject] = score\nprint(report)", "填空嵌套构建。", "students = [(\"Alice\", \"Math\", 92), (\"Alice\", \"Eng\", 88), (\"Bob\", \"Math\", 78)]\nreport = {}\nfor name, subject, score in students:\n    report.setdefault(name, {})[subject] = score\nprint(report)"),
    (9, "字典实现频率排序。", "nums = [4, 1, 4, 2, 1, 4]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nby_freq = sorted(counts, key=lambda k: (-counts[k], k))\nprint(by_freq)", "填空频率排序。", "nums = [4, 1, 4, 2, 1, 4]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nby_freq = sorted(counts, key=lambda k: (-counts[k], k))\nprint(by_freq)"),
    (10, "字典实现缓存计算。", "cache = {}\ndef fib(n):\n    if n in cache:\n        return cache[n]\n    if n <= 1:\n        cache[n] = n\n    else:\n        cache[n] = fib(n - 1) + fib(n - 2)\n    return cache[n]\n\nprint(fib(10))\nprint(cache)", "填空缓存斐波那契。", "cache = {}\ndef fib(n):\n    if n in cache:\n        return cache[n]\n    if n <= 1:\n        cache[n] = n\n    else:\n        cache[n] = fib(n - 1) + fib(n - 2)\n    return cache[n]\n\nprint(fib(10))\nprint(cache)"),
    (11, "字典求最接近值。", "d = {\"a\": 10, \"b\": 25, \"c\": 40}\ntarget = 30\nclosest_key = min(d, key=lambda k: abs(d[k] - target))\nprint(f\"Closest: {closest_key}\")", "填空最近键。", "d = {\"a\": 10, \"b\": 25, \"c\": 40}\ntarget = 30\nclosest_key = min(d, key=lambda k: abs(d[k] - target))\nprint(f\"Closest: {closest_key}\")"),
    (12, "字典实现多级分组。", "data = [(\"x\", 1), (\"x\", 2), (\"y\", 3)]\ngroups = {}\nfor key, value in data:\n    groups.setdefault(key, []).append(value)\nprint(groups)", "填空多级分组。", "data = [(\"x\", 1), (\"x\", 2), (\"y\", 3)]\ngroups = {}\nfor key, value in data:\n    groups.setdefault(key, []).append(value)\nprint(groups)"),
    (13, "字典实现词频 top 字典。", "words = [\"a\", \"b\", \"a\", \"c\", \"b\", \"a\"]\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\ntop = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2])\nprint(top)", "填空 top 字典。", "words = [\"a\", \"b\", \"a\", \"c\", \"b\", \"a\"]\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\ntop = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2])\nprint(top)"),
    (14, "字典键值对筛选重建。", "d = {\"a\": 1, \"b\": 4, \"c\": 9, \"d\": 16}\nroots = {k: v for k, v in d.items() if int(v ** 0.5) ** 2 == v}\nprint(roots)", "填空平方筛选。", "d = {\"a\": 1, \"b\": 4, \"c\": 9, \"d\": 16}\nroots = {k: v for k, v in d.items() if int(v ** 0.5) ** 2 == v}\nprint(roots)"),
    (15, "字典实现状态统计。", "states = [\"open\", \"closed\", \"open\", \"open\", \"closed\"]\ncounts = {}\nfor s in states:\n    counts[s] = counts.get(s, 0) + 1\nprint(counts)", "填空状态统计。", "states = [\"open\", \"closed\", \"open\", \"open\", \"closed\"]\ncounts = {}\nfor s in states:\n    counts[s] = counts.get(s, 0) + 1\nprint(counts)"),
    (16, "字典实现价格折扣表。", "prices = {\"apple\": 3.5, \"milk\": 5.0}\ndiscounts = {k: round(v * 0.9, 2) for k, v in prices.items()}\nprint(discounts)", "填空折扣表。", "prices = {\"apple\": 3.5, \"milk\": 5.0}\ndiscounts = {k: round(v * 0.9, 2) for k, v in prices.items()}\nprint(discounts)"),
    (17, "字典求值之差最大对。", "d = {\"a\": 1, \"b\": 9, \"c\": 4}\nmax_key = max(d, key=d.get)\nmin_key = min(d, key=d.get)\nprint(f\"Max: {max_key}, Min: {min_key}\")", "填空极值对。", "d = {\"a\": 1, \"b\": 9, \"c\": 4}\nmax_key = max(d, key=d.get)\nmin_key = min(d, key=d.get)\nprint(f\"Max: {max_key}, Min: {min_key}\")"),
    (18, "嵌套字典深层取值。", "data = {\"a\": {\"b\": {\"c\": 42}}}\nresult = data[\"a\"][\"b\"][\"c\"]\nprint(result)", "填空深层取值。", "data = {\"a\": {\"b\": {\"c\": 42}}}\nresult = data[\"a\"][\"b\"][\"c\"]\nprint(result)"),
    (19, "字典实现默认值计数器。", "counts = {}\nfor ch in \"aabbb\":\n    counts[ch] = counts.get(ch, 0) + 1\nmost = max(counts, key=counts.get)\nprint(f\"{most}: {counts[most]}\")", "填空众数输出。", "counts = {}\nfor ch in \"aabbb\":\n    counts[ch] = counts.get(ch, 0) + 1\nmost = max(counts, key=counts.get)\nprint(f\"{most}: {counts[most]}\")"),
    (20, "字典求键值对数量变化。", "d = {}\nfor i in range(5):\n    d[i] = i * 10\nprint(len(d), d[4])", "填空动态构建。", "d = {}\nfor i in range(5):\n    d[i] = i * 10\nprint(len(d), d[4])"),
    (21, "字典实现缓存幂运算。", "cache = {}\ndef power_cache(base, exp):\n    key = (base, exp)\n    if key not in cache:\n        cache[key] = base ** exp\n    return cache[key]\n\nprint(power_cache(2, 5), power_cache(3, 3))\nprint(len(cache))", "填空幂缓存。", "cache = {}\ndef power_cache(base, exp):\n    key = (base, exp)\n    if key not in cache:\n        cache[key] = base ** exp\n    return cache[key]\n\nprint(power_cache(2, 5), power_cache(3, 3))\nprint(len(cache))"),
    (22, "字典实现分组最大值。", "data = [(\"a\", 5), (\"b\", 3), (\"a\", 9), (\"b\", 7)]\nmaxes = {}\nfor key, value in data:\n    maxes[key] = max(maxes.get(key, value), value)\nprint(maxes)", "填空分组最大。", "data = [(\"a\", 5), (\"b\", 3), (\"a\", 9), (\"b\", 7)]\nmaxes = {}\nfor key, value in data:\n    maxes[key] = max(maxes.get(key, value), value)\nprint(maxes)"),
    (23, "字典值排序后重建。", "d = {\"a\": 3, \"b\": 1, \"c\": 2}\nsorted_d = dict(sorted(d.items(), key=lambda x: x[1]))\nprint(sorted_d)", "填空值排序重建。", "d = {\"a\": 3, \"b\": 1, \"c\": 2}\nsorted_d = dict(sorted(d.items(), key=lambda x: x[1]))\nprint(sorted_d)"),
    (24, "字典实现词频柱状图。", "text = \"data science data\"\ncounts = {}\nfor w in text.split():\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items()):\n    print(f\"{w}: {'*' * c}\")", "填空柱状图。", "text = \"data science data\"\ncounts = {}\nfor w in text.split():\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items()):\n    print(f\"{w}: {'*' * c}\")"),
    (25, "字典求多键值交叉。", "d = {\"x\": 1, \"y\": 2, \"z\": 3}\nkeys = [\"x\", \"z\"]\nresult = {k: d[k] for k in keys}\nprint(result)", "填空键筛选。", "d = {\"x\": 1, \"y\": 2, \"z\": 3}\nkeys = [\"x\", \"z\"]\nresult = {k: d[k] for k in keys}\nprint(result)"),
    (26, "字典实现回文统计。", "words = [\"radar\", \"hello\", \"level\"]\npal_count = 0\nfor w in words:\n    if w == w[::-1]:\n        pal_count += 1\nprint(f\"Palindromes: {pal_count}\")", "填空回文统计。", "words = [\"radar\", \"hello\", \"level\"]\npal_count = 0\nfor w in words:\n    if w == w[::-1]:\n        pal_count += 1\nprint(f\"Palindromes: {pal_count}\")"),
    (27, "字典实现嵌套排序。", "students = {\"alice\": {\"score\": 90}, \"bob\": {\"score\": 85}}\nranking = sorted(students.items(), key=lambda x: x[1][\"score\"], reverse=True)\nfor name, info in ranking:\n    print(name, info[\"score\"])", "填空嵌套排序。", "students = {\"alice\": {\"score\": 90}, \"bob\": {\"score\": 85}}\nranking = sorted(students.items(), key=lambda x: x[1][\"score\"], reverse=True)\nfor name, info in ranking:\n    print(name, info[\"score\"])"),
    (28, "字典实现多条件筛选。", "d = {\"a\": 2, \"b\": 5, \"c\": 8, \"d\": 11}\nfiltered = {k: v for k, v in d.items() if v % 2 == 0 and v > 5}\nprint(filtered)", "填空多条件筛选。", "d = {\"a\": 2, \"b\": 5, \"c\": 8, \"d\": 11}\nfiltered = {k: v for k, v in d.items() if v % 2 == 0 and v > 5}\nprint(filtered)"),
    (29, "字典值求和占比。", "d = {\"a\": 2, \"b\": 6}\ntotal = sum(d.values())\nfor k, v in d.items():\n    print(f\"{k}: {v / total:.0%}\")", "填空占比输出。", "d = {\"a\": 2, \"b\": 6}\ntotal = sum(d.values())\nfor k, v in d.items():\n    print(f\"{k}: {v / total:.0%}\")"),
    (30, "综合：字典数据报告。", "sales = {\"mon\": 120, \"tue\": 90, \"wed\": 150}\ntotal = sum(sales.values())\navg = total / len(sales)\nbest = max(sales, key=sales.get)\nprint(f\"Total: {total}, Avg: {avg}, Best: {best}\")", "填空综合报告。", "sales = {\"mon\": 120, \"tue\": 90, \"wed\": 150}\ntotal = sum(sales.values())\navg = total / len(sales)\nbest = max(sales, key=sales.get)\nprint(f\"Total: {total}, Avg: {avg}, Best: {best}\")"),
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
