# skills/run_skill.py
import subprocess
import re
from skills.base_skill import BaseSkill

class RunCommandSkill(BaseSkill):
    name = "Windows Command Runner"
    intents = ['RUN_COMMAND', 'CHAT']  # 同时监听两个意图
    
    # 危险命令列表
    DANGER_KEYWORDS = [
        'del', 'rmdir', 'rd', 'erase', 'format', 
        'diskpart', 'reg', 'shutdown', 'taskkill',
        'powershell -noexit', 'iex', 'Invoke-Expression'
    ]
    
    # 确认关键词
    CONFIRM_WORDS = ['我已知晓风险，继续执行', 'continue', '确认执行', '继续']
    CANCEL_WORDS = ['取消', 'cancel', '算了', '不执行']

    def execute(self, user_input, keywords, context):
        # 优先检查：是否处于"待确认"状态？
        pending_cmd = context.slots.get('pending_danger_cmd')
        
        if pending_cmd:
            return self._handle_confirmation(user_input, context)

        # 正常流程：提取并检查命令
        command = self._extract_command(user_input)
        
        if not command:
            # 没有要执行的命令，返回None，让下一个技能（ChatSkill）处理
            return None 

        # 检查是否危险
        if self._is_dangerous(command):
            # 暂存命令到上下文
            context.slots['pending_danger_cmd'] = command
            return (
                f"⚠️ 安全警告 ⚠️\n"
                f"检测到以下命令可能包含风险操作：\n"
                f">>> {command}\n\n"
                f"请确认：\n"
                f" - 输入「我已知晓风险，继续执行」或「continue」来执行\n"
                f" - 输入其他内容或「取消」来终止操作"
            )
        else:
            # 安全命令，直接执行
            return self._run_cmd(command)

    def _handle_confirmation(self, user_input, context):
        """处理用户的确认回复"""
        command = context.slots.get('pending_danger_cmd')
        user_resp = user_input.strip().lower()
        
        # 清空状态
        context.clear_slots()
        
        if any(word.lower() in user_resp for word in self.CONFIRM_WORDS):
            # 用户确认了，执行
            return f"正在执行命令...\n{self._run_cmd(command)}"
        else:
            # 用户取消或没说确认词
            return "已取消执行该命令。"

    def _extract_command(self, text):
        match = re.search(r'(?:执行|运行|cmd|敲入|输入命令|打开)\s*(.*)', text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return None

    def _is_dangerous(self, command):
        cmd_lower = command.lower()
        for keyword in self.DANGER_KEYWORDS:
            if keyword in cmd_lower:
                return True
        return False

    def _run_cmd(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='gbk',
                errors='ignore'
            )

            output = "--- 命令执行结果 ---\n"
            if result.stdout:
                output += f"[标准输出]\n{result.stdout}\n"
            if result.stderr:
                output += f"[错误信息]\n{result.stderr}\n"
            
            if not result.stdout and not result.stderr:
                output += "命令执行完毕，无输出内容。"
                
            return output
        except Exception as e:
            return f"执行出错：{str(e)}"