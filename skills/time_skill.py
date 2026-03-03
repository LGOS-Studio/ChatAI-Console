# skills/time_skill.py
from skills.base_skill import BaseSkill
from datetime import datetime

class TimeSkill(BaseSkill):
    name = "Time Query"
    intents = ['GET_TIME'] # 绑定的意图
    
    def execute(self, user_input, keywords, context):
        now = datetime.now()
        time_str = now.strftime("%Y年%m月%d日 %H:%M:%S")
        return f"现在的时间是：{time_str}"