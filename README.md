# PyQuest — 互动式 Python 练习平台

> 闯关式 · 高密度 · 从零到进阶的 Python 刷题平台

## 🖥️ 在线练习

**👉 [https://pystay.github.io/python-pyquest/](https://pystay.github.io/python-pyquest/)**

在浏览器中直接刷题：代码通过 **Pyodide（WebAssembly 版 Python）** 实时运行判分，无需安装任何软件。
完成一题自动记录进度（保存在浏览器本地）。题库、前端与判分逻辑全部开源于此仓库。

> 若链接暂未生效，请到仓库 **Settings → Pages** 选择分支 `master` 与目录 `/docs` 后保存，等待 1~2 分钟即可访问。

PyQuest 是一套以 **learn-py.org** 知识体系为蓝本的 Python 交互式练习题集，
按"超简单 → 简单 → 中等 → 较难"四档难度阶梯组织，共规划 **29 章 × 120 题 = 3480 道**练习题。

## ✨ 特性

- **四档难度阶梯**：每章 120 道题，超简单（填空补全）→ 简单（实现简单功能）→ 中等（多知识点综合）→ 较难（算法与边缘情况）
- **统一题型格式**：每道题包含 `id` / `topic` / `difficulty` / `stars` / `description` / `code_template` / `expected_output` / `hints` / `test_cases` / `solution` 十个字段
- **自动判分机制**：运行代码捕获输出 `captured_output`，执行 `test_cases` 中的断言验证
- **自动化生成**：`expected_output` 与 `test_cases` 由生成脚本模拟运行 `solution` 自动产出，杜绝手写转义误差
- **可重复生成**：每个章节的题库由独立生成脚本驱动，可随时重新生成并校验

## 📦 当前进度

| 章节 | 状态 | 章节 | 状态 |
|---|---|---|---|
| CH01 Hello, World! | ✅ 120 道 | CH09 函数（基础） | ✅ 120 道 |
| CH02 变量和类型 | ✅ 100 道 | CH10 函数（参数） | ✅ 120 道 |
| CH03 列表 (Lists) | ✅ 120 道 | CH11 函数（返回值） | ✅ 120 道 |
| CH04 基础运算符 | ✅ 120 道 | CH12 作用域与变量 | ✅ 120 道 |
| CH05 字符串格式化 | ✅ 120 道 | CH13 元组 (Tuples) | ✅ 120 道 |
| CH06 条件语句 | ✅ 120 道 | CH14 字典 (Dictionaries) | ✅ 120 道 |
| CH07 循环 (for) | ✅ 120 道 | CH15 集合 (Sets) | ✅ 120 道 |
| CH08 循环 (while) | ✅ 120 道 | CH16 ~ CH29 | ⏳ 待生成 |

> **进度合计：15 章 = 1780 道**，全库校验通过。剩余 14 章正在分批生成中。

## 🚀 快速开始

### 环境要求

- Python 3.8+

### 运行全库测试

```bash
python generator/validate.py
```

输出示例：

```
OK: CH01_Hello_World 120 道通过
...
全库校验通过：15 章，1780 道
```

### 重新生成某一章的题库

```bash
python generator/gen_ch01_easy.py     # CH01 超简单档
python generator/gen_ch02_hard.py     # CH02 中等档（20 道）
python generator/gen_ch14.py          # CH14 四档
...
python generator/validate.py          # 生成后全库校验
```

## 📁 目录结构

```
PyQuest/
├── docs/                 # 在线练习站点（GitHub Pages 发布目录）
│   ├── index.html        # 刷题页面
│   ├── app.js            # 导航 + Pyodide 判分 + 进度
│   ├── styles.css
│   └── data/             # 同步的题库数据 + index.json
├── questions/            # 题库（按章节组织）
│   ├── CH01_Hello_World/ # easy_30.json / medium_30.json / hard_30.json / expert_30.json
│   ├── CH02_Variables_Types/
│   └── ...               # 每章 4 个难度文件
├── generator/            # 题库生成与校验脚本
│   ├── framework.py      # 共享生成框架（含自动挖空模板）
│   ├── gen_chXX.py       # 各章生成脚本
│   ├── sync_site.py      # 同步题库 → docs/data/ 并生成索引
│   └── validate.py       # 全库校验入口
└── package.json
```

## 📝 题库格式

```json
{
  "id": "CH01-E-001",
  "topic": "print() 函数的基本使用",
  "difficulty": "超简单",
  "stars": "⭐",
  "description": "用 print() 输出字符串 'Hello, World!'。",
  "code_template": "print(___)",
  "expected_output": "Hello, World!\n",
  "hints": "字符串需要加引号。",
  "test_cases": ["assert captured_output == 'Hello, World!\\n'"],
  "solution": "print('Hello, World!')"
}
```

### 难度与 id 约定

| 难度 | 星数 | 文件 | id 后缀 | 定位 |
|---|---|---|---|---|
| 超简单 | ⭐ | easy_30.json | E | 填空补全（1-2 处修改，≤5 行） |
| 简单 | ⭐⭐ | medium_30.json | M | 实现简单功能（5-10 行） |
| 中等 | ⭐⭐⭐ | hard_30.json | H | 综合 2-3 个知识点（10-20 行） |
| 较难 | ⭐⭐⭐⭐ | expert_30.json | X | 3+ 知识点、边缘情况与算法思维（20-40 行） |

## 🗺️ 路线图

- [x] **阶段一**：题库生成（29 章 × 120 道，进行中，已 15 章）
- [x] **阶段二**：在线练习前端（GitHub Pages + Pyodide 实时判分）
- [ ] **阶段三**：本地测试与判分验证
- [ ] **阶段四**：部署上线与推广

## 🤝 贡献者

- **pystay** — 项目设计与全部题库内容

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。
