# -*- coding: utf-8 -*-
"""生成 CH15 集合 (Sets) 题库（4 档 × 30 = 120 道）。

id 后缀沿用递进命名：E=超简单 / M=简单 / H=中等 / X=较难。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import gen_chapter  # noqa: E402

CHAPTER = "CH15"
TITLE = "集合 (Sets)"
OUT_DIR = "CH15_Sets"
DIFF = {"E": ("超简单", "⭐"), "M": ("简单", "⭐⭐"),
        "H": ("中等", "⭐⭐⭐"), "X": ("较难", "⭐⭐⭐⭐")}
TOPIC = {"E": TITLE, "M": TITLE, "H": TITLE, "X": TITLE}

EASY = [
    (1, "创建集合并输出。", "s = {1, 2, 3}\nprint(___)", "print 内填 s。", "s = {1, 2, 3}\nprint(s)"),
    (2, "创建空集合。", "s = set()\nprint(len(__))", "len 内填 s。", "s = set()\nprint(len(s))"),
    (3, "用 add() 添加元素。", "s = {1, 2}\ns.add(4)\nprint(s)", "填空 add。", "s = {1, 2}\ns.add(4)\nprint(s)"),
    (4, "用 remove() 删除元素。", "s = {1, 2, 3}\ns.remove(2)\nprint(s)", "填空 remove。", "s = {1, 2, 3}\ns.remove(2)\nprint(s)"),
    (5, "用 discard() 删除不存在的元素。", "s = {1, 2}\ns.discard(9)\nprint(s)", "填空 discard。", "s = {1, 2}\ns.discard(9)\nprint(s)"),
    (6, "求集合长度。", "s = {1, 2, 3, 4}\nprint(len(__))", "len 内填 s。", "s = {1, 2, 3, 4}\nprint(len(s))"),
    (7, "集合自动去重。", "s = {1, 2, 2, 3, 4}\nprint(s)", "填空去重。", "s = {1, 2, 2, 3, 4}\nprint(s)"),
    (8, "用 in 判断成员。", "s = {1, 2, 3}\nprint(2 in __)", "填 s。", "s = {1, 2, 3}\nprint(2 in s)"),
    (9, "遍历集合。", "for v in {1, 2, 3}:\n    print(___)\n", "输出变量 v。", "for v in {1, 2, 3}:\n    print(v)"),
    (10, "求集合并集。", "a = {1, 2}\nb = {3, 4, 5}\nprint(a | b)", "填空并集。", "a = {1, 2}\nb = {3, 4, 5}\nprint(a | b)"),
    (11, "求集合交集。", "a = {1, 2}\nb = {2, 3}\nprint(a & b)", "填空交集。", "a = {1, 2}\nb = {2, 3}\nprint(a & b)"),
    (12, "求集合差集。", "a = {1, 2, 3, 4}\nb = {2}\nprint(a - b)", "填空差集。", "a = {1, 2, 3, 4}\nb = {2}\nprint(a - b)"),
    (13, "求集合对称差。", "a = {1, 2}\nb = {2, 3, 4, 5}\nprint(a ^ b)", "填空对称差。", "a = {1, 2}\nb = {2, 3, 4, 5}\nprint(a ^ b)"),
    (14, "集合转列表。", "s = {3, 1, 2}\nprint(list(s))", "填空转换。", "s = {3, 1, 2}\nprint(list(s))"),
    (15, "列表转集合。", "nums = [1, 2, 2, 3, 7]\nprint(set(nums))", "填空转换。", "nums = [1, 2, 2, 3, 7]\nprint(set(nums))"),
    (16, "求集合最大值。", "s = {3, 9, 5}\nprint(max(__))", "max 内填 s。", "s = {3, 9, 5}\nprint(max(s))"),
    (17, "求集合最小值。", "s = {3, 9, 5}\nprint(min(__))", "min 内填 s。", "s = {3, 9, 5}\nprint(min(s))"),
    (18, "求集合总和。", "s = {1, 2, 3}\nprint(sum(__))", "sum 内填 s。", "s = {1, 2, 3}\nprint(sum(s))"),
    (19, "用 union() 求并集。", "a = {1, 2}\nb = {3, 4, 5, 6}\nprint(a.union(b))", "填空 union。", "a = {1, 2}\nb = {3, 4, 5, 6}\nprint(a.union(b))"),
    (20, "用 intersection() 求交集。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a.intersection(b))", "填空 intersection。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a.intersection(b))"),
    (21, "判断子集。", "a = {1, 2}\nb = {1, 2, 4}\nprint('Subset:', a.issubset(b))", "填空 issubset。", "a = {1, 2}\nb = {1, 2, 4}\nprint('Subset:', a.issubset(b))"),
    (22, "判断超集。", "a = {1, 2, 3}\nb = {1, 2}\nprint(a.issuperset(b), b.issubset(a))", "填空 issuperset。", "a = {1, 2, 3}\nb = {1, 2}\nprint(a.issuperset(b), b.issubset(a))"),
    (23, "集合清空。", "s = {1, 2}\ns.clear()\nprint(len(__))", "len 内填 s。", "s = {1, 2}\ns.clear()\nprint(s)"),
    (24, "集合 pop() 删除。", "s = {5}\nprint(s.pop())", "填空 pop。", "s = {5}\nprint(s.pop())"),
    (25, "字符串集合去重。", "s = set(\"programming\")\nprint(len(s))", "填空字符去重。", "s = set(\"programming\")\nprint(len(s))"),
    (26, "布尔值集合。", "s = {True, False}\nprint(len(s))", "填空布尔集合。", "s = {True, False}\nprint(len(s))"),
    (27, "浮点数集合。", "s = {1.5, 2.5}\nprint(sum(s))", "填空浮点集合。", "s = {1.5, 2.5}\nprint(sum(s))"),
    (28, "集合运算组合。", "a = {1, 2}\nb = {2, 3}\nprint(len(a | b), len(a & b))", "填空运算长度。", "a = {1, 2}\nb = {2, 3}\nprint(len(a | b), len(a & b))"),
    (29, "集合添加多个。", "s = {1}\ns.update({2, 4, 5})\nprint(s)", "填空 update。", "s = {1}\ns.update({2, 4, 5})\nprint(s)"),
    (30, "综合：集合基本操作。", "s = {1, 2, 3}\ns.add(4)\ns.discard(1)\nprint('Size:', len(s))", "填空操作后长度。", "s = {1, 2, 3}\ns.add(4)\ns.discard(1)\nprint('Size:', len(s))"),
]

SIMPLE = [
    (1, "用集合去重列表。", "nums = [1, 2, 2, 3, 3, 3, 4]\nunique = list(set(nums))\nprint(sorted(unique))", "填空去重排序。", "nums = [1, 2, 2, 3, 3, 3, 4]\nunique = list(set(nums))\nprint(sorted(unique))"),
    (2, "求两列表公共元素。", "a = [1, 2, 3]\nb = [2, 3, 4]\ncommon = list(set(a) & set(b))\nprint('Common:', sorted(common))", "填空交集。", "a = [1, 2, 3]\nb = [2, 3, 4]\ncommon = list(set(a) & set(b))\nprint('Common:', sorted(common))"),
    (3, "求两列表差集。", "a = [1, 2, 3, 4, 6]\nb = [2, 3]\ndiff = list(set(a) - set(b))\nprint(sorted(diff))", "填空差集。", "a = [1, 2, 3, 4, 6]\nb = [2, 3]\ndiff = list(set(a) - set(b))\nprint(sorted(diff))"),
    (4, "集合成员判断并输出。", "s = {1, 2, 3}\nif 2 in s:\n    print(\"found\")\nelse:\n    print(\"missing\")", "填空成员判断。", "s = {1, 2, 3}\nif 2 in s:\n    print(\"found\")\nelse:\n    print(\"missing\")"),
    (5, "集合遍历统计。", "s = {1, 2, 3, 4}\ntotal = 0\nfor v in s:\n    total += v\nprint(f\"Total: {total}\")", "填空遍历累加。", "s = {1, 2, 3, 4}\ntotal = 0\nfor v in s:\n    total += v\nprint(f\"Total: {total}\")"),
    (6, "集合更新操作。", "s = {1, 2, 4}\ns.add(3)\ns.remove(1)\ns.discard(9)\nprint(s)", "填空链式操作。", "s = {1, 2, 4}\ns.add(3)\ns.remove(1)\ns.discard(9)\nprint(s)"),
    (7, "判断两集合相等。", "a = {1, 2, 3}\nb = {3, 2, 1}\nprint('Equal:', a == b)", "填空相等判断。", "a = {1, 2, 3}\nb = {3, 2, 1}\nprint('Equal:', a == b)"),
    (8, "求对称差并排序。", "a = {1, 2, 3}\nb = {3, 4}\nprint(sorted(a ^ b))", "填空对称差。", "a = {1, 2, 3}\nb = {3, 4}\nprint(sorted(a ^ b))"),
    (9, "集合推导式。", "squares = {n * n for n in range(1, 4)}\nprint(squares)", "填空推导式。", "squares = {n * n for n in range(1, 4)}\nprint(squares)"),
    (10, "统计唯一字符数。", "text = \"banana\"\nprint('Unique:', len(set(text)))", "填空唯一字符。", "text = \"banana\"\nprint('Unique:', len(set(text)))"),
    (11, "集合运算组合输出。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(len(a | b), len(a & b), len(a - b))", "填空三运算。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(len(a | b), len(a & b), len(a - b))"),
    (12, "集合 isdisjoint 判断。", "a = {1, 2}\nb = {3, 4}\nprint('Disjoint:', a.isdisjoint(b))", "填空无交集判断。", "a = {1, 2}\nb = {3, 4}\nprint('Disjoint:', a.isdisjoint(b))"),
    (13, "过滤重复单词。", "words = [\"a\", \"b\", \"a\"]\nunique_words = sorted(set(words))\nprint(unique_words)", "填空去重。", "words = [\"a\", \"b\", \"a\"]\nunique_words = sorted(set(words))\nprint(unique_words)"),
    (14, "集合求并集大小。", "a = {1, 2}\nb = {2, 3, 4}\nprint('Size:', len(a | b))", "填空并集大小。", "a = {1, 2}\nb = {2, 3, 4}\nprint('Size:', len(a | b))"),
    (15, "集合条件筛选。", "nums = set(range(1, 8))\nevens = {n for n in nums if n % 2 == 0}\nprint(evens)", "填空筛选推导。", "nums = set(range(1, 8))\nevens = {n for n in nums if n % 2 == 0}\nprint(evens)"),
    (16, "字符串与集合互转。", "s = set(\"abc\")\nprint(\"\".join(sorted(s)))", "填空字符排序。", "s = set(\"abc\")\nprint(\"\".join(sorted(s)))"),
    (17, "集合求最大最小差。", "s = {3, 9, 1, 7}\nprint('Span:', max(s) - min(s))", "填空极值差。", "s = {3, 9, 1, 7}\nprint('Span:', max(s) - min(s))"),
    (18, "集合更新多个。", "s = {1}\ns.update([2, 3], {4})\nprint('Count:', len(s))", "填空 update 多样。", "s = {1}\ns.update([2, 3], {4})\nprint('Count:', len(s))"),
    (19, "判断子集输出。", "a = {1, 2}\nb = {1, 2, 3}\nif a.issubset(b):\n    print(\"subset\")\nelse:\n    print(\"not subset\")", "填空子集判断。", "a = {1, 2}\nb = {1, 2, 3}\nif a.issubset(b):\n    print(\"subset\")\nelse:\n    print(\"not subset\")"),
    (20, "集合求元素总和。", "s = {4, 6, 8}\nprint(f\"Sum: {sum(s)}\")", "填空总和。", "s = {4, 6, 8}\nprint(f\"Sum: {sum(s)}\")"),
    (21, "集合与列表差异。", "s = {1, 2, 3}\nlst = [1, 2, 3, 3]\nprint(len(s), len(lst))", "填空长度对比。", "s = {1, 2, 3}\nlst = [1, 2, 3, 3]\nprint(len(s), len(lst))"),
    (22, "集合包含检查。", "s = {\"apple\", \"banana\"}\nprint(\"apple\" in s, \"cherry\" in s)", "填空包含检查。", "s = {\"apple\", \"banana\"}\nprint(\"apple\" in s, \"cherry\" in s)"),
    (23, "集合求差集大小。", "a = {1, 2, 3, 4}\nb = {2, 3}\nprint('Diff:', len(a - b))", "填空差集大小。", "a = {1, 2, 3, 4}\nb = {2, 3}\nprint('Diff:', len(a - b))"),
    (24, "清空后判断。", "s = {1, 2}\ns.clear()\nprint('Empty:', len(s) == 0)", "填空清空判断。", "s = {1, 2}\ns.clear()\nprint('Empty:', len(s) == 0)"),
    (25, "集合交集大小。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint('Inter:', len(a & b))", "填空交集大小。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint('Inter:', len(a & b))"),
    (26, "浮点集合运算。", "a = {1.5, 2.5}\nb = {2.5, 3.5}\nprint(sorted(a | b))", "填空浮点并集。", "a = {1.5, 2.5}\nb = {2.5, 3.5}\nprint(sorted(a | b))"),
    (27, "集合求和平均。", "s = {2, 4, 6}\nprint(f\"Average: {sum(s) / len(s)}\")", "填空平均。", "s = {2, 4, 6}\nprint(f\"Average: {sum(s) / len(s)}\")"),
    (28, "集合逆序输出。", "s = {1, 2, 3}\nprint(sorted(s, reverse=True))", "填空降序。", "s = {1, 2, 3}\nprint(sorted(s, reverse=True))"),
    (29, "集合与元组互转。", "t = (1, 2, 2, 3)\nprint(tuple(set(t)))", "填空元组转换。", "t = (1, 2, 2, 3)\nprint(tuple(set(t)))"),
    (30, "综合：集合统计。", "nums = [1, 2, 2, 3, 3, 3]\ns = set(nums)\nprint(len(s), sum(s))", "填空统计。", "nums = [1, 2, 2, 3, 3, 3]\ns = set(nums)\nprint(len(s), sum(s))"),
]

MEDIUM = [
    (1, "用集合求两字符串公共字符。", "a = \"hello\"\nb = \"world\"\ncommon = set(a) & set(b)\nprint('Common:', sorted(common))", "填空公共字符。", "a = \"hello\"\nb = \"world\"\ncommon = set(a) & set(b)\nprint('Common:', sorted(common))"),
    (2, "集合求唯一单词。", "text = \"the cat the dog\"\nwords = text.split()\nunique = set(words)\nprint(len(unique), sorted(unique))", "填空唯一单词。", "text = \"the cat the dog\"\nwords = text.split()\nunique = set(words)\nprint(len(unique), sorted(unique))"),
    (3, "集合求对称差元素。", "a = {1, 2, 3, 4}\nb = {3, 4, 5}\nprint(sorted(a ^ b))", "填空对称差。", "a = {1, 2, 3, 4}\nb = {3, 4, 5}\nprint(sorted(a ^ b))"),
    (4, "集合推导带条件。", "nums = range(1, 11)\nbig = {n for n in nums if n > 5}\nprint(big)", "填空条件推导。", "nums = range(1, 11)\nbig = {n for n in nums if n > 5}\nprint(big)"),
    (5, "集合运算综合。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a | b)\nprint(a & b)\nprint(a - b)", "填空三运算输出。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a | b)\nprint(a & b)\nprint(a - b)"),
    (6, "集合判断包含关系。", "a = {1, 2}\nb = {1, 2, 3}\nprint('Rel:', a.issubset(b), b.issuperset(a))", "填空包含关系。", "a = {1, 2}\nb = {1, 2, 3}\nprint('Rel:', a.issubset(b), b.issuperset(a))"),
    (7, "统计每字符串唯一字符数。", "words = [\"ab\", \"abc\", \"abca\"]\ncounts = {w: len(set(w)) for w in words}\nprint(counts)", "填空唯一字符统计。", "words = [\"ab\", \"abc\", \"abca\"]\ncounts = {w: len(set(w)) for w in words}\nprint(counts)"),
    (8, "集合去重后排序输出。", "nums = [5, 1, 3, 1, 5]\nfor n in sorted(set(nums)):\n    print(n)", "填空去重遍历。", "nums = [5, 1, 3, 1, 5]\nfor n in sorted(set(nums)):\n    print(n)"),
    (9, "集合求差集用于筛选。", "all_users = {\"a\", \"b\", \"c\"}\nactive = {\"a\", \"c\"}\ninactive = all_users - active\nprint(sorted(inactive))", "填空差集筛选。", "all_users = {\"a\", \"b\", \"c\"}\nactive = {\"a\", \"c\"}\ninactive = all_users - active\nprint(sorted(inactive))"),
    (10, "集合求并集去重。", "tags1 = {\"python\", \"data\"}\ntags2 = {\"data\", \"ai\"}\nall_tags = tags1 | tags2\nprint(len(all_tags), sorted(all_tags))", "填空并集去重。", "tags1 = {\"python\", \"data\"}\ntags2 = {\"data\", \"ai\"}\nall_tags = tags1 | tags2\nprint(len(all_tags), sorted(all_tags))"),
    (11, "集合生成数对。", "a = {1, 2}\nb = {3, 4}\npairs = {(x, y) for x in a for y in b}\nprint(sorted(pairs))", "填空笛卡尔积。", "a = {1, 2}\nb = {3, 4}\npairs = {(x, y) for x in a for y in b}\nprint(sorted(pairs))"),
    (12, "集合求交集大小比较。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nc = {1, 2, 5, 6}\nprint(len(a & b), len(a & c), len(b & c))", "填空多交集。", "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nc = {1, 2, 5, 6}\nprint(len(a & b), len(a & c), len(b & c))"),
    (13, "集合求缺失元素。", "expected = {1, 2, 3, 4, 5}\nactual = {1, 3, 5}\nmissing = expected - actual\nprint(sorted(missing))", "填空缺失元素。", "expected = {1, 2, 3, 4, 5}\nactual = {1, 3, 5}\nmissing = expected - actual\nprint(sorted(missing))"),
    (14, "集合成员批量判断。", "s = {1, 2, 3}\nchecks = [n in s for n in [1, 5, 3]]\nprint(checks)", "填空批量判断。", "s = {1, 2, 3}\nchecks = [n in s for n in [1, 5, 3]]\nprint(checks)"),
    (15, "集合去重后求和。", "nums = [1, 2, 2, 3, 3, 3]\nprint(f\"Unique sum: {sum(set(nums))}\")", "填空去重求和。", "nums = [1, 2, 2, 3, 3, 3]\nprint(f\"Unique sum: {sum(set(nums))}\")"),
    (16, "集合求最值与长度。", "s = {4, 9, 2, 7}\nprint(max(s), min(s), len(s))", "填空极值长度。", "s = {4, 9, 2, 7}\nprint(max(s), min(s), len(s))"),
    (17, "集合应用：去除重复后平均。", "nums = [1, 1, 2, 3, 3]\nunique = set(nums)\nprint(f\"Average: {sum(unique) / len(unique)}\")", "填空去重平均。", "nums = [1, 1, 2, 3, 3]\nunique = set(nums)\nprint(f\"Average: {sum(unique) / len(unique)}\")"),
    (18, "集合求公共字母。", "words = [\"hello\", \"help\"]\ncommon = set(words[0])\nfor w in words[1:]:\n    common &= set(w)\nprint('Common:', sorted(common))", "填空多集合交集。", "words = [\"hello\", \"help\"]\ncommon = set(words[0])\nfor w in words[1:]:\n    common &= set(w)\nprint('Common:', sorted(common))"),
    (19, "集合更新运算。", "a = {1, 2, 3}\na.update({4, 5, 6})\na.discard(2)\nprint(a)", "填空更新链。", "a = {1, 2, 3}\na.update({4, 5, 6})\na.discard(2)\nprint(a)"),
    (20, "集合判断是否相等。", "a = {1, 2, 3}\nb = {3, 2, 1}\nc = {1, 2, 4}\nprint('Equal:', a == b, a == c)", "填空相等判断。", "a = {1, 2, 3}\nb = {3, 2, 1}\nc = {1, 2, 4}\nprint('Equal:', a == b, a == c)"),
    (21, "集合求差与并组合。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted((a - b) | (b - a)))", "填空对称差组合。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted((a - b) | (b - a)))"),
    (22, "字符串集合统计元音。", "text = \"hello\"\nvowels = set(\"aeiou\")\ncount = sum(1 for ch in text if ch in vowels)\nprint(f\"Vowels: {count}\")", "填空元音统计。", "text = \"hello\"\nvowels = set(\"aeiou\")\ncount = sum(1 for ch in text if ch in vowels)\nprint(f\"Vowels: {count}\")"),
    (23, "集合求最大数。", "s = {5, 9, 2, 12}\nprint(f\"Max: {max(s)}\")", "填空最大值。", "s = {5, 9, 2, 12}\nprint(f\"Max: {max(s)}\")"),
    (24, "集合去重后排序。", "data = [3, 1, 3, 2, 1, 2, 5]\nprint(sorted(set(data)))", "填空去重排序。", "data = [3, 1, 3, 2, 1, 2, 5]\nprint(sorted(set(data)))"),
    (25, "集合元素个数统计。", "a = {1, 2}\nb = {2, 3}\nc = {3, 4}\nprint('Union:', len(a | b | c))", "填空多并集。", "a = {1, 2}\nb = {2, 3}\nc = {3, 4}\nprint('Union:', len(a | b | c))"),
    (26, "集合求交集元素和。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint('Sum:', sum(a & b))", "填空交集和。", "a = {1, 2, 3}\nb = {2, 3, 4}\nprint('Sum:', sum(a & b))"),
    (27, "集合筛选质数雏形。", "nums = {n for n in range(2, 15)}\nprimes = {n for n in nums if all(n % d for d in range(2, n))}\nprint(primes)", "填空质数集合。", "nums = {n for n in range(2, 15)}\nprimes = {n for n in nums if all(n % d for d in range(2, n))}\nprint(primes)"),
    (28, "集合求互斥元素。", "a = {1, 2, 3}\nb = {2, 3, 4}\nonly_a = a - b\nonly_b = b - a\nprint(sorted(only_a), sorted(only_b))", "填空互斥。", "a = {1, 2, 3}\nb = {2, 3, 4}\nonly_a = a - b\nonly_b = b - a\nprint(sorted(only_a), sorted(only_b))"),
    (29, "集合综合统计。", "nums = [1, 2, 2, 3, 4, 4, 4]\ns = set(nums)\nprint(len(nums), len(s), len(nums) - len(s))", "填空重复统计。", "nums = [1, 2, 2, 3, 4, 4, 4]\ns = set(nums)\nprint(len(nums), len(s), len(nums) - len(s))"),
    (30, "综合：集合处理函数。", "def unique_sum(nums):\n    return sum(set(nums))\n\nprint('Total:', unique_sum([1, 2, 2, 3]))", "填空去重求和函数。", "def unique_sum(nums):\n    return sum(set(nums))\n\nprint('Total:', unique_sum([1, 2, 2, 3]))"),
]

HARD = [
    (1, "用集合求最长连续序列。", "nums = [100, 4, 200, 1, 3, 2]\nnum_set = set(nums)\nlongest = 0\nfor n in num_set:\n    if n - 1 not in num_set:\n        length = 1\n        while n + length in num_set:\n            length += 1\n        longest = max(longest, length)\nprint(f\"Longest: {longest}\")", "填空集合连续序列。", "nums = [100, 4, 200, 1, 3, 2]\nnum_set = set(nums)\nlongest = 0\nfor n in num_set:\n    if n - 1 not in num_set:\n        length = 1\n        while n + length in num_set:\n            length += 1\n        longest = max(longest, length)\nprint(f\"Longest: {longest}\")"),
    (2, "集合实现单词字母差。", "def missing_letters(word):\n    alphabet = set(\"abcdefghijklmnopqrstuvwxyz\")\n    return sorted(alphabet - set(word.lower()))\n\nprint(missing_letters(\"abc\"))", "填空缺失字母。", "def missing_letters(word):\n    alphabet = set(\"abcdefghijklmnopqrstuvwxyz\")\n    return sorted(alphabet - set(word.lower()))\n\nprint(missing_letters(\"abc\"))"),
    (3, "集合实现去重保序。", "def unique_ordered(items):\n    seen = set()\n    result = []\n    for item in items:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nprint(unique_ordered([3, 1, 3, 2, 1]))", "填空去重保序。", "def unique_ordered(items):\n    seen = set()\n    result = []\n    for item in items:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nprint(unique_ordered([3, 1, 3, 2, 1]))"),
    (4, "集合实现变位词分组。", "def group_anagrams(words):\n    groups = {}\n    for w in words:\n        key = tuple(sorted(w))\n        groups.setdefault(key, []).append(w)\n    return groups\n\nprint(group_anagrams([\"abc\", \"cba\", \"def\", \"fed\"]))", "填空变位词分组。", "def group_anagrams(words):\n    groups = {}\n    for w in words:\n        key = tuple(sorted(w))\n        groups.setdefault(key, []).append(w)\n    return groups\n\nprint(group_anagrams([\"abc\", \"cba\", \"def\", \"fed\"]))"),
    (5, "集合求最大交集子集。", "sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]\ncommon = sets[0]\nfor s in sets[1:]:\n    common &= s\nprint(common)", "填空多集合交集。", "sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]\ncommon = sets[0]\nfor s in sets[1:]:\n    common &= s\nprint(common)"),
    (6, "集合实现对称差去重。", "def symmetric(a, b):\n    return sorted(a ^ b)\n\nprint(symmetric({1, 2, 3}, {3, 4, 5}))", "填空对称差函数。", "def symmetric(a, b):\n    return sorted(a ^ b)\n\nprint(symmetric({1, 2, 3}, {3, 4, 5}))"),
    (7, "集合求覆盖检查。", "def covers(available, required):\n    return required.issubset(available)\n\navailable = {\"a\", \"b\", \"c\", \"d\"}\nrequired = {\"a\", \"c\"}\nprint('Covered:', covers(available, required))", "填空覆盖检查。", "def covers(available, required):\n    return required.issubset(available)\n\navailable = {\"a\", \"b\", \"c\", \"d\"}\nrequired = {\"a\", \"c\"}\nprint('Covered:', covers(available, required))"),
    (8, "集合实现两数差对。", "def diff_pairs(nums, diff):\n    num_set = set(nums)\n    return sorted({(n, n + diff) for n in num_set if n + diff in num_set})\n\nprint(diff_pairs([1, 3, 5, 7], 2))", "填空差对。", "def diff_pairs(nums, diff):\n    num_set = set(nums)\n    return sorted({(n, n + diff) for n in num_set if n + diff in num_set})\n\nprint(diff_pairs([1, 3, 5, 7], 2))"),
    (9, "集合实现多列表并集去重。", "lists = [[1, 2], [2, 3], [3, 4]]\nall_items = set()\nfor lst in lists:\n    all_items.update(lst)\nprint('All:', sorted(all_items))", "填空多列表并集。", "lists = [[1, 2], [2, 3], [3, 4]]\nall_items = set()\nfor lst in lists:\n    all_items.update(lst)\nprint('All:', sorted(all_items))"),
    (10, "集合求出现次数大于 1 的。", "def duplicates(nums):\n    seen = set()\n    dupes = set()\n    for n in nums:\n        if n in seen:\n            dupes.add(n)\n        seen.add(n)\n    return sorted(dupes)\n\nprint('Dupes:', duplicates([1, 2, 2, 3, 3, 3]))", "填空重复检测。", "def duplicates(nums):\n    seen = set()\n    dupes = set()\n    for n in nums:\n        if n in seen:\n            dupes.add(n)\n        seen.add(n)\n    return sorted(dupes)\n\nprint('Dupes:', duplicates([1, 2, 2, 3, 3, 3]))"),
    (11, "集合求最长公共子集长度。", "def common_count(a, b):\n    return len(a & b)\n\nprint('Common:', common_count({1, 2, 3, 4}, {3, 4, 5}))", "填空公共计数。", "def common_count(a, b):\n    return len(a & b)\n\nprint('Common:', common_count({1, 2, 3, 4}, {3, 4, 5}))"),
    (12, "集合实现字符串差异。", "def char_diff(s1, s2):\n    return sorted(set(s1) ^ set(s2))\n\nprint(char_diff(\"abc\", \"abd\"))", "填空字符差异。", "def char_diff(s1, s2):\n    return sorted(set(s1) ^ set(s2))\n\nprint(char_diff(\"abc\", \"abd\"))"),
    (13, "集合求唯一数之和。", "def unique_sum_lists(lists):\n    return sum(set().union(*[set(l) for l in lists]))\n\nprint('Sum:', unique_sum_lists([[1, 2], [2, 3]]))", "填空唯一和。", "def unique_sum_lists(lists):\n    return sum(set().union(*[set(l) for l in lists]))\n\nprint('Sum:', unique_sum_lists([[1, 2], [2, 3]]))"),
    (14, "集合实现相似度。", "def jaccard(a, b):\n    return len(a & b) / len(a | b)\n\nprint(round(jaccard({1, 2, 3}, {2, 3, 4}), 2))", "填空 Jaccard。", "def jaccard(a, b):\n    return len(a & b) / len(a | b)\n\nprint(round(jaccard({1, 2, 3}, {2, 3, 4}), 2))"),
    (15, "集合求幂集大小。", "def powerset_size(s):\n    return 2 ** len(s)\n\nprint('Powerset:', powerset_size({1, 2, 3}))", "填空幂集大小。", "def powerset_size(s):\n    return 2 ** len(s)\n\nprint('Powerset:', powerset_size({1, 2, 3}))"),
    (16, "集合实现去重排序合并。", "def merge_unique(a, b):\n    return sorted(a | b)\n\nprint(merge_unique({1, 3}, {2, 3, 4, 5}))", "填空合并去重。", "def merge_unique(a, b):\n    return sorted(a | b)\n\nprint(merge_unique({1, 3}, {2, 3, 4, 5}))"),
    (17, "集合求最频繁元素。", "def most_common(nums):\n    counts = {}\n    for n in nums:\n        counts[n] = counts.get(n, 0) + 1\n    return max(counts, key=counts.get)\n\nprint('Mode:', most_common([1, 2, 2, 3, 2]))", "填空众数。", "def most_common(nums):\n    counts = {}\n    for n in nums:\n        counts[n] = counts.get(n, 0) + 1\n    return max(counts, key=counts.get)\n\nprint('Mode:', most_common([1, 2, 2, 3, 2]))"),
    (18, "集合求缺失数字。", "def missing_number(nums):\n    n = len(nums)\n    full = set(range(n + 1))\n    return (full - set(nums)).pop()\n\nprint('Missing:', missing_number([0, 1, 3]))", "填空缺失数。", "def missing_number(nums):\n    n = len(nums)\n    full = set(range(n + 1))\n    return (full - set(nums)).pop()\n\nprint('Missing:', missing_number([0, 1, 3]))"),
    (19, "集合求三元组和。", "def triple_sum(nums, target):\n    result = set()\n    for i in range(len(nums)):\n        for j in range(i + 1, len(nums)):\n            for k in range(j + 1, len(nums)):\n                if nums[i] + nums[j] + nums[k] == target:\n                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))\n    return sorted(result)\n\nprint(triple_sum([1, 2, 3, 4], 6))", "填空三元组。", "def triple_sum(nums, target):\n    result = set()\n    for i in range(len(nums)):\n        for j in range(i + 1, len(nums)):\n            for k in range(j + 1, len(nums)):\n                if nums[i] + nums[j] + nums[k] == target:\n                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))\n    return sorted(result)\n\nprint(triple_sum([1, 2, 3, 4], 6))"),
    (20, "集合求可组成数字。", "def can_make(nums, target):\n    num_set = set(nums)\n    return any(target - n in num_set for n in num_set)\n\nprint('Make:', can_make([3, 5, 1], 8), can_make([3, 5, 1], 9))", "填空组成判断。", "def can_make(nums, target):\n    num_set = set(nums)\n    return any(target - n in num_set for n in num_set)\n\nprint('Make:', can_make([3, 5, 1], 8), can_make([3, 5, 1], 9))"),
    (21, "集合求唯一元素。", "def single(nums):\n    result = 0\n    for n in nums:\n        result ^= n\n    return result\n\nprint('Single:', single([4, 1, 2, 1, 2]))", "填空异或唯一。", "def single(nums):\n    result = 0\n    for n in nums:\n        result ^= n\n    return result\n\nprint('Single:', single([4, 1, 2, 1, 2]))"),
    (22, "集合求两集合最大差。", "def max_diff(a, b):\n    return max(a | b) - min(a | b)\n\nprint('Diff:', max_diff({1, 5, 9}, {3, 7}))", "填空最大差。", "def max_diff(a, b):\n    return max(a | b) - min(a | b)\n\nprint('Diff:', max_diff({1, 5, 9}, {3, 7}))"),
    (23, "集合实现词频过滤。", "def filter_stopwords(words, stopwords):\n    stop = set(stopwords)\n    return [w for w in words if w not in stop]\n\nprint(filter_stopwords([\"a\", \"the\", \"cat\"], [\"a\", \"the\"]))", "填空停用词过滤。", "def filter_stopwords(words, stopwords):\n    stop = set(stopwords)\n    return [w for w in words if w not in stop]\n\nprint(filter_stopwords([\"a\", \"the\", \"cat\"], [\"a\", \"the\"]))"),
    (24, "集合求交集数。", "def intersection_size(a, b):\n    return len(a & b)\n\nprint('Count:', intersection_size({1, 2, 3}, {2, 3, 4}))", "填空交集数。", "def intersection_size(a, b):\n    return len(a & b)\n\nprint('Count:', intersection_size({1, 2, 3}, {2, 3, 4}))"),
    (25, "集合实现双色分组。", "def partition(nums):\n    evens = set()\n    odds = set()\n    for n in nums:\n        if n % 2 == 0:\n            evens.add(n)\n        else:\n            odds.add(n)\n    return sorted(evens), sorted(odds)\n\ne, o = partition([1, 2, 3, 4, 5])\nprint(e, o)", "填空奇偶分组。", "def partition(nums):\n    evens = set()\n    odds = set()\n    for n in nums:\n        if n % 2 == 0:\n            evens.add(n)\n        else:\n            odds.add(n)\n    return sorted(evens), sorted(odds)\n\ne, o = partition([1, 2, 3, 4, 5])\nprint(e, o)"),
    (26, "集合求最大可覆盖区间。", "def covered(nums):\n    num_set = set(nums)\n    return max(len(range(min(nums), max(nums) + 1)) - len(num_set), 0)\n\nprint(covered([1, 2, 4]))", "填空覆盖缺口。", "def covered(nums):\n    num_set = set(nums)\n    return max(len(range(min(nums), max(nums) + 1)) - len(num_set), 0)\n\nprint(covered([1, 2, 4]))"),
    (27, "集合实现对称分组。", "def group_by_parity(nums):\n    groups = {}\n    for n in nums:\n        groups.setdefault(n % 2, set()).add(n)\n    return {k: sorted(v) for k, v in groups.items()}\n\nprint(group_by_parity([1, 2, 3, 4]))", "填空奇偶分组字典。", "def group_by_parity(nums):\n    groups = {}\n    for n in nums:\n        groups.setdefault(n % 2, set()).add(n)\n    return {k: sorted(v) for k, v in groups.items()}\n\nprint(group_by_parity([1, 2, 3, 4]))"),
    (28, "集合求任意差目标。", "def has_diff(nums, diff):\n    num_set = set(nums)\n    return any(n + diff in num_set for n in num_set)\n\nprint('Diff:', has_diff([1, 3, 5], 2), has_diff([1, 3, 5], 1))", "填空差目标。", "def has_diff(nums, diff):\n    num_set = set(nums)\n    return any(n + diff in num_set for n in num_set)\n\nprint('Diff:', has_diff([1, 3, 5], 2), has_diff([1, 3, 5], 1))"),
    (29, "集合求并集最小覆盖。", "def min_cover(sets):\n    union = set()\n    for s in sets:\n        union |= s\n    return len(union)\n\nprint('Cover:', min_cover([{1, 2}, {2, 3}, {4}]))", "填空最小覆盖。", "def min_cover(sets):\n    union = set()\n    for s in sets:\n        union |= s\n    return len(union)\n\nprint('Cover:', min_cover([{1, 2}, {2, 3}, {4}]))"),
    (30, "综合：集合数据分析。", "def analyze(nums):\n    s = set(nums)\n    return len(s), sum(s), max(s) - min(s)\n\nunique_count, unique_sum, span = analyze([1, 2, 2, 5])\nprint(unique_count, unique_sum, span)", "填空集合分析。", "def analyze(nums):\n    s = set(nums)\n    return len(s), sum(s), max(s) - min(s)\n\nunique_count, unique_sum, span = analyze([1, 2, 2, 5])\nprint(unique_count, unique_sum, span)"),
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
