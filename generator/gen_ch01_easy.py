# -*- coding: utf-8 -*-
"""生成 CH01 超简单（Easy）30 道题：print() 函数的基本使用。

按 PyQuest 项目清单"第一轮执行指令"生成，输出到
questions/CH01_Hello_World/easy_30.json，并执行校验：
  - JSON 合法、id 连续且唯一
  - expected_output 不重复
  - solution 实际运行输出与 expected_output 一致
  - test_cases 断言全部通过（captured_output 机制）
"""
import io
import json
import os
import sys

TOPIC = "print() 函数的基本使用"
DIFFICULTY = "超简单"
STARS = "⭐"


def q(num, desc, template, expected, solution, hints="", extra_tests=None):
    """构造一道题。expected 为程序运行后的完整输出（真实换行/制表符）。"""
    tests = ["assert captured_output == " + repr(expected)]
    if extra_tests:
        tests.extend(extra_tests)
    return {
        "id": "CH01-E-%03d" % num,
        "topic": TOPIC,
        "difficulty": DIFFICULTY,
        "stars": STARS,
        "description": desc,
        "code_template": template,
        "expected_output": expected,
        "hints": hints,
        "test_cases": tests,
        "solution": solution,
    }


def build_questions():
    questions = []
    a = questions.append

    # --- 指定 15 种用法（每种至少 1 题） ---
    # ① 纯字符串（单引号 / 双引号）
    a(q(1, "用 print() 输出单引号字符串 'Hello, Python!'。",
        "print(___)", "Hello, Python!\n", "print('Hello, Python!')",
        "在括号内填入 'Hello, Python!'，字符串要用引号包裹。"))
    a(q(2, "用 print() 输出双引号字符串 \"Hello, World!\"。",
        "print(___)", "Hello, World!\n", 'print("Hello, World!")',
        "在括号内填入 \"Hello, World!\"，双引号同样能包裹字符串。"))
    # ② 数字（整数 / 浮点数）
    a(q(3, "用 print() 输出整数 42。",
        "print(___)", "42\n", "print(42)",
        "数字不需要引号，直接填入 42。"))
    a(q(4, "用 print() 输出浮点数 3.14。",
        "print(___)", "3.14\n", "print(3.14)",
        "小数直接填入 3.14 即可。"))
    # ③ 布尔值
    a(q(5, "用 print() 输出布尔值 True。",
        "print(___)", "True\n", "print(True)",
        "布尔值 True 首字母大写，且不加引号。"))
    a(q(6, "用 print() 输出带双引号的字符串。",
        "print(___)", 'He said "hi"\n', "print('He said \"hi\"')",
        "外层用单引号，内层的双引号就能直接显示。"))
    # ④ 输出变量（字符串变量 / 数字变量）
    a(q(7, "定义字符串变量 name 并输出它。",
        "name = \"Alice\"\nprint(___)", "Alice\n", "name = \"Alice\"\nprint(name)",
        "在 print 括号内填入变量名 name，不要加引号。"))
    a(q(8, "定义数字变量 age 并输出它。",
        "age = 25\nprint(___)", "25\n", "age = 25\nprint(age)",
        "在 print 括号内填入变量名 age。"))
    # ⑤ 多个参数（逗号分隔，空格自动填充）
    a(q(9, "用 print() 同时输出两个字符串。",
        "print(\"Hello\", ___)", "Hello World\n", 'print("Hello", "World")',
        "在第二个参数位置填入 \"World\"，多个参数用逗号分隔。"))
    # ⑥ 转义字符 \n
    a(q(10, "用 \\n 让字符串在中间换行。",
        "print(___)", "Line1\nLine2\n", 'print("Line1\\nLine2")',
        "在字符串中写 \\n 表示换行，注意要写在引号内。"))
    # ⑦ 输出空行
    a(q(11, "在两次输出之间打印一个空行。",
        "print(\"A\")\nprint(___)\nprint(\"B\")", "A\n\nB\n",
        'print("A")\nprint()\nprint("B")',
        "让 print() 不带任何参数，就会输出一个空行。"))
    # ⑧ sep 参数
    a(q(12, "用 sep 参数把三个词用 - 连接输出。",
        "print(\"a\", \"b\", \"c\", sep=___)", "a-b-c\n",
        'print("a", "b", "c", sep="-")',
        "在 sep= 后面填入 \"-\"，注意要用引号。"))
    # ⑨ end 参数
    a(q(13, "用 end 参数把结尾的换行改成 !。",
        "print(\"Hi\", end=___)", "Hi!", 'print("Hi", end="!")',
        "在 end= 后面填入 \"!\"，输出就不会换行了。"))
    # ⑩ 特殊字符
    a(q(14, "用 print() 输出包含 @ 的邮箱字符串。",
        "print(___)", "Email: user@example.com\n",
        "print(\"Email: user@example.com\")",
        "直接填入 \"Email: user@example.com\" 即可。"))
    # ⑪ 计算表达式
    a(q(15, "用 print() 输出 1 + 2 的计算结果。",
        "print(___)", "3\n", "print(1 + 2)",
        "在括号内填入表达式 1 + 2，print 会先算出结果。"))
    # ⑫ 比较表达式
    a(q(16, "用 print() 输出 3 < 2 的比较结果。",
        "print(___)", "False\n", "print(3 < 2)",
        "在括号内填入 3 < 2，结果为 False。"))
    # ⑬ 字符串与数字混合
    a(q(17, "用 print() 输出字符串和数字混合内容。",
        "print(___, 25)", "Age: 25\n", 'print("Age:", 25)',
        "第一个参数填 \"Age:\"，与数字 25 用逗号分隔。"))
    # ⑭ 连续调用 print()
    a(q(18, "连续调用两次 print() 输出两行。",
        "print(\"One\")\nprint(___)", "One\nTwo\n", 'print("One")\nprint("Two")',
        "第二次调用时填入 \"Two\"，观察每次 print 自动换行。"))
    # ⑮ 多行字符串（三引号）
    a(q(19, "用三引号字符串一次输出三行。",
        "print(___)", "Line1\nLine2\nLine3\n",
        'print("""Line1\\nLine2\\nLine3""")',
        "用三引号包裹，字符串内用 \\n 换行。"))

    # --- 补充 11 道常见用法 ---
    # 转义字符 \t
    a(q(20, "用 \\t 在字符串中间插入制表符。",
        "print(___)", "A\tB\n", 'print("A\\tB")',
        "在字符串中写 \\t 表示制表符。"))
    # 字符串拼接
    a(q(21, "用 + 拼接两个字符串后输出。",
        "print(\"Python\" + ___)", "Python is fun\n", 'print("Python" + " is fun")',
        "第二个字符串是 \" is fun\"，注意前面有空格。"))
    # 变量参与计算
    a(q(22, "定义 age 后输出 age + 1 的结果。",
        "age = 25\nprint(___)", "26\n", "age = 25\nprint(age + 1)",
        "在 print 括号内填入 age + 1。"))
    # 乘法
    a(q(23, "用 print() 输出 7 * 8 的计算结果。",
        "print(___)", "56\n", "print(7 * 8)",
        "填入乘法表达式 7 * 8。"))
    # 幂运算
    a(q(24, "用 print() 输出 2 的 3 次方。",
        "print(___)", "8\n", "print(2 ** 3)",
        "Python 中用 ** 表示幂运算，填入 2 ** 3。"))
    # 除法
    a(q(25, "用 print() 输出 9 / 3 的结果。",
        "print(___)", "3.0\n", "print(9 / 3)",
        "填入 9 / 3，注意除法的结果是浮点数。"))
    # 负数
    a(q(26, "用 print() 输出负数 -7。",
        "print(___)", "-7\n", "print(-7)",
        "直接在括号内填入 -7。"))
    # 字符串变量与多参数
    a(q(27, "定义 name 后与字符串一起输出。",
        "name = \"Bob\"\nprint(___, name)", "Hi Bob\n", 'name = "Bob"\nprint("Hi", name)',
        "第一个参数填 \"Hi\"，与变量 name 用逗号分隔。"))
    # sep 拼接日期
    a(q(28, "用 sep 参数把日期用 / 连接输出。",
        "print(\"2024\", \"08\", \"12\", sep=___)", "2024/08/12\n",
        'print("2024", "08", "12", sep="/")',
        "在 sep= 后面填入 \"/\"。"))
    # end 省略号
    a(q(29, "用 end 参数在末尾追加省略号。",
        "print(\"Loading\", end=___)", "Loading...", 'print("Loading", end="...")',
        "在 end= 后面填入 \"...\"。"))
    # 多参数混合类型
    a(q(30, "用 print() 输出字符串、字符串和数字的混合。",
        "print(\"I love\", ___, 3)", "I love Python 3\n",
        'print("I love", "Python", 3)',
        "第二个参数填 \"Python\"，三个参数用逗号分隔。"))

    assert len(questions) == 30, "必须恰好 30 道题"
    return questions


def simulate(solution, test_cases):
    """模拟运行 solution，返回 (实际输出, 断言是否全部通过)。"""
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        exec(solution, {})
    finally:
        sys.stdout = old
    captured = buf.getvalue()
    for case in test_cases:
        env = {"captured_output": captured}
        exec(case, env)
    return captured


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH01_Hello_World")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "easy_30.json")

    questions = build_questions()

    # 校验：id 连续唯一
    ids = [x["id"] for x in questions]
    assert ids == ["CH01-E-%03d" % i for i in range(1, 31)], "id 必须为 CH01-E-001..030"

    # 校验：expected_output 不重复
    outs = [x["expected_output"] for x in questions]
    assert len(set(outs)) == 30, "expected_output 存在重复: %s" % (
        [o for o in outs if outs.count(o) > 1])

    # 校验：模拟运行 + 断言
    for x in questions:
        captured = simulate(x["solution"], x["test_cases"])
        assert captured == x["expected_output"], (
            "%s 实际输出 %r != 期望 %r" % (x["id"], captured, x["expected_output"]))

    data = {"chapter": "CH01", "title": "Hello, World!", "difficulty": "超简单",
            "questions": questions}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("已生成 %s（%d 道题）" % (out_path, len(questions)))
    for x in questions:
        print("  %s -> %r" % (x["id"], x["expected_output"]))


if __name__ == "__main__":
    main()
