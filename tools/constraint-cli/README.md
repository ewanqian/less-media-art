# constraint-cli

少媒体艺术研究工具 - 在约束条件下与AI对话

## 功能

### 1. 苏格拉底模式（推荐）

AI扮演提问者，通过十轮对话帮助你反思：

```bash
python socratic.py --topic "你想探索的主题"
```

**特点**：
- AI只提问，不回答
- 十轮深入对话
- 自动生成对话档案
- 显形你的思维过程

### 2. 约束模式（开发中）

设定约束规则，记录创作过程：

```bash
constraint-cli --constraint "仅使用100个token" --log session.log
```

## 安装

```bash
cd tools/constraint-cli
pip install -e .
```

## 依赖

- Python 3.8+
- Ollama（本地运行）

## 使用示例

### 苏格拉底对话

```bash
$ python socratic.py --topic "创作的意义"

============================================================
苏格拉底模式 - 十轮批判对话
主题: 创作的意义
============================================================

规则:
1. AI只会提问，不会直接回答
2. 每轮你必须回应，不能跳过
3. 共10轮，结束后生成对话档案
4. 输入 'quit' 可提前结束

[1/10] AI: 你想探索'创作的意义'，能告诉我是什么吸引你关注这个话题吗？
------------------------------------------------------------
你: [你的回答]

[2/10] AI: 你刚才的回答中，有一个潜在的假设，你能识别出来吗？
...
```

对话结束后，档案自动保存到 `~/.less-media-art/archives/`

## 档案格式

```json
{
  "type": "socratic_dialogue",
  "topic": "创作的意义",
  "metadata": {
    "start_time": "2025-02-02T10:00:00",
    "end_time": "2025-02-02T10:30:00",
    "total_rounds": 10,
    "model": "llama3.2:3b"
  },
  "dialogue": [
    {
      "round": 1,
      "ai_question": "...",
      "user_response": "...",
      "timestamp": "..."
    }
  ],
  "reflection_prompts": [...]
}
```

## 哲学

这个工具不是帮你生成内容的工具，而是**让你意识到自己在使用工具**的工具。

- 通过约束，重获主体性
- 通过对话，显形思维过程
- 通过记录，创造价值档案

## 相关文档

- [对话式创作](../../docs/theory/dialogic-creation.md)
- [过程显形](../../docs/theory/process-visibilization.md)
- [摩擦](../../docs/theory/friction.md)
