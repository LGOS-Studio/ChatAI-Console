# skills/math_skill.py
from skills.base_skill import BaseSkill
import re

class MathSkill(BaseSkill):
    name = "Calculator"
    intents = ['CALCULATE']
    
    def execute(self, user_input, keywords, context):
        # 安全计算：提取数字和运算符
        try:
            # 简单提取算式 (实际项目中这里需要写 700+ 行来处理各种数学逻辑和 AST 抽象语法树)
            # 这里仅做演示，禁止直接 eval 不受信任的输入！
            exp = re.findall(r'[\d+\-*/.()]+', user_input)
            if exp:
                # 这里为了安全，我们只做简单的四则运算解析，或者用 ast.literal_eval 的复杂版
                # 为了演示原生库能力，我们用简单的 eval (生产环境需替换)
                result = eval(exp[0]) 
                return f"计算结果是：{result}"
            return "我没找到需要计算的式子，请告诉我比如：1+1等于几"
        except:
            return "这题太难了，我算不过来..."