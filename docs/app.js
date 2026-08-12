/* PyQuest 刷题站前端逻辑（vanilla JS，无构建步骤） */
"use strict";

/* ---------- 全局状态 ---------- */
const state = {
  index: null,          // { chapters: [{id, title, count, files:[{file, diff}]}] }
  questions: {},        // id -> 题目对象（懒加载缓存）
  order: [],            // 当前排序后的题目 id 列表
  pos: 0,               // 当前题号在 order 中的下标
  pyodide: null,
  pyReady: false,
  progress: {},         // id -> true（已完成）
};

const KEY_PROGRESS = "pyquest-progress-v1";
const KEY_CODE = "pyquest-code-";

/* ---------- DOM 快捷引用 ---------- */
const $ = (id) => document.getElementById(id);

/* ---------- 进度 ---------- */
function loadProgress() {
  try { state.progress = JSON.parse(localStorage.getItem(KEY_PROGRESS) || "{}"); }
  catch (e) { state.progress = {}; }
}
function saveProgress() {
  localStorage.setItem(KEY_PROGRESS, JSON.stringify(state.progress));
}
function saveCode(id, code) {
  try { localStorage.setItem(KEY_CODE + id, code); } catch (e) { /* 忽略配额错误 */ }
}
function loadCode(id) {
  try { return localStorage.getItem(KEY_CODE + id) || ""; } catch (e) { return ""; }
}

/* ---------- Pyodide 引擎 ---------- */
async function initPyodide() {
  const status = $("engine-status");
  status.textContent = "Python 引擎加载中…";
  try {
    if (!window.loadPyodide) {
      status.textContent = "引擎脚本加载失败，请检查网络";
      status.className = "engine-status fail";
      return;
    }
    state.pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/",
    });
    state.pyReady = true;
    status.textContent = "Python 引擎就绪 ✓";
    status.className = "engine-status ready";
  } catch (err) {
    console.error("Pyodide 初始化失败:", err);
    status.textContent = "Python 引擎加载失败";
    status.className = "engine-status fail";
  }
}

/* ---------- 索引加载 ---------- */
async function loadIndex() {
  const res = await fetch("data/index.json");
  if (!res.ok) throw new Error("索引加载失败: " + res.status);
  state.index = await res.json();
  renderChapters();
  refreshProgressBar();
}

/* ---------- 渲染章节树 ---------- */
const DIFF_LABEL = { E: "超简单", M: "简单", H: "中等", X: "较难" };

function renderChapters() {
  const wrap = $("chapter-list");
  wrap.innerHTML = "";
  const order = [];
  for (const ch of state.index.chapters) {
    for (const f of ch.files) {
      for (let i = 1; i <= f.n; i++) {
        order.push(ch.id + "-" + f.diff + "-" + String(i).padStart(3, "0"));
      }
    }

    const item = document.createElement("div");
    item.className = "chapter-item";

    const head = document.createElement("button");
    head.className = "chapter-head";
    head.innerHTML = "<span>" + ch.title + "</span><span class='count'>" + ch.count + " 题</span>";
    item.appendChild(head);

    const body = document.createElement("div");
    body.className = "diff-group";
    body.style.display = "none";
    for (const f of ch.files) {
      const label = DIFF_LABEL[f.diff] || f.diff;
      const dg = document.createElement("div");
      const t = document.createElement("div");
      t.className = "diff-title";
      t.textContent = label;
      dg.appendChild(t);
      for (let i = 1; i <= f.n; i++) {
        const id = ch.id + "-" + f.diff + "-" + String(i).padStart(3, "0");
        const btn = document.createElement("button");
        btn.className = "qlink";
        btn.dataset.id = id;
        btn.textContent = id;
        if (state.progress[id]) btn.classList.add("done");
        btn.addEventListener("click", () => openQuestion(id));
        dg.appendChild(btn);
      }
      body.appendChild(dg);
    }
    item.appendChild(body);

    head.addEventListener("click", () => {
      body.style.display = body.style.display === "none" ? "block" : "none";
    });
    wrap.appendChild(item);
  }
  state.order = order;
  state.pos = 0;
}

/* ---------- 题目加载与渲染 ---------- */
async function getQuestion(id) {
  if (state.questions[id]) return state.questions[id];
  // 从索引中查找包含该 id 的章节目录
  const ch = state.index.chapters.find((c) => id.startsWith(c.id + "-"));
  if (!ch) throw new Error("无法定位题目所属章节: " + id);
  const m = id.match(/-([EMHX])-(\d+)$/);
  if (!m) throw new Error("无法解析题目 id: " + id);
  const diffMap = { E: "easy_30", M: "medium_30", H: "hard_30", X: "expert_30" };
  const file = diffMap[m[1]] + ".json";
  const res = await fetch("data/questions/" + ch.dir + "/" + file);
  if (!res.ok) throw new Error("题目数据加载失败: " + res.status);
  const data = await res.json();
  const q = data.questions.find((x) => x.id === id);
  if (!q) throw new Error("题目不存在: " + id);
  state.questions[id] = q;
  return q;
}

async function openQuestion(id) {
  const q = await getQuestion(id);
  const idx = state.order.indexOf(id);
  if (idx >= 0) state.pos = idx;

  $("welcome").classList.add("hidden");
  $("quiz").classList.remove("hidden");
  $("q-id").textContent = q.id;
  $("q-difficulty").textContent = DIFF_LABEL[q.id.split("-")[1][0]] || q.difficulty;
  $("q-difficulty").className = "badge " + q.id.split("-")[1][0];
  $("q-stars").textContent = q.stars || "";
  $("q-topic").textContent = q.topic || "";
  $("q-description").textContent = q.description || "";
  $("q-hints-text").textContent = q.hints || "";
  $("q-hints").classList.toggle("hidden", !q.hints);

  // 编辑器初始为空白；仅当用户之前保存过代码时恢复，否则一律留空
  const saved = loadCode(q.id);
  $("editor").value = saved || "";

  // 题目头部“已完成”徽章 + 左侧链接标记（与已存进度同步）
  const done = !!state.progress[id];
  $("q-done").classList.toggle("hidden", !done);

  // 彻底重置输出与判定区（不残留上一题的通过/失败状态）
  $("output").textContent = "点击「运行」查看结果…";
  $("verdict").classList.add("hidden");
  $("verdict").innerHTML = "";
  $("btn-run").disabled = false;
  $("btn-run").textContent = "▶ 运行";

  document.querySelectorAll(".qlink").forEach((b) => {
    b.classList.toggle("active", b.dataset.id === id);
    b.classList.toggle("done", !!state.progress[id]);
  });
}

/* ---------- 运行与判分 ---------- */
// 运行序号：切题后旧运行结果一律丢弃，防止“残留的通过提示”串到其他题
let runSeq = 0;

function captureRun(pyodide, code) {
  let out = "";
  pyodide.setStdout({ batched: (s) => { out += s; } });
  try {
    pyodide.runPython(code);
  } finally {
    pyodide.setStdout({ batched: () => {} });
  }
  return out;
}

function judge(q, actual) {
  const expected = q.expected_output || "";
  if (actual === expected) return { pass: true };
  // 仅当期望输出本身不是空白时，才允许“尾部空白差异”容差（如缺末尾换行）
  if (expected.trim() !== "" && actual.replace(/\s+$/, "") === expected.replace(/\s+$/, "")) {
    return { pass: true, soft: true };
  }
  return { pass: false };
}

async function runCode() {
  if (!state.pyReady) {
    $("output").textContent = "Python 引擎尚未就绪，请稍候…";
    return;
  }
  const qid = $("q-id").textContent;
  const q = state.questions[qid];
  if (!q) return;
  const seq = ++runSeq;
  const code = $("editor").value;
  saveCode(qid, code);

  const btn = $("btn-run");
  btn.disabled = true;
  btn.textContent = "运行中…";
  $("verdict").classList.add("hidden");
  $("verdict").innerHTML = "";

  try {
    const actual = captureRun(state.pyodide, code);
    // 运行期间若已切题，丢弃本次结果，不显示任何判定
    if (seq !== runSeq) return;
    $("output").textContent = actual === "" ? "（无输出）" : actual;

    const v = judge(q, actual);
    const box = $("verdict");
    box.classList.remove("hidden");
    if (v.pass) {
      box.className = "verdict ok";
      box.innerHTML = "✅ 通过！" + (v.soft ? "（末尾空行差异已忽略）" : "");
      if (!state.progress[qid]) {
        state.progress[qid] = true;
        saveProgress();
        refreshProgressBar();
        markLinkDone(qid);
      }
      // 题目头部立即点亮“已完成”徽章
      $("q-done").classList.remove("hidden");
    } else {
      box.className = "verdict fail";
      box.innerHTML =
        "❌ 输出与期望不一致。<pre>期望输出：\n" + escapeHtml(q.expected_output || "") +
        "\n实际输出：\n" + escapeHtml(actual) + "</pre>";
    }
  } catch (err) {
    if (seq !== runSeq) return;
    $("output").textContent = "";
    const box = $("verdict");
    box.classList.remove("hidden");
    box.className = "verdict fail";
    box.innerHTML = "⚠️ 程序运行出错（SyntaxError / 异常）：<pre>" + escapeHtml(String(err)) + "</pre>";
  } finally {
    if (seq === runSeq) {
      btn.disabled = false;
      btn.textContent = "▶ 运行";
    }
  }
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

/* ---------- 进度 UI ---------- */
function refreshProgressBar() {
  const done = Object.keys(state.progress).length;
  const total = state.order.length;
  $("progress-count").textContent = done;
  $("progress-total").textContent = total;
  $("progress-fill").style.width = total ? (done / total * 100).toFixed(1) + "%" : "0%";
}

function markLinkDone(id) {
  document.querySelectorAll(".qlink").forEach((b) => {
    if (b.dataset.id === id) b.classList.add("done");
  });
}

/* ---------- 导航按钮 ---------- */
async function goto(offset) {
  if (!state.order.length) return;
  const next = (state.pos + offset + state.order.length) % state.order.length;
  try {
    await openQuestion(state.order[next]);
  } catch (err) {
    console.error(err);
  }
}

/* ---------- 事件绑定 ---------- */
$("btn-run").addEventListener("click", runCode);
$("btn-prev").addEventListener("click", () => goto(-1));
$("btn-next").addEventListener("click", () => goto(1));
$("btn-reset").addEventListener("click", () => {
  $("editor").value = "";
  $("output").textContent = "点击「运行」查看结果…";
  $("verdict").classList.add("hidden");
  $("verdict").innerHTML = "";
});
$("btn-hint").addEventListener("click", () => $("q-hints").classList.remove("hidden"));
$("btn-start").addEventListener("click", () => {
  if (state.order.length) openQuestion(state.order[0]);
});
$("btn-clear-progress").addEventListener("click", () => {
  if (!confirm("确定清空全部进度与已保存的代码？此操作不可恢复。")) return;
  try { localStorage.removeItem(KEY_PROGRESS); } catch (e) {}
  state.progress = {};
  refreshProgressBar();
  document.querySelectorAll(".qlink").forEach((b) => b.classList.remove("done"));
  $("q-done").classList.add("hidden");
  $("editor").value = "";
  $("output").textContent = "点击「运行」查看结果…";
  $("verdict").classList.add("hidden");
  $("verdict").innerHTML = "";
});
$("editor").addEventListener("keydown", (e) => {
  if (e.key === "Tab") {
    e.preventDefault();
    const el = e.target;
    const s = el.selectionStart, en = el.selectionEnd;
    el.value = el.value.slice(0, s) + "    " + el.value.slice(en);
    el.selectionStart = el.selectionEnd = s + 4;
  }
});

/* ---------- 启动 ---------- */
loadProgress();
loadIndex().catch((err) => {
  $("chapter-list").innerHTML = "<p style='color:#ef4444'>索引加载失败: " + escapeHtml(err.message) + "</p>";
});
initPyodide();
