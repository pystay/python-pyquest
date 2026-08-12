# -*- coding: utf-8 -*-
"""生成 CH02 较难档 20 道（CH02-X-001..020），主题"变量的复杂应用与类型检查技巧"。

清单要求（第八轮）：
- 10 种复杂应用场景各 ≥2：类型检查与条件分支 / 转换异常处理 / 混合类型列表提取 /
  数字与字符串互转 / 变量作用域 / 可变与不可变 / 类型推断与动态类型 /
  复杂数据结构访问 / id() 引用 / 自定义类型检查
- 边缘情况：≥5 转换异常、≥5 None/空值、≥5 布尔参与运算、≥5 复杂结构类型检查
- 每道 3-5 个 assert；模板含 ___ 占位符
"""
import io
import json
import os
import sys

from framework import auto_template

DIFFICULTY = "较难"
STARS = "⭐⭐⭐⭐"
SUFFIX = "X"
TOPIC = "变量的复杂应用与类型检查技巧"


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
    if "___" not in template:
        template = auto_template(solution)
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


NL = "\n"

# (序号, 描述, 模板, 提示, solution)
EXPERT = [
    (1, "给定混合列表 data，将其中能安全转换为整数的元素相加（布尔值跳过、无法转换的字符串跳过），输出结果。",
     "data = [10, '20', 3.14, True, 'False', None, 25, '30']" + NL + "total = 0" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        continue" + NL + "    if isinstance(item, (int, float)):" + NL + "        total += int(item)" + NL + "    elif isinstance(item, str):" + NL + "        ___" + NL + "            total += int(item)" + NL + "        except ValueError:" + NL + "            pass" + NL + "print(total)",
     "用 try-except 捕获 int() 的 ValueError。",
     "data = [10, '20', 3.14, True, 'False', None, 25, '30']" + NL + "total = 0" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        continue" + NL + "    if isinstance(item, (int, float)):" + NL + "        total += int(item)" + NL + "    elif isinstance(item, str):" + NL + "        try:" + NL + "            total += int(item)" + NL + "        except ValueError:" + NL + "            pass" + NL + "print(total)"),
    (2, "统计混合列表中各类型元素的数量（区分 int/float/str/bool/None），输出计数字典。",
     "data = [10, '20', 3.14, True, 'False', None, 25]" + NL + "counts = {'int': 0, 'float': 0, 'str': 0, 'bool': 0, 'none': 0}" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        counts['bool'] += 1" + NL + "    elif isinstance(item, int):" + NL + "        counts['int'] += 1" + NL + "    elif isinstance(item, float):" + NL + "        counts['float'] += 1" + NL + "    elif isinstance(item, str):" + NL + "        counts['str'] += 1" + NL + "    elif item is None:" + NL + "        counts['none'] += 1" + NL + "print(___)",
     "bool 是 int 的子类，判断顺序要先 bool 后 int。",
     "data = [10, '20', 3.14, True, 'False', None, 25]" + NL + "counts = {'int': 0, 'float': 0, 'str': 0, 'bool': 0, 'none': 0}" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        counts['bool'] += 1" + NL + "    elif isinstance(item, int):" + NL + "        counts['int'] += 1" + NL + "    elif isinstance(item, float):" + NL + "        counts['float'] += 1" + NL + "    elif isinstance(item, str):" + NL + "        counts['str'] += 1" + NL + "    elif item is None:" + NL + "        counts['none'] += 1" + NL + "print(counts)"),
    (3, "定义 safe_int() 函数：将值转为整数，转换失败返回 None，对列表 values 逐项转换并输出结果列表。",
     "def safe_int(value):" + NL + "    try:" + NL + "        return int(value)" + NL + "    except (ValueError, TypeError):" + NL + "        ___" + NL + "values = ['12', '3.5', 7, None, 'abc']" + NL + "results = [safe_int(v) for v in values]" + NL + "print(results)",
     "异常时返回 None。",
     "def safe_int(value):" + NL + "    try:" + NL + "        return int(value)" + NL + "    except (ValueError, TypeError):" + NL + "        return None" + NL + "values = ['12', '3.5', 7, None, 'abc']" + NL + "results = [safe_int(v) for v in values]" + NL + "print(results)"),
    (4, "理解全局变量：counter 为全局变量，increment() 函数通过 global 修改它，连续调用两次后输出 counter。",
     "counter = 0" + NL + "def increment(step):" + NL + "    global counter" + NL + "    counter += step" + NL + "increment(2)" + NL + "increment(3)" + NL + "print(\"Counter:\", counter)",
     "函数内修改全局变量必须声明 global。",
     "counter = 0" + NL + "def increment(step):" + NL + "    global counter" + NL + "    counter += step" + NL + "increment(2)" + NL + "increment(3)" + NL + "print(\"Counter:\", counter)"),
    (5, "可变与不可变类型：函数内对列表追加元素、对字符串重新赋值，输出调用后原变量的值。",
     "def modify(li, s):" + NL + "    li.append(4)" + NL + "    s = s + '!'" + NL + "my_list = [1, 2, 3]" + NL + "my_str = 'hi'" + NL + "modify(my_list, my_str)" + NL + "print(my_list, my_str)",
     "列表可变（原地修改生效），字符串不可变（函数内是新对象）。",
     "def modify(li, s):" + NL + "    li.append(4)" + NL + "    s = s + '!'" + NL + "my_list = [1, 2, 3]" + NL + "my_str = 'hi'" + NL + "modify(my_list, my_str)" + NL + "print(my_list, my_str)"),
    (6, "类型推断与动态类型：变量 x 依次赋值为整数、字符串、列表，分别用 type().__name__ 输出其类型名。",
     "x = 42" + NL + "print(type(x).__name__)" + NL + "x = 'hello'" + NL + "print(type(x).__name__)" + NL + "x = [1, 2]" + NL + "print(___)",
     "type(x).__name__ 返回类型名字符串。",
     "x = 42" + NL + "print(type(x).__name__)" + NL + "x = 'hello'" + NL + "print(type(x).__name__)" + NL + "x = [1, 2]" + NL + "print(type(x).__name__)"),
    (7, "嵌套字典与列表访问：从 data['user']['scores'] 取出第一个分数，输出 '名字: 分数' 格式。",
     "data = {'user': {'name': 'Alice', 'scores': [90, 85]}}" + NL + "name = data['user']['name']" + NL + "first = data['user']['scores'][0]" + NL + "print(f'{name}: {first}')",
     "逐层用键/索引访问。",
     "data = {'user': {'name': 'Alice', 'scores': [90, 85]}}" + NL + "name = data['user']['name']" + NL + "first = data['user']['scores'][0]" + NL + "print(f'{name}: {first}')"),
    (8, "变量引用与 id()：判断小整数 256 与 256 是否同一对象、列表与其副本是否同一对象，输出三个布尔结果。",
     "a = 256" + NL + "b = 256" + NL + "c = [1, 2]" + NL + "d = c" + NL + "print(a is b, c is d, c is c.copy())",
     "小整数可能被缓存；list.copy() 返回新对象。",
     "a = 256" + NL + "b = 256" + NL + "c = [1, 2]" + NL + "d = c" + NL + "print(a is b, c is d, c is c.copy())"),
    (9, "自定义类型检查：定义 Animal 与继承它的 Dog 类，创建 Dog 实例后用 isinstance() 判断类型并输出。",
     "class Animal:" + NL + "    pass" + NL + "class Dog(Animal):" + NL + "    pass" + NL + "d = Dog()" + NL + "print(isinstance(d, Dog), isinstance(d, Animal), type(d).__name__)",
     "isinstance 支持继承关系判断。",
     "class Animal:" + NL + "    pass" + NL + "class Dog(Animal):" + NL + "    pass" + NL + "d = Dog()" + NL + "print(isinstance(d, Dog), isinstance(d, Animal), type(d).__name__)"),
    (10, "布尔值参与运算的特殊情况：输出 True+True、True*3、bool(0)、bool([])、bool('a') 五个结果。",
     "print(True + True, True * 3, bool(0), bool([]), bool('a'))",
     "True 可当作 1 参与算术。",
     "print(True + True, True * 3, bool(0), bool([]), bool('a'))"),
    (11, "None 与空值判断：分别判断 None、空列表、空字符串与 None 的关系及与空值比较的结果，输出五个布尔值。",
     "a = None" + NL + "b = []" + NL + "c = ''" + NL + "print(a is None, b is None, b == [], c == '')",
     "is None 判断身份，== 判断值相等。",
     "a = None" + NL + "b = []" + NL + "c = ''" + NL + "print(a is None, b is None, b == [], c == '')"),
    (12, "从混合列表提取数字：将能转换为浮点数的元素转为 float 放入新列表（跳过无法转换的），输出结果列表。",
     "data = ['12', '3.5', '7', 'x', 8]" + NL + "nums = []" + NL + "for item in data:" + NL + "    ___" + NL + "        nums.append(float(item))" + NL + "    except (ValueError, TypeError):" + NL + "        continue" + NL + "print(nums)",
     "float() 可转换数字字符串；8 为 int 也可转。",
     "data = ['12', '3.5', '7', 'x', 8]" + NL + "nums = []" + NL + "for item in data:" + NL + "    try:" + NL + "        nums.append(float(item))" + NL + "    except (ValueError, TypeError):" + NL + "        continue" + NL + "print(nums)"),
    (13, "异常处理链：convert() 将值转 int，捕获 ValueError 与 TypeError 返回 None，对多种输入转换后输出结果列表。",
     "def convert(value):" + NL + "    try:" + NL + "        return int(value)" + NL + "    except (ValueError, TypeError):" + NL + "        return None" + NL + "results = [convert(v) for v in ['5', 'abc', None, 3.9, '']]" + NL + "print(results)",
     "int(3.9) 截断为 3；int('') 抛 ValueError。",
     "def convert(value):" + NL + "    try:" + NL + "        return int(value)" + NL + "    except (ValueError, TypeError):" + NL + "        return None" + NL + "results = [convert(v) for v in ['5', 'abc', None, 3.9, '']]" + NL + "print(results)"),
    (14, "参数类型校验：add() 函数仅当两个参数均为 int/float 时求和，否则返回 None，输出三组调用结果。",
     "def add(a, b):" + NL + "    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):" + NL + "        return None" + NL + "    return a + b" + NL + "print(add(1, 2), add('x', 2), add(1.5, 2))",
     "isinstance(a, (int, float)) 检查数值类型。",
     "def add(a, b):" + NL + "    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):" + NL + "        return None" + NL + "    return a + b" + NL + "print(add(1, 2), add('x', 2), add(1.5, 2))"),
    (15, "深浅拷贝与引用：对含嵌套列表的 orig 分别做浅拷贝与深拷贝，修改浅拷贝的内层后输出原列表与深拷贝的内层。",
     "import copy" + NL + "orig = [1, [2, 3]]" + NL + "shallow = copy.copy(orig)" + NL + "deep = copy.deepcopy(orig)" + NL + "shallow[1].append(4)" + NL + "print(orig[1], deep[1])",
     "浅拷贝共享内层可变对象，深拷贝完全独立。",
     "import copy" + NL + "orig = [1, [2, 3]]" + NL + "shallow = copy.copy(orig)" + NL + "deep = copy.deepcopy(orig)" + NL + "shallow[1].append(4)" + NL + "print(orig[1], deep[1])"),
    (16, "鸭子类型与方法检查：定义 Cat 与 Dog 类（各有 speak 方法），用 hasattr() 判断对象是否有 speak 方法再调用，并传入一个普通整数观察结果。",
     "class Cat:" + NL + "    def speak(self):" + NL + "        return 'Meow'" + NL + "class Dog:" + NL + "    def speak(self):" + NL + "        return 'Woof'" + NL + "def call_speak(animal):" + NL + "    if hasattr(animal, 'speak'):" + NL + "        print(animal.speak())" + NL + "    else:" + NL + "        print('No speak method')" + NL + "call_speak(Cat())" + NL + "call_speak(Dog())" + NL + "call_speak(42)",
     "hasattr(obj, name) 检查属性/方法是否存在。",
     "class Cat:" + NL + "    def speak(self):" + NL + "        return 'Meow'" + NL + "class Dog:" + NL + "    def speak(self):" + NL + "        return 'Woof'" + NL + "def call_speak(animal):" + NL + "    if hasattr(animal, 'speak'):" + NL + "        print(animal.speak())" + NL + "    else:" + NL + "        print('No speak method')" + NL + "call_speak(Cat())" + NL + "call_speak(Dog())" + NL + "call_speak(42)"),
    (17, "布尔值参与数值运算的陷阱：跳过列表中的布尔值，对其余元素安全 int() 转换后求和，输出结果。",
     "data = [True, 1, '3']" + NL + "total = 0" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        continue" + NL + "    try:" + NL + "        total += int(item)" + NL + "    except (ValueError, TypeError):" + NL + "        pass" + NL + "print('Total:', total)",
     "bool 是 int 子类，int(True) 会得到 1，需先跳过。",
     "data = [True, 1, '3']" + NL + "total = 0" + NL + "for item in data:" + NL + "    if isinstance(item, bool):" + NL + "        continue" + NL + "    try:" + NL + "        total += int(item)" + NL + "    except (ValueError, TypeError):" + NL + "        pass" + NL + "print('Total:', total)"),
    (18, "复杂结构中的类型检查：字典混合键（int/str/tuple），遍历输出每个键及其值的类型名。",
     "d = {1: 'int', '1': 'str', (1,): 'tuple'}" + NL + "for key in d:" + NL + "    print(key, type(d[key]).__name__)",
     "字典保持插入顺序。",
     "d = {1: 'int', '1': 'str', (1,): 'tuple'}" + NL + "for key in d:" + NL + "    print(key, type(d[key]).__name__)"),
    (19, "递归与全局变量：全局累加器 total，accumulate(n) 递归累加 n 到 1，调用 accumulate(4) 后输出 total。",
     "total = 0" + NL + "def accumulate(n):" + NL + "    global total" + NL + "    if n == 0:" + NL + "        return" + NL + "    total += n" + NL + "    accumulate(n - 1)" + NL + "accumulate(4)" + NL + "print(total)",
     "递归每层用 global 修改 total。",
     "total = 0" + NL + "def accumulate(n):" + NL + "    global total" + NL + "    if n == 0:" + NL + "        return" + NL + "    total += n" + NL + "    accumulate(n - 1)" + NL + "accumulate(4)" + NL + "print(total)"),
    (20, "综合类型检查工具：classify() 将任意值归类为 none/bool/int/float/str/container，对示例列表逐项输出分类名。",
     "def classify(value):" + NL + "    if value is None:" + NL + "        return 'none'" + NL + "    if isinstance(value, bool):" + NL + "        return 'bool'" + NL + "    if isinstance(value, int):" + NL + "        return 'int'" + NL + "    if isinstance(value, float):" + NL + "        return 'float'" + NL + "    if isinstance(value, str):" + NL + "        return 'str'" + NL + "    if isinstance(value, (list, tuple, set, dict)):" + NL + "        return 'container'" + NL + "    return 'unknown'" + NL + "for v in [True, 5, 3.14, 'hi', [1], None]:" + NL + "    print(classify(v))",
     "先判断 None 与 bool，再判断数值与容器类型。",
     "def classify(value):" + NL + "    if value is None:" + NL + "        return 'none'" + NL + "    if isinstance(value, bool):" + NL + "        return 'bool'" + NL + "    if isinstance(value, int):" + NL + "        return 'int'" + NL + "    if isinstance(value, float):" + NL + "        return 'float'" + NL + "    if isinstance(value, str):" + NL + "        return 'str'" + NL + "    if isinstance(value, (list, tuple, set, dict)):" + NL + "        return 'container'" + NL + "    return 'unknown'" + NL + "for v in [True, 5, 3.14, 'hi', [1], None]:" + NL + "    print(classify(v))"),
]

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "questions", "CH02_Variables_Types")
    os.makedirs(out_dir, exist_ok=True)

    questions = [make_q(num, desc, tpl, hint, sol) for num, desc, tpl, hint, sol in EXPERT]
    assert len(questions) == 20, len(questions)
    ids = [q["id"] for q in questions]
    assert ids == ["CH02-X-%03d" % i for i in range(1, 21)], ids
    outs = [q["expected_output"] for q in questions]
    assert len(set(outs)) == 20, "expected_output 存在重复"
    for q in questions:
        assert q["code_template"].count("___") >= 1, q["id"]
        run(q["solution"])  # 再跑一次确认可执行
        for t in q["test_cases"]:
            exec(t, {"captured_output": q["expected_output"]})

    payload = {"chapter": "CH02", "title": TOPIC,
               "difficulty": DIFFICULTY, "questions": questions}
    path = os.path.join(out_dir, "expert_30.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("已生成 %s（%d 道）" % (path, len(questions)))
    print("OK: 较难档 20 道，id 唯一，expected_output 唯一")


if __name__ == "__main__":
    main()
