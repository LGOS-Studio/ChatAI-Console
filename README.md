# LGOS AI Console

一个基于 Python 原生库开发的轻量级命令行智能助手，支持模块化技能扩展、Windows 命令执行、上下文记忆等核心功能，无第三方依赖，开箱即用。

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

## 🌟 核心特性
- **纯原生开发**：仅使用 Python 标准库，无需安装额外依赖
- **模块化架构**：技能插件化设计，可快速扩展新功能
- **多技能支持**：内置闲聊、时间查询、数学计算、系统命令执行、AI 介绍等技能
- **安全防护**：危险命令执行前二次确认，避免误操作
- **上下文记忆**：支持多轮对话上下文管理
- **日志系统**：完整的日志记录，方便调试和问题定位

## 📋 功能清单
| 技能名称 | 触发关键词 | 功能描述 |
|---------|-----------|---------|
| 闲聊技能 | 你好、再见、开心、难过等日常用语 | 基于关键词匹配的自然闲聊，支持 500+ 问答库 |
| 时间技能 | 时间、几点、日期、现在 | 实时获取系统当前时间和日期 |
| 计算技能 | 算、计算、加、减、乘、除 | 支持基础数学运算 |
| 命令执行 | 执行、运行、cmd、输入命令 | 执行 Windows 系统命令，危险命令需二次确认 |
| AI 介绍 | 关于、版本、开发者、技术栈 | 展示 AI 版本、开发者、技术架构等信息 |

## 🚀 快速开始

### 环境要求
- Python 3.8 及以上版本
- Windows 操作系统（命令执行功能当前版本仅适配 Windows）

### 安装与运行
1. 克隆仓库
```bash
git clone https://github.com/LGOS-Studio/ChatAI-Console.git
cd ChatAI-Console
```

2. 直接运行（无需安装依赖）
```bash
python main.py
```

3. 开始使用
```
===================================
  LGOS Studio AI Console v1.1.3
  Type 'quit' to exit.
===================================
用户（请输入）: 你好
ChatAI: 你好呀！我是 ChatAI，很高兴为你服务。
```

## 📖 使用示例

### 基础闲聊
```
用户（请输入）: 早上好
ChatAI: 早上好！新的一天要元气满满哦。

用户（请输入）: 我好开心
ChatAI: 听到你开心我也很开心！
```

### 时间查询
```
用户（请输入）: 现在几点了
ChatAI: 现在的时间是：2026年03月03日 19:00:00
```

### 数学计算
```
用户（请输入）: 算一下 100+200*3
ChatAI: 计算结果是：700
```

### 执行系统命令
```
用户（请输入）: 执行 ipconfig
ChatAI: --- 命令执行结果 ---
[标准输出]
Windows IP 配置
... (网卡信息) ...

用户（请输入）: 执行 shutdown -s -t 60
ChatAI: ⚠️ 安全警告 ⚠️
检测到以下命令可能包含风险操作：
>>> shutdown -s -t 60

请确认：
 - 输入「我已知晓风险，继续执行」或「continue」来执行
 - 输入其他内容或「取消」来终止操作

用户（请输入）: continue
ChatAI: 正在执行命令...
--- 命令执行结果 ---
[标准输出]
成功地安排了关机。
```

### 查看 AI 信息
```
用户（请输入）: 介绍一下你自己
ChatAI: 📋 LGOS AI Console 完整介绍
━━━━━━━━━━━━━━━━━━━━━━━━
• 名称：LGOS AI Console
• 版本：1.0.0
• 开发者：LGOS Studio
• 构建时间：2026-03

💡 核心特性：
1. 纯 Python 原生库开发，无第三方依赖
2. 模块化设计，支持 Skills 插件扩展
...
```
### ***注意：此对话示例不代表实际使用效果，仅供参考***

## 🛠️ 项目结构
```
ChatAI-Console/
├── data/                  # 数据目录
│   └── knowledge_base.json # 闲聊问答库
├── engine/                # 核心引擎
│   ├── brain.py           # 技能调度核心
│   ├── context.py         # 上下文管理器
│   └── nlp_core.py        # 自然语言处理
├── skills/                # 技能模块
│   ├── base_skill.py      # 技能基类
│   ├── about_skill.py     # AI 介绍技能
│   ├── chat_skill.py      # 闲聊技能
│   ├── math_skill.py      # 计算技能
│   ├── run_skill.py       # 命令执行技能
│   ├── skill_loader.py    # 技能加载器
│   └── time_skill.py      # 时间技能
├── utils/                 # 工具类
│   ├── __init__.py
│   ├── logger.py          # 日志工具
│   └── text_utils.py      # 文本处理工具
├── config.py              # 配置文件
├── main.py                # 主程序入口
├── LICENSE                # MIT 许可证
└── README.md              # 项目说明
```

## 🧩 扩展自定义技能
1. 在 `skills` 目录下创建新的技能文件（如 `weather_skill.py`）
2. 继承 `BaseSkill` 基类，实现 `execute` 方法
3. 注册意图（intents），在 `nlp_core.py` 中添加意图识别规则
4. 重启程序，自动加载新技能

示例：
```python
# skills/weather_skill.py
from skills.base_skill import BaseSkill

class WeatherSkill(BaseSkill):
    name = "Weather Query"
    intents = ['GET_WEATHER']
    
    def execute(self, user_input, keywords, context):
        return "暂时还不支持天气查询，你可以扩展这个技能！"
```

## 🧩 扩展自定义知识库
1. 在 `data/knowledge_base.json` 文件下根据示例创建新的json代码并保存
2. 重新加载程序，新知识库会自动读取并加载

示例：
```json
"关键词": [
  "回答1（可选）",
  "回答2（可选）",
  "回答3（可选）",
  "扩展更多回答...（可选）", 
  "回答N（必选）"
]
```

## 投稿方式
- 你可以通过[Pull Requests](https://github.com/LGOS-Studio/ChatAI-Console/pulls)的方式投稿你的自定义插件与知识库文件
- 如果你不想复制整个仓库，你也可以使用[Issues](https://github.com/LGOS-Studio/ChatAI-Console/issues/new)的方式投稿你的skills或 知识库json代码

## 📄 许可证
本项目采用 MIT 许可证开源 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢
- Python 官方文档提供的标准库支持
- 所有为开源社区做出贡献的开发者
- 测试软件的你

## 📞 联系我们
- 开发者：LGOS Studio
- 软件版本：v1.1.3
- 构建时间：2026-03
- 此文件版本：1.0.0

## Bug反馈
- 如果你要反馈Bug，可以选择[Issues](https://github.com/LGOS-Studio/ChatAI-Console/issues/new)的方式，我们会尽可能修复这些Bug

---
