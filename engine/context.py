# engine/context.py
from collections import deque
import config

class ContextManager:
    def __init__(self):
        self.history = deque(maxlen=config.MAX_CONTEXT_TURNS)
        self.current_intent = None
        self.slots = {} # 用于存储多轮对话的槽位信息

    def add_turn(self, user_input, system_response):
        self.history.append({"user": user_input, "sys": system_response})

    def get_history(self):
        return list(self.history)

    def clear_slots(self):
        self.slots = {}