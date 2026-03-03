# engine/brain.py
from engine.nlp_core import NLPEngine
from engine.context import ContextManager
from skills.skill_loader import SkillLoader
from utils.logger import setup_logger

class Brain:
    def __init__(self):
        self.logger = setup_logger("Brain")
        self.nlp = NLPEngine()
        self.ctx = ContextManager()
        self.skills = SkillLoader()
        
        self.logger.info("LGOS Studio AI Brain initialized.")

    def process(self, user_input):
        self.logger.debug(f"Processing input: {user_input}")
        
        # 1. NLP 处理
        keywords = self.nlp.extract_keywords(user_input)
        intent = self.nlp.classify_intent(user_input, keywords)
        
        self.logger.info(f"Intent: {intent}, Keywords: {keywords}")
        
        # 2. 核心修改：获取该意图下的所有技能，按顺序执行
        skill_list = self.skills.get_skills(intent)
        response = None

        # 遍历所有技能，直到拿到非None的有效回复
        for skill in skill_list:
            try:
                self.logger.debug(f"Trying skill: {skill.name}")
                skill_response = skill.execute(user_input, keywords, self.ctx)
                if skill_response is not None:
                    response = skill_response
                    self.logger.debug(f"Skill {skill.name} returned valid response.")
                    break  # 拿到有效回复，停止遍历
            except Exception as e:
                self.logger.error(f"Skill {skill.name} execution error: {e}", exc_info=True)
                continue

        # 3. 终极兜底：如果所有技能都没返回有效内容，强制用默认回复
        if not response:
            self.logger.warning("All skills returned None, using default fallback.")
            response = "抱歉，我不太理解你的意思，可以换个说法吗？"

        # 4. 更新上下文
        self.ctx.add_turn(user_input, response)
        
        return response