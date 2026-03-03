# skills/skill_loader.py
import os
import importlib.util
import config
from skills.base_skill import BaseSkill
from utils.logger import setup_logger

class SkillLoader:
    def __init__(self):
        self.logger = setup_logger("SkillLoader")
        # 核心修改：字典的值从单个技能 改为 技能列表
        self.skill_registry = {}
        self._load_skills()

    def _load_skills(self):
        """动态加载 skills 目录下所有继承 BaseSkill 的类"""
        skill_dir = config.SKILLS_DIR
        
        for filename in os.listdir(skill_dir):
            if filename.endswith('.py') and filename not in ['__init__.py', 'base_skill.py', 'skill_loader.py']:
                module_name = filename[:-3]
                file_path = os.path.join(skill_dir, filename)
                
                # 动态导入模块
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # 查找模块中的 Skill 类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, BaseSkill) and attr is not BaseSkill:
                        # 核心修改：支持多技能注册，不再覆盖，而是追加到列表
                        if hasattr(attr, 'intents'):
                            skill_instance = attr()
                            for intent in attr.intents:
                                if intent not in self.skill_registry:
                                    self.skill_registry[intent] = []
                                # 把技能加入对应意图的列表
                                self.skill_registry[intent].append(skill_instance)
                                self.logger.info(f"Loaded skill: {attr.__name__} for intent: {intent}")

    def get_skills(self, intent):
        """获取对应意图的所有技能列表，没有则返回空列表"""
        return self.skill_registry.get(intent, [])