# skills/chat_skill.py
from skills.base_skill import BaseSkill
import random
import json
import os
import config

class ChatSkill(BaseSkill):
    name = "Casual Chat"
    intents = ['CHAT']
    
    def __init__(self):
        self.qas = self._load_kb()
        
    def _load_kb(self):
        path = os.path.join(config.DATA_DIR, 'knowledge_base.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def execute(self, user_input, keywords, context):
        # 简单的关键词匹配回复
        for q, a_list in self.qas.items():
            if q in user_input:
                return random.choice(a_list)
        
        # 默认回复
        defaults = [
            "我不太理解你的意思，但我正在学习中。",
            "有意思，能详细说说吗？",
            "收到，虽然我不太懂，但我会记下来的。",
            "这是一个有趣的话题。"
        ]
        return random.choice(defaults)