# config.py
import os

# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SKILLS_DIR = os.path.join(BASE_DIR, 'skills')

# NLP 配置
KEYWORD_MIN_LENGTH = 2
MAX_CONTEXT_TURNS = 10

# 交互配置
PROMPT = "用户（请输入）:  "
EXIT_COMMANDS = ['quit', 'exit', 'q', '再见']

# 日志配置
LOG_LEVEL = "INFO"