# -*- coding: utf-8 -*-
"""生成 CH03 列表 (Lists) 题库（4 档 × 30 = 120 道）。

id 后缀沿用递进命名：E=超简单 / M=简单 / H=中等 / X=较难。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import gen_chapter  # noqa: E402

CHAPTER = "CH03"
TITLE = "列表 (Lists)"
OUT_DIR = "CH03_Lists"
DIFF = {"E": ("超简单", "⭐"), "M": ("简单", "⭐⭐"),
        "H": ("中等", "⭐⭐⭐"), "X": ("较难", "⭐⭐⭐⭐")}
TOPIC = {"E": TITLE, "M": TITLE, "H": TITLE, "X": TITLE}

EASY = [
    (1, "创建列表并输出。", "nums = [1, 2, 3]\nprint(___)", "print 括号内填 nums。", "nums = [1, 2, 3]\nprint(nums)"),
    (2, "创建空列表并输出。", "empty = []\nprint(___)", "print 括号内填 empty。", "empty = []\nprint(empty)"),
    (3, "用索引访问列表第一个元素。", "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[___])", "索引填 0。", "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[0])"),
    (4, "用负索引访问列表最后一个元素。", "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[___])", "索引填 -1。", "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[-1])"),
    (5, "用切片截取列表中间部分。", "nums = [1, 2, 3, 4, 5]\nprint(nums[1:___])", "结束索引填 4。", "nums = [1, 2, 3, 4, 5]\nprint(nums[1:4])"),
    (6, "用切片截取列表尾部。", "nums = [1, 2, 3, 4, 5]\nprint(nums[___])", "切片填 3:。", "nums = [1, 2, 3, 4, 5]\nprint(nums[3:])"),
    (7, "用切片步长隔一个取一个。", "nums = [1, 2, 3, 4, 5]\nprint(nums[___])", "切片填 ::2。", "nums = [1, 2, 3, 4, 5]\nprint(nums[::2])"),
    (8, "用 len() 获取列表长度。", "nums = [1, 2, 3, 4, 5]\nprint(len(___))", "len 括号内填 nums。", "nums = [1, 2, 3, 4, 5]\nprint(len(nums))"),
    (9, "用 append() 在末尾添加元素。", "nums = [1, 2, 3, 4, 5]\nnums.append(___)\nprint(nums)", "添加数字 6。", "nums = [1, 2, 3, 4, 5]\nnums.append(6)\nprint(nums)"),
    (10, "用 pop() 删除末尾元素。", "nums = [1, 2, 3, 4, 5]\nnums.pop()\nprint(nums)", "填空 nums.pop()。", "nums = [1, 2, 3, 4, 5]\nnums.pop()\nprint(nums)"),
    (11, "用 pop() 删除指定索引的元素。", "nums = [1, 2, 3, 4, 5]\nnums.pop(___)\nprint(nums)", "索引填 0。", "nums = [1, 2, 3, 4, 5]\nnums.pop(0)\nprint(nums)"),
    (12, "用 insert() 在开头插入元素。", "nums = [1, 2, 3, 4, 5]\nnums.insert(0, ___)\nprint(nums)", "插入数字 0。", "nums = [1, 2, 3, 4, 5]\nnums.insert(0, 0)\nprint(nums)"),
    (13, "用 remove() 删除指定元素。", "nums = [1, 2, 3, 4, 5]\nnums.remove(___)\nprint(nums)", "删除数字 3。", "nums = [1, 2, 3, 4, 5]\nnums.remove(3)\nprint(nums)"),
    (14, "按索引修改列表元素。", "nums = [1, 2, 3, 4, 5]\nnums[___] = 100\nprint(nums)", "索引填 0。", "nums = [1, 2, 3, 4, 5]\nnums[0] = 100\nprint(nums)"),
    (15, "创建字符串列表并输出。", "colors = [\"red\", \"green\"]\nprint(colors)", "填空 colors。", "colors = [\"red\", \"green\"]\nprint(colors)"),
    (16, "创建混合类型列表并输出。", "mixed = [1, \"two\", 3.0]\nprint(mixed)", "填空 mixed。", "mixed = [1, \"two\", 3.0]\nprint(mixed)"),
    (17, "用乘法快速生成重复元素的列表。", "print([___] * 4)", "填 0。", "print([0] * 4)"),
    (18, "用 + 拼接两个列表。", "a = [5, 6]\nb = [7, 8]\nprint(___ + ___)", "依次填 a、b。", "a = [5, 6]\nb = [7, 8]\nprint(a + b)"),
    (19, "用 max() 求列表最大值。", "nums = [4, 9, 2]\nprint(max(___))", "填 nums。", "nums = [4, 9, 2]\nprint(max(nums))"),
    (20, "用 min() 求列表最小值。", "nums = [4, 9, 5]\nprint(min(___))", "填 nums。", "nums = [4, 9, 5]\nprint(min(nums))"),
    (21, "用 sum() 求列表总和。", "nums = [4, 9, 2]\nprint(sum(___))", "填 nums。", "nums = [4, 9, 2]\nprint(sum(nums))"),
    (22, "用 count() 统计元素出现次数。", "nums = [1, 2, 2, 3]\nprint(nums.count(___))", "统计数字 2。", "nums = [1, 2, 2, 3]\nprint(nums.count(2))"),
    (23, "用 index() 查找元素的位置。", "nums = [1, 2, 2, 3]\nprint(nums.index(___))", "查找数字 2。", "nums = [1, 2, 2, 3]\nprint(nums.index(2))"),
    (24, "用 in 判断元素是否在列表中。", "nums = [1, 2, 3]\nprint(___ in nums)", "判断数字 2。", "nums = [1, 2, 3]\nprint(2 in nums)"),
    (25, "用 for 循环遍历列表逐行输出。", "for n in [1, 2, 3]:\n    print(___)\n", "输出变量 n。", "for n in [1, 2, 3]:\n    print(n)"),
    (26, "用切片反转列表。", "nums = [1, 2, 3]\nprint(nums[___])", "切片填 ::-1。", "nums = [1, 2, 3]\nprint(nums[::-1])"),
    (27, "用 sorted() 返回排序后的新列表。", "nums = [5, 3, 4]\nprint(sorted(___))", "填 nums。", "nums = [5, 3, 4]\nprint(sorted(nums))"),
    (28, "用 sort() 原地排序列表。", "nums = [2, 1]\nnums.sort()\nprint(___)", "print 括号内填 nums。", "nums = [2, 1]\nnums.sort()\nprint(nums)"),
    (29, "用 reverse() 原地反转列表。", "nums = [1, 2]\nnums.reverse()\nprint(___)", "print 括号内填 nums。", "nums = [1, 2]\nnums.reverse()\nprint(nums)"),
    (30, "访问嵌套列表中的元素。", "matrix = [[1, 2], [3, 4]]\nprint(matrix[___][0])", "外层索引填 1。", "matrix = [[1, 2], [3, 4]]\nprint(matrix[1][0])"),
]

SIMPLE = [
    (1, "用循环往列表中添加元素。", "nums = []\nfor i in range(0, 10, 3):\n    nums.append(i)\nprint(nums)", "填空 append(i)。", "nums = []\nfor i in range(0, 10, 3):\n    nums.append(i)\nprint(nums)"),
    (2, "用列表推导式生成平方数列表。", "squares = [n * n for n in range(1, 6)]\nprint(squares)", "填空 n * n。", "squares = [n * n for n in range(1, 6)]\nprint(squares)"),
    (3, "输出列表的和与长度。", "nums = [2, 4, 6]\nprint(sum(nums), len(nums))", "填空 sum(nums)、len(nums)。", "nums = [2, 4, 6]\nprint(sum(nums), len(nums))"),
    (4, "用切片复制整个列表。", "nums = [7, 8, 9]\ncopy = nums[:]\nprint(copy)", "填空 nums[:]。", "nums = [7, 8, 9]\ncopy = nums[:]\nprint(copy)"),
    (5, "用 del 删除指定索引元素。", "nums = [1, 2, 3]\ndel nums[1]\nprint(nums)", "填空 del nums[1]。", "nums = [1, 2, 3]\ndel nums[1]\nprint(nums)"),
    (6, "用 extend() 扩展列表。", "a = [1, 2]\na.extend([9, 8])\nprint(a)", "填空 a.extend([9, 8])。", "a = [1, 2]\na.extend([9, 8])\nprint(a)"),
    (7, "修改并插入列表元素。", "nums = [1, 2, 3]\nnums[1] = 20\nnums.insert(2, 15)\nprint(nums)", "填空修改与插入。", "nums = [1, 2, 3]\nnums[1] = 20\nnums.insert(2, 15)\nprint(nums)"),
    (8, "用循环筛选出偶数。", "nums = [1, 2, 3, 4, 5]\nevens = []\nfor n in nums:\n    if n % 2 == 0:\n        evens.append(n)\nprint(evens)", "填空条件与 append。", "nums = [1, 2, 3, 4, 5]\nevens = []\nfor n in nums:\n    if n % 2 == 0:\n        evens.append(n)\nprint(evens)"),
    (9, "用带条件的列表推导式生成奇数。", "odds = [n for n in range(1, 11) if n % 2 == 1]\nprint(odds)", "填空推导式。", "odds = [n for n in range(1, 11) if n % 2 == 1]\nprint(odds)"),
    (10, "把列表中的字符串转大写。", "words = [\"hi\", \"bye\"]\nprint([w.upper() for w in words])", "填空 w.upper()。", "words = [\"hi\", \"bye\"]\nprint([w.upper() for w in words])"),
    (11, "输出每个单词的长度列表。", "words = [\"hello\", \"hi\", \"hey\"]\nprint([len(w) for w in words])", "填空 len(w)。", "words = [\"hello\", \"hi\", \"hey\"]\nprint([len(w) for w in words])"),
    (12, "访问嵌套列表的两个元素。", "matrix = [[1, 2], [3, 4]]\nprint(matrix[0][1], matrix[1][0])", "填空两处索引。", "matrix = [[1, 2], [3, 4]]\nprint(matrix[0][1], matrix[1][0])"),
    (13, "用 reversed() 反转列表并转为列表。", "nums = [1, 2, 3, 4]\nprint(list(reversed(nums)))", "填空 reversed(nums)。", "nums = [1, 2, 3, 4]\nprint(list(reversed(nums)))"),
    (14, "用 all() 判断是否全部为正数。", "print(\"All positive:\", all(n > 0 for n in [1, 2, -3]))", "填空 n > 0。", "print(\"All positive:\", all(n > 0 for n in [1, 2, -3]))"),
    (15, "用索引访问并相加列表元素。", "nums = [10, 20, 30]\nprint(nums[0] + nums[1] + nums[2])", "填空三处索引。", "nums = [10, 20, 30]\nprint(nums[0] + nums[1] + nums[2])"),
    (16, "用 enumerate() 同时输出索引和元素。", "fruits = [\"a\", \"b\", \"c\"]\nfor i, f in enumerate(fruits):\n    print(i, f)", "填空 enumerate(fruits)。", "fruits = [\"a\", \"b\", \"c\"]\nfor i, f in enumerate(fruits):\n    print(i, f)"),
    (17, "用 zip() 对应相加两个列表。", "a = [1, 2, 3]\nb = [4, 5, 6]\nprint([x + y for x, y in zip(a, b)])", "填空 zip(a, b)。", "a = [1, 2, 3]\nb = [4, 5, 6]\nprint([x + y for x, y in zip(a, b)])"),
    (18, "用 join() 拼接字符串列表。", "words = [\"Py\", \"Quest\"]\nprint(\"\".join(words))", "填空 join(words)。", "words = [\"Py\", \"Quest\"]\nprint(\"\".join(words))"),
    (19, "用 join() 把数字列表拼成字符串。", "nums = [1, 2, 3]\nprint(\"-\".join(map(str, nums)))", "填空 map(str, nums)。", "nums = [1, 2, 3]\nprint(\"-\".join(map(str, nums)))"),
    (20, "用 set 去重后求和。", "nums = [1, 2, 2, 3, 5]\nprint(sum(set(nums)))", "填空 set(nums)。", "nums = [1, 2, 2, 3, 5]\nprint(sum(set(nums)))"),
    (21, "用 sorted() 降序排序。", "nums = [5, 1, 3]\nprint(sorted(nums, reverse=True))", "填空 reverse=True。", "nums = [5, 1, 3]\nprint(sorted(nums, reverse=True))"),
    (22, "用列表推导式生成二维网格。", "grid = [[0] * 3 for _ in range(2)]\nprint(grid)", "填空 [0] * 3。", "grid = [[0] * 3 for _ in range(2)]\nprint(grid)"),
    (23, "用切片替换列表片段。", "nums = [1, 2, 3, 4, 5]\nnums[1:3] = [20, 30]\nprint(nums)", "填空切片替换。", "nums = [1, 2, 3, 4, 5]\nnums[1:3] = [20, 30]\nprint(nums)"),
    (24, "清空列表并输出长度。", "nums = [1, 2, 3]\nnums.clear()\nprint(nums, len(nums))", "填空 nums.clear()。", "nums = [1, 2, 3]\nnums.clear()\nprint(nums, len(nums))"),
    (25, "求列表中偶数的和。", "nums = [1, 2, 3, 4, 5, 6]\nprint(sum(n for n in nums if n % 2 == 0))", "填空生成器表达式。", "nums = [1, 2, 3, 4, 5, 6]\nprint(sum(n for n in nums if n % 2 == 0))"),
    (26, "找最大值所在的位置。", "nums = [5, 9, 3]\nprint(\"Index of max:\", nums.index(max(nums)))", "填空 max(nums)。", "nums = [5, 9, 3]\nprint(\"Index of max:\", nums.index(max(nums)))"),
    (27, "把字符串转成字符列表。", "s = \"abc\"\nprint(list(s))", "填空 list(s)。", "s = \"abc\"\nprint(list(s))"),
    (28, "修改嵌套列表中的元素。", "matrix = [[1, 2], [3, 4]]\nmatrix[1][1] = 40\nprint(matrix)", "填空修改嵌套元素。", "matrix = [[1, 2], [3, 4]]\nmatrix[1][1] = 40\nprint(matrix)"),
    (29, "交换列表首尾元素。", "nums = [1, 2, 3, 4]\nnums[0], nums[-1] = nums[-1], nums[0]\nprint(nums)", "填空首尾交换。", "nums = [1, 2, 3, 4]\nnums[0], nums[-1] = nums[-1], nums[0]\nprint(nums)"),
    (30, "用切片步长取偶数索引元素。", "nums = [10, 20, 30, 40]\nprint(nums[::2])", "切片填 ::2。", "nums = [10, 20, 30, 40]\nprint(nums[::2])"),
]

MEDIUM = [
    (1, "统计分数列表的最大、最小和平均值。", "scores = [88, 92, 76, 95]\nprint(\"Max:\", max(scores))\nprint(\"Min:\", min(scores))\nprint(\"Avg:\", sum(scores) / len(scores))", "填空 max/min/sum 统计。", "scores = [88, 92, 76, 95]\nprint(\"Max:\", max(scores))\nprint(\"Min:\", min(scores))\nprint(\"Avg:\", sum(scores) / len(scores))"),
    (2, "把列表向左旋转两位。", "nums = [1, 2, 3, 4, 5]\nprint(nums[2:] + nums[:2])", "填空切片拼接。", "nums = [1, 2, 3, 4, 5]\nprint(nums[2:] + nums[:2])"),
    (3, "去除列表中的重复元素（保持顺序）。", "nums = [3, 1, 2, 3, 1]\nseen = []\nfor n in nums:\n    if n not in seen:\n        seen.append(n)\nprint(seen)", "填空去重逻辑。", "nums = [3, 1, 2, 3, 1]\nseen = []\nfor n in nums:\n    if n not in seen:\n        seen.append(n)\nprint(seen)"),
    (4, "统计列表中每个元素的出现次数。", "nums = [1, 2, 2, 3, 3, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)", "填空计数更新。", "nums = [1, 2, 2, 3, 3, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nprint(counts)"),
    (5, "转置一个 2x3 矩阵。", "matrix = [[1, 2, 3], [4, 5, 6]]\ntransposed = [[matrix[j][i] for j in range(2)] for i in range(3)]\nprint(transposed)", "填空转置推导。", "matrix = [[1, 2, 3], [4, 5, 6]]\ntransposed = [[matrix[j][i] for j in range(2)] for i in range(3)]\nprint(transposed)"),
    (6, "在有序列表中二分查找目标值。", "nums = [1, 3, 5, 7, 9]\ntarget = 7\nlow, high = 0, len(nums) - 1\nfound = False\nwhile low <= high:\n    mid = (low + high) // 2\n    if nums[mid] == target:\n        found = True\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\nprint(\"Found:\", found, \"at index\", mid)", "填空二分逻辑。", "nums = [1, 3, 5, 7, 9]\ntarget = 7\nlow, high = 0, len(nums) - 1\nfound = False\nwhile low <= high:\n    mid = (low + high) // 2\n    if nums[mid] == target:\n        found = True\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\nprint(\"Found:\", found, \"at index\", mid)"),
    (7, "用选择排序给列表排序。", "nums = [5, 3, 8, 1]\nfor i in range(len(nums)):\n    m = i\n    for j in range(i + 1, len(nums)):\n        if nums[j] < nums[m]:\n            m = j\n    nums[i], nums[m] = nums[m], nums[i]\nprint(nums)", "填空选择排序。", "nums = [5, 3, 8, 1]\nfor i in range(len(nums)):\n    m = i\n    for j in range(i + 1, len(nums)):\n        if nums[j] < nums[m]:\n            m = j\n    nums[i], nums[m] = nums[m], nums[i]\nprint(nums)"),
    (8, "用插入排序给列表排序。", "nums = [9, 2, 7, 4]\nfor i in range(1, len(nums)):\n    key = nums[i]\n    j = i - 1\n    while j >= 0 and nums[j] > key:\n        nums[j + 1] = nums[j]\n        j -= 1\n    nums[j + 1] = key\nprint(nums)", "填空插入排序。", "nums = [9, 2, 7, 4]\nfor i in range(1, len(nums)):\n    key = nums[i]\n    j = i - 1\n    while j >= 0 and nums[j] > key:\n        nums[j + 1] = nums[j]\n        j -= 1\n    nums[j + 1] = key\nprint(nums)"),
    (9, "合并两个有序列表。", "a = [1, 4, 7]\nb = [2, 5]\nmerged = sorted(a + b)\nprint(merged)", "填空 a + b 与 sorted。", "a = [1, 4, 7]\nb = [2, 5]\nmerged = sorted(a + b)\nprint(merged)"),
    (10, "找出列表中第二大的数。", "nums = [4, 9, 7, 9, 2]\nprint(sorted(set(nums))[-2])", "填空去重排序取倒数第二个。", "nums = [4, 9, 7, 9, 2]\nprint(sorted(set(nums))[-2])"),
    (11, "把列表向右旋转一位。", "nums = [1, 2, 3, 4, 5]\nprint([nums[-1]] + nums[:-1])", "填空右移拼接。", "nums = [1, 2, 3, 4, 5]\nprint([nums[-1]] + nums[:-1])"),
    (12, "把列表分成奇数和偶数两组。", "nums = [1, 2, 3, 4, 5, 6]\nevens = [n for n in nums if n % 2 == 0]\nodds = [n for n in nums if n % 2 == 1]\nprint(evens, odds)", "填空两组推导式。", "nums = [1, 2, 3, 4, 5, 6]\nevens = [n for n in nums if n % 2 == 0]\nodds = [n for n in nums if n % 2 == 1]\nprint(evens, odds)"),
    (13, "比较两个列表的内容与身份。", "a = [1, 2, 3]\nb = [1, 2, 3]\nprint(a == b, a is b)", "填空 == 与 is 比较。", "a = [1, 2, 3]\nb = [1, 2, 3]\nprint(a == b, a is b)"),
    (14, "判断元素是否存在于列表中。", "nums = [1, 2, 3]\nprint(0 in nums, 5 in nums)", "填空两个 in 判断。", "nums = [1, 2, 3]\nprint(0 in nums, 5 in nums)"),
    (15, "计算列表的前缀和。", "nums = [1, 2, 3, 4]\nprefix = []\ntotal = 0\nfor n in nums:\n    total += n\n    prefix.append(total)\nprint(prefix)", "填空累加与添加。", "nums = [1, 2, 3, 4]\nprefix = []\ntotal = 0\nfor n in nums:\n    total += n\n    prefix.append(total)\nprint(prefix)"),
    (16, "求矩阵主对角线元素之和。", "matrix = [[2, 3], [4, 9]]\nprint(\"Diagonal sum:\", matrix[0][0] + matrix[1][1])", "填空对角线求和。", "matrix = [[2, 3], [4, 9]]\nprint(\"Diagonal sum:\", matrix[0][0] + matrix[1][1])"),
    (17, "把 range 转成列表。", "print(list(range(5)))", "填空 list(range(5))。", "print(list(range(5)))"),
    (18, "按字符串长度排序列表。", "words = [\"bb\", \"a\", \"ccc\"]\nprint(sorted(words, key=len))", "填空 key=len。", "words = [\"bb\", \"a\", \"ccc\"]\nprint(sorted(words, key=len))"),
    (19, "格式化输出列表中的每个元素。", "nums = [1, 2, 3]\nfor n in nums:\n    print(f\"Item: {n}\")", "填空 f-string。", "nums = [1, 2, 3]\nfor n in nums:\n    print(f\"Item: {n}\")"),
    (20, "计算列表中所有元素的乘积。", "nums = [2, 3, 4]\nproduct = 1\nfor n in nums:\n    product *= n\nprint(product)", "填空累乘。", "nums = [2, 3, 4]\nproduct = 1\nfor n in nums:\n    product *= n\nprint(product)"),
    (21, "找出列表中重复出现的元素。", "nums = [1, 3, 3, 5, 5, 5]\nprint([n for n in sorted(set(nums)) if nums.count(n) > 1])", "填空去重筛选。", "nums = [1, 3, 3, 5, 5, 5]\nprint([n for n in sorted(set(nums)) if nums.count(n) > 1])"),
    (22, "把二维列表扁平化。", "matrix = [[7, 8], [9, 10]]\nflat = [n for row in matrix for n in row]\nprint(flat)", "填空嵌套推导。", "matrix = [[7, 8], [9, 10]]\nflat = [n for row in matrix for n in row]\nprint(flat)"),
    (23, "把列表首尾配对求和。", "nums = [1, 2, 3, 4]\nprint([nums[i] + nums[-1 - i] for i in range(len(nums) // 2)])", "填空配对索引。", "nums = [1, 2, 3, 4]\nprint([nums[i] + nums[-1 - i] for i in range(len(nums) // 2)])"),
    (24, "过滤掉列表中的 None。", "items = [None, \"a\", None, \"b\"]\nprint([x for x in items if x is not None])", "填空过滤条件。", "items = [None, \"a\", None, \"b\"]\nprint([x for x in items if x is not None])"),
    (25, "筛选平方大于 10 的元素。", "nums = [1, 2, 3, 4, 5]\nprint([n * n for n in nums if n * n > 10])", "填空筛选与平方。", "nums = [1, 2, 3, 4, 5]\nprint([n * n for n in nums if n * n > 10])"),
    (26, "输出每个单词的长度列表。", "words = [\"hello\", \"world\", \"python\"]\nprint([len(w) for w in words])", "填空 len(w)。", "words = [\"hello\", \"world\", \"python\"]\nprint([len(w) for w in words])"),
    (27, "找出列表 A 中不在列表 B 的元素。", "a = [10, 20, 30, 40, 50]\nb = [20, 40]\nprint([x for x in a if x not in b])", "填空差集推导。", "a = [10, 20, 30, 40, 50]\nb = [20, 40]\nprint([x for x in a if x not in b])"),
    (28, "输出每个元素及其出现次数。", "nums = [1, 1, 2]\nfor n in sorted(set(nums)):\n    print(n, nums.count(n))", "填空遍历去重集合。", "nums = [1, 1, 2]\nfor n in sorted(set(nums)):\n    print(n, nums.count(n))"),
    (29, "求反转列表的和。", "nums = [1, 2, 3, 4]\nprint(\"Sum of reversed:\", sum(nums[::-1]))", "填空反转切片。", "nums = [1, 2, 3, 4]\nprint(\"Sum of reversed:\", sum(nums[::-1]))"),
    (30, "用 enumerate() 输出索引和值。", "nums = [10, 20, 30]\nfor i, n in enumerate(nums):\n    print(i, n)", "填空 enumerate(nums)。", "nums = [10, 20, 30]\nfor i, n in enumerate(nums):\n    print(i, n)"),
]

HARD = [
    (1, "演示冒泡排序的每轮结果。", "nums = [5, 3, 8, 1]\nfor i in range(len(nums) - 1):\n    for j in range(len(nums) - 1 - i):\n        if nums[j] > nums[j + 1]:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\n    print(\"Pass\", i + 1, nums)", "填空比较与交换。", "nums = [5, 3, 8, 1]\nfor i in range(len(nums) - 1):\n    for j in range(len(nums) - 1 - i):\n        if nums[j] > nums[j + 1]:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\n    print(\"Pass\", i + 1, nums)"),
    (2, "用递归实现快速排序。", "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    left = [x for x in arr[1:] if x <= pivot]\n    right = [x for x in arr[1:] if x > pivot]\n    return quicksort(left) + [pivot] + quicksort(right)\n\nprint(quicksort([5, 3, 8, 1, 2]))", "填空递归分区。", "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    left = [x for x in arr[1:] if x <= pivot]\n    right = [x for x in arr[1:] if x > pivot]\n    return quicksort(left) + [pivot] + quicksort(right)\n\nprint(quicksort([5, 3, 8, 1, 2]))"),
    (3, "用递归实现归并排序。", "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] < right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nprint(merge_sort([8, 3, 6, 1, 7, 2]))", "填空归并逻辑。", "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] < right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nprint(merge_sort([8, 3, 6, 1, 7, 2]))"),
    (4, "演示二分查找的查找过程。", "nums = [1, 3, 5, 7, 9, 11]\ntarget = 9\nlow, high = 0, len(nums) - 1\nwhile low <= high:\n    mid = (low + high) // 2\n    print(\"Check index\", mid, \"->\", nums[mid])\n    if nums[mid] == target:\n        print(\"Found at\", mid)\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1", "填空中点与比较。", "nums = [1, 3, 5, 7, 9, 11]\ntarget = 9\nlow, high = 0, len(nums) - 1\nwhile low <= high:\n    mid = (low + high) // 2\n    print(\"Check index\", mid, \"->\", nums[mid])\n    if nums[mid] == target:\n        print(\"Found at\", mid)\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1"),
    (5, "生成 3x3 螺旋矩阵。", "n = 3\nmatrix = [[0] * n for _ in range(n)]\ntop, bottom, left, right = 0, n - 1, 0, n - 1\nnum = 1\nwhile top <= bottom and left <= right:\n    for j in range(left, right + 1):\n        matrix[top][j] = num\n        num += 1\n    top += 1\n    for i in range(top, bottom + 1):\n        matrix[i][right] = num\n        num += 1\n    right -= 1\n    for j in range(right, left - 1, -1):\n        matrix[bottom][j] = num\n        num += 1\n    bottom -= 1\n    for i in range(bottom, top - 1, -1):\n        matrix[i][left] = num\n        num += 1\n    left += 1\nfor row in matrix:\n    print(row)", "填空螺旋填充。", "n = 3\nmatrix = [[0] * n for _ in range(n)]\ntop, bottom, left, right = 0, n - 1, 0, n - 1\nnum = 1\nwhile top <= bottom and left <= right:\n    for j in range(left, right + 1):\n        matrix[top][j] = num\n        num += 1\n    top += 1\n    for i in range(top, bottom + 1):\n        matrix[i][right] = num\n        num += 1\n    right -= 1\n    for j in range(right, left - 1, -1):\n        matrix[bottom][j] = num\n        num += 1\n    bottom -= 1\n    for i in range(bottom, top - 1, -1):\n        matrix[i][left] = num\n        num += 1\n    left += 1\nfor row in matrix:\n    print(row)"),
    (6, "求最大子数组和（Kadane 算法）。", "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\nmax_sum = nums[0]\ncur = 0\nfor n in nums:\n    cur = max(n, cur + n)\n    max_sum = max(max_sum, cur)\nprint(max_sum)", "填空动态规划转移。", "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\nmax_sum = nums[0]\ncur = 0\nfor n in nums:\n    cur = max(n, cur + n)\n    max_sum = max(max_sum, cur)\nprint(max_sum)"),
    (7, "找出两数之和等于目标值的索引。", "nums = [2, 7, 11, 15]\ntarget = 9\nresult = []\nfor i in range(len(nums)):\n    for j in range(i + 1, len(nums)):\n        if nums[i] + nums[j] == target:\n            result = [i, j]\nprint(result)", "填空双重循环。", "nums = [2, 7, 11, 15]\ntarget = 9\nresult = []\nfor i in range(len(nums)):\n    for j in range(i + 1, len(nums)):\n        if nums[i] + nums[j] == target:\n            result = [i, j]\nprint(result)"),
    (8, "把数组循环右移 k 位。", "nums = [1, 2, 3, 4, 5]\nk = 2\nk = k % len(nums)\nprint(nums[-k:] + nums[:-k])", "填空切片旋转。", "nums = [1, 2, 3, 4, 5]\nk = 2\nk = k % len(nums)\nprint(nums[-k:] + nums[:-k])"),
    (9, "输出出现次数最多的两个单词。", "words = [\"a\", \"b\", \"a\", \"c\", \"a\", \"b\"]\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2]:\n    print(w, c)", "填空频次统计与排序。", "words = [\"a\", \"b\", \"a\", \"c\", \"a\", \"b\"]\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nfor w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:2]:\n    print(w, c)"),
    (10, "模拟约瑟夫环的出列顺序。", "people = list(range(1, 8))\nk = 3\nidx = 0\norder = []\nwhile people:\n    idx = (idx + k - 1) % len(people)\n    order.append(people.pop(idx))\nprint(order)", "填空环形淘汰。", "people = list(range(1, 8))\nk = 3\nidx = 0\norder = []\nwhile people:\n    idx = (idx + k - 1) % len(people)\n    order.append(people.pop(idx))\nprint(order)"),
    (11, "把列表按指定大小分块。", "nums = [1, 2, 3, 4, 5, 6, 7]\nsize = 3\nchunks = [nums[i:i + size] for i in range(0, len(nums), size)]\nprint(chunks)", "填空切片分块。", "nums = [1, 2, 3, 4, 5, 6, 7]\nsize = 3\nchunks = [nums[i:i + size] for i in range(0, len(nums), size)]\nprint(chunks)"),
    (12, "手写合并两个有序列表。", "a = [1, 3, 9]\nb = [2, 4]\nmerged = []\ni = j = 0\nwhile i < len(a) and j < len(b):\n    if a[i] < b[j]:\n        merged.append(a[i])\n        i += 1\n    else:\n        merged.append(b[j])\n        j += 1\nmerged.extend(a[i:])\nmerged.extend(b[j:])\nprint(merged)", "填空双指针合并。", "a = [1, 3, 9]\nb = [2, 4]\nmerged = []\ni = j = 0\nwhile i < len(a) and j < len(b):\n    if a[i] < b[j]:\n        merged.append(a[i])\n        i += 1\n    else:\n        merged.append(b[j])\n        j += 1\nmerged.extend(a[i:])\nmerged.extend(b[j:])\nprint(merged)"),
    (13, "用列表生成杨辉三角前 5 行。", "rows = 5\ntriangle = []\nfor i in range(rows):\n    row = [1] * (i + 1)\n    for j in range(1, i):\n        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]\n    triangle.append(row)\nprint(triangle)", "填空杨辉三角递推。", "rows = 5\ntriangle = []\nfor i in range(rows):\n    row = [1] * (i + 1)\n    for j in range(1, i):\n        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]\n    triangle.append(row)\nprint(triangle)"),
    (14, "生成 3x3 乘法表矩阵。", "n = 3\nmatrix = [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]\nfor row in matrix:\n    print(row)", "填空乘法推导。", "n = 3\nmatrix = [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]\nfor row in matrix:\n    print(row)"),
    (15, "用异或找出只出现一次的数字。", "nums = [8, 1, 2, 1, 2]\nresult = 0\nfor n in nums:\n    result ^= n\nprint(result)", "填空异或累积。", "nums = [8, 1, 2, 1, 2]\nresult = 0\nfor n in nums:\n    result ^= n\nprint(result)"),
    (16, "用栈检查括号是否匹配（不匹配样例）。", "s = \"{[()]\"\nstack = []\npairs = {\")\": \"(\", \"]\": \"[\", \"}\": \"{\"}\nok = True\nfor ch in s:\n    if ch in \"([{\":\n        stack.append(ch)\n    elif not stack or stack.pop() != pairs[ch]:\n        ok = False\n        break\nprint(ok and not stack)", "填空栈匹配。", "s = \"{[()]\"\nstack = []\npairs = {\")\": \"(\", \"]\": \"[\", \"}\": \"{\"}\nok = True\nfor ch in s:\n    if ch in \"([{\":\n        stack.append(ch)\n    elif not stack or stack.pop() != pairs[ch]:\n        ok = False\n        break\nprint(ok and not stack)"),
    (17, "求逆波兰表达式 5 5 + 的值。", "tokens = [\"5\", \"5\", \"+\"]\nstack = []\nfor t in tokens:\n    if t in \"+-*/\":\n        b = stack.pop()\n        a = stack.pop()\n        if t == \"+\":\n            stack.append(a + b)\n        elif t == \"-\":\n            stack.append(a - b)\n        elif t == \"*\":\n            stack.append(a * b)\n        else:\n            stack.append(a // b)\n    else:\n        stack.append(int(t))\nprint(stack[0])", "填空运算求值。", "tokens = [\"5\", \"5\", \"+\"]\nstack = []\nfor t in tokens:\n    if t in \"+-*/\":\n        b = stack.pop()\n        a = stack.pop()\n        if t == \"+\":\n            stack.append(a + b)\n        elif t == \"-\":\n            stack.append(a - b)\n        elif t == \"*\":\n            stack.append(a * b)\n        else:\n            stack.append(a // b)\n    else:\n        stack.append(int(t))\nprint(stack[0])"),
    (18, "求列表中最大的两数乘积。", "nums = [3, 5, 2, 7, 4]\nsorted_nums = sorted(nums)\nprint(sorted_nums[-1] * sorted_nums[-2])", "填空排序取最大两数。", "nums = [3, 5, 2, 7, 4]\nsorted_nums = sorted(nums)\nprint(sorted_nums[-1] * sorted_nums[-2])"),
    (19, "用单调栈求下一个更大元素。", "nums = [2, 1, 4, 3]\nresult = [-1] * len(nums)\nstack = []\nfor i in range(len(nums)):\n    while stack and nums[stack[-1]] < nums[i]:\n        result[stack.pop()] = nums[i]\n    stack.append(i)\nprint(result)", "填空单调栈。", "nums = [2, 1, 4, 3]\nresult = [-1] * len(nums)\nstack = []\nfor i in range(len(nums)):\n    while stack and nums[stack[-1]] < nums[i]:\n        result[stack.pop()] = nums[i]\n    stack.append(i)\nprint(result)"),
    (20, "求 4x4 网格的路径数（只能向右向下）。", "m, n = 4, 4\ndp = [[1] * n for _ in range(m)]\nfor i in range(1, m):\n    for j in range(1, n):\n        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]\nprint(dp[m - 1][n - 1])", "填空动态规划。", "m, n = 4, 4\ndp = [[1] * n for _ in range(m)]\nfor i in range(1, m):\n    for j in range(1, n):\n        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]\nprint(dp[m - 1][n - 1])"),
    (21, "求数组中最长连续序列的长度。", "nums = [100, 4, 200, 1, 3, 2]\nnum_set = set(nums)\nlongest = 0\nfor n in num_set:\n    if n - 1 not in num_set:\n        length = 1\n        while n + length in num_set:\n            length += 1\n        longest = max(longest, length)\nprint(\"Longest:\", longest)", "填空集合查找。", "nums = [100, 4, 200, 1, 3, 2]\nnum_set = set(nums)\nlongest = 0\nfor n in num_set:\n    if n - 1 not in num_set:\n        length = 1\n        while n + length in num_set:\n            length += 1\n        longest = max(longest, length)\nprint(\"Longest:\", longest)"),
    (22, "用双指针在有序列表中找两数之和。", "nums = [1, 2, 4, 6, 8]\ntarget = 10\nleft, right = 0, len(nums) - 1\nresult = None\nwhile left < right:\n    total = nums[left] + nums[right]\n    if total == target:\n        result = [left, right]\n        break\n    elif total < target:\n        left += 1\n    else:\n        right -= 1\nprint(result)", "填空双指针移动。", "nums = [1, 2, 4, 6, 8]\ntarget = 10\nleft, right = 0, len(nums) - 1\nresult = None\nwhile left < right:\n    total = nums[left] + nums[right]\n    if total == target:\n        result = [left, right]\n        break\n    elif total < target:\n        left += 1\n    else:\n        right -= 1\nprint(result)"),
    (23, "删除列表中所有指定值。", "nums = [1, 2, 3, 2, 4, 2]\nvalue = 2\nresult = [x for x in nums if x != value]\nprint(result)", "填空过滤删除。", "nums = [1, 2, 3, 2, 4, 2]\nvalue = 2\nresult = [x for x in nums if x != value]\nprint(result)"),
    (24, "求买卖股票的最大利润（持续下跌样例）。", "prices = [7, 6, 4, 3, 1]\nmin_price = prices[0]\nmax_profit = 0\nfor p in prices:\n    min_price = min(min_price, p)\n    max_profit = max(max_profit, p - min_price)\nprint(max_profit)", "填空贪心更新。", "prices = [7, 6, 4, 3, 1]\nmin_price = prices[0]\nmax_profit = 0\nfor p in prices:\n    min_price = min(min_price, p)\n    max_profit = max(max_profit, p - min_price)\nprint(max_profit)"),
    (25, "求矩阵副对角线元素之和。", "matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]\nn = 3\nprint(sum(matrix[i][n - 1 - i] for i in range(n)))", "填空副对角线索引。", "matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]\nn = 3\nprint(sum(matrix[i][n - 1 - i] for i in range(n)))"),
    (26, "用递归扁平化多层嵌套列表。", "def flatten(lst):\n    result = []\n    for item in lst:\n        if isinstance(item, list):\n            result.extend(flatten(item))\n        else:\n            result.append(item)\n    return result\n\nprint(flatten([1, [2, [3, 4]], 5]))", "填空递归扁平化。", "def flatten(lst):\n    result = []\n    for item in lst:\n        if isinstance(item, list):\n            result.extend(flatten(item))\n        else:\n            result.append(item)\n    return result\n\nprint(flatten([1, [2, [3, 4]], 5]))"),
    (27, "判断列表是否回文并比较首尾。", "nums = [1, 2, 3, 2, 1]\nprint(nums == nums[::-1], nums[0] == nums[-1])", "填空反转比较。", "nums = [1, 2, 3, 2, 1]\nprint(nums == nums[::-1], nums[0] == nums[-1])"),
    (28, "合并重叠区间。", "intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]\nintervals.sort()\nmerged = []\nfor start, end in intervals:\n    if not merged or start > merged[-1][1]:\n        merged.append([start, end])\n    else:\n        merged[-1][1] = max(merged[-1][1], end)\nprint(merged)", "填空区间合并。", "intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]\nintervals.sort()\nmerged = []\nfor start, end in intervals:\n    if not merged or start > merged[-1][1]:\n        merged.append([start, end])\n    else:\n        merged[-1][1] = max(merged[-1][1], end)\nprint(merged)"),
    (29, "求列表元素的最大差值（后减前）。", "nums = [2, 3, 10, 6, 4, 8]\nmin_so_far = nums[0]\nmax_diff = 0\nfor n in nums[1:]:\n    max_diff = max(max_diff, n - min_so_far)\n    min_so_far = min(min_so_far, n)\nprint(\"Max diff:\", max_diff)", "填空差值更新。", "nums = [2, 3, 10, 6, 4, 8]\nmin_so_far = nums[0]\nmax_diff = 0\nfor n in nums[1:]:\n    max_diff = max(max_diff, n - min_so_far)\n    min_so_far = min(min_so_far, n)\nprint(\"Max diff:\", max_diff)"),
    (30, "统计列表中每个数字出现次数并排序输出。", "nums = [3, 1, 2, 1, 3, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nfor n in sorted(counts):\n    print(n, counts[n])", "填空统计与排序输出。", "nums = [3, 1, 2, 1, 3, 3]\ncounts = {}\nfor n in nums:\n    counts[n] = counts.get(n, 0) + 1\nfor n in sorted(counts):\n    print(n, counts[n])"),
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
