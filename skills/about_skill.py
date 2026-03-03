# skills/about_skill.py
from skills.base_skill import BaseSkill
import datetime

class AboutSkill(BaseSkill):
    name = "About LGOS AI"
    intents = ['ABOUT_APP']
    
    # 预设信息
    APP_NAME = "LGOS AI Console"
    VERSION = "1.1.3"
    DEVELOPER = "LGOS Studio"
    BUILD_DATE = "2026-03"
    FULL_UPDATE_LOG = f"""   1.优化系统稳定性，修复已知问题。
    2.增加 Windows 命令执行工具（***Required Microsoft Windows***），
使用方法：在想执行的命令前加入关键词“运行”
    3.增加“关于 {APP_NAME}”应用程序
    4.增加语言知识库（欢迎投稿，投稿地址：
https://github.com/LGOS-Studio/ChatAI-Console/issues/，
投稿格式：
[
  "Question": [
    "Answer1", （可选）
    "Answer2", （可选）
    "Answer3"
  ]
]
）
"""
    
    def execute(self, user_input, keywords, context):
        # 根据不同的关键词侧重点，返回略有不同的回答
        text_lower = user_input.lower()
        
        if any(k in text_lower for k in ['版本', 'version', '几号']):
            return self._get_version_info()
        elif any(k in text_lower for k in ['开发者', '谁做的', '开发', '制作']):
            return self._get_dev_info()
        elif any(k in text_lower for k in ['技术', '用什么写', 'python', '代码']):
            return self._get_tech_info()
        else:
            # 默认返回完整介绍
            return self._get_full_intro()

    def _get_full_intro(self):
        return f"""关于 {self.APP_NAME}
━━━━━━━━━━━━━━━━━━━━━━━━
• 名称：{self.APP_NAME}
• 开发者：{self.DEVELOPER}
• 构建时间：{self.BUILD_DATE}

**核心特性** ：
1. 纯 Python 原生库开发，无第三方依赖
2. 模块化设计，支持 Skills 插件扩展
3. 支持关键词提取与上下文记忆
4. 可执行 Windows 系统命令（部分命令需安全确认）

目前支持的技能：闲聊、查时间、数学计算、执行命令。

• 当前版本：{self.VERSION}，以下是该版本更新日志：

**
{self.FULL_UPDATE_LOG}
**
"""

    def _get_version_info(self):
        return f"{self.APP_NAME} 当前版本：**v{self.VERSION}** (Build {self.BUILD_DATE})"

    def _get_dev_info(self):
        return f"软件是由 **{self.DEVELOPER}** 开发的。感谢你的使用！"

    def _get_tech_info(self):
        return f"""**技术栈信息** ：
• 语言：Python 3
• 核心库：仅使用 Python 原生标准库 (subprocess, json, re, os 等)
• 架构：模块化设计 (Engine + Skills + Utils)
• 代码量：预计 7000+ 行
• 交互模式：命令行 (CLI)
"""