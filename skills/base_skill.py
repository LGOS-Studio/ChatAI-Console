# skills/base_skill.py
from abc import ABC, abstractmethod

class BaseSkill(ABC):
    name = "Unknown"
    description = "Base class for skills"
    
    @abstractmethod
    def execute(self, user_input, keywords, context):
        pass