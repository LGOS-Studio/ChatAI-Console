# main.py
import sys
import config
from engine.brain import Brain
from utils.logger import setup_logger

def main():
    logger = setup_logger("Main")
    print("===================================")
    print("  LGOS Studio AI Console v1.1.3")
    print("  Type 'quit' to exit.")
    print("===================================")
    
    # 初始化大脑
    try:
        ai = Brain()
    except Exception as e:
        logger.critical(f"Failed to initialize AI: {e}", exc_info=True)
        return

    # 交互循环
    while True:
        try:
            user_input = input(config.PROMPT).strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in config.EXIT_COMMANDS:
                print("ChatAI: 再见！")
                break
            
            # 思考并生成回复
            response = ai.process(user_input)
            print(f"ChatAI: {response}")
            
        except KeyboardInterrupt:
            print("\nChatAI: 检测到中断，再见。")
            break
        except Exception as e:
            logger.error(f"Main loop error: {e}", exc_info=True)
            print("ChatAI: 发生了一个内部错误。")

if __name__ == "__main__":
    main()