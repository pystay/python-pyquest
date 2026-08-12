# -*- coding: utf-8 -*-
"""同步题库到站点目录：复制 questions/ 到 docs/data/questions/ 并生成 docs/data/index.json。

用法：python generator/sync_site.py
"""
import json
import shutil
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "questions")
DST = os.path.join(ROOT, "docs", "data", "questions")

CHAPTER_TITLES = {
    "CH01_Hello_World": "CH01 Hello, World!",
    "CH02_Variables_Types": "CH02 变量和类型",
    "CH03_Lists": "CH03 列表 (Lists)",
    "CH04_Operators": "CH04 基础运算符",
    "CH05_String_Formatting": "CH05 字符串格式化",
    "CH06_Conditionals": "CH06 条件语句",
    "CH07_For_Loops": "CH07 循环 (for)",
    "CH08_While_Loops": "CH08 循环 (while)",
    "CH09_Functions": "CH09 函数 (基础)",
    "CH10_Function_Params": "CH10 函数 (参数)",
    "CH11_Function_Returns": "CH11 函数 (返回值)",
    "CH12_Scope": "CH12 作用域与变量",
    "CH13_Tuples": "CH13 元组 (Tuples)",
    "CH14_Dictionaries": "CH14 字典 (Dictionaries)",
    "CH15_Sets": "CH15 集合 (Sets)",
}

DIFF_MAP = {"easy_30.json": "E", "medium_30.json": "M", "hard_30.json": "H", "expert_30.json": "X"}

# 清空并复制
if os.path.exists(DST):
    shutil.rmtree(DST)
os.makedirs(DST)

chapters = []
total = 0
for src_dir in sorted(glob.glob(os.path.join(SRC, "CH*"))):
    name = os.path.basename(src_dir)
    files = []
    count = 0
    for fname in sorted(glob.glob(os.path.join(src_dir, "*.json"))):
        base = os.path.basename(fname)
        if base not in DIFF_MAP:
            continue
        with open(fname, encoding="utf-8") as fh:
            data = json.load(fh)
        n = len(data["questions"])
        count += n
        total += n
        files.append({"diff": DIFF_MAP[base], "file": base, "n": n})
        shutil.copy2(fname, os.path.join(DST, name + "_" + base))
    chapters.append({
        "id": name.split("_")[0],
        "dir": name,
        "title": CHAPTER_TITLES.get(name, name),
        "count": count,
        "files": files,
    })

# 注意：复制后文件名改为 CH01_Hello_World_easy_30.json，app.js 的 fetch 路径要对应
# 重新规划：保持原目录结构更简单
if os.path.exists(DST):
    shutil.rmtree(DST)
os.makedirs(DST)
chapters = []
total = 0
for src_dir in sorted(glob.glob(os.path.join(SRC, "CH*"))):
    name = os.path.basename(src_dir)
    dst_dir = os.path.join(DST, name)
    shutil.copytree(src_dir, dst_dir)
    files = []
    count = 0
    for fname in sorted(glob.glob(os.path.join(src_dir, "*.json"))):
        base = os.path.basename(fname)
        if base not in DIFF_MAP:
            continue
        with open(fname, encoding="utf-8") as fh:
            data = json.load(fh)
        n = len(data["questions"])
        count += n
        total += n
        files.append({"diff": DIFF_MAP[base], "file": base, "n": n})
    chapters.append({
        "id": name.split("_")[0],
        "dir": name,
        "title": CHAPTER_TITLES.get(name, name),
        "count": count,
        "files": files,
    })

index = {"generated_at": "static", "chapters": chapters}
with open(os.path.join(ROOT, "docs", "data", "index.json"), "w", encoding="utf-8") as fh:
    json.dump(index, fh, ensure_ascii=False, indent=2)

print("同步完成：%d 章 %d 道 → docs/data/questions/ + docs/data/index.json" % (len(chapters), total))
