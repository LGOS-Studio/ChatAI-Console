# engine/nlp_core.py
import re
import os
import config
from utils.text_utils import TextCleaner
from collections import Counter, defaultdict
import math

class NLPEngine:
    def __init__(self):
        self.stopwords = self._load_stopwords()
        
    def _load_stopwords(self):
        path = os.path.join(config.DATA_DIR, 'stopwords.txt')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return set([line.strip() for line in f if line.strip()])
        return set()

    def extract_keywords(self, text, top_k=5):
        """
        关键词提取逻辑：
        1. 清洗
        2. 分词 (简单的中文按字/英文按空格，或基于正则的n-gram)
        3. 去除停用词
        4. 基于词频和位置加权
        """
        clean_text = TextCleaner.to_lower(text)
        clean_text = TextCleaner.remove_punctuation(clean_text)
        
        # 简单分词策略：中文单字 + 英文单词
        words = []
        # 提取英文单词
        english_words = re.findall(r'[a-zA-Z]+', clean_text)
        words.extend(english_words)
        
        # 提取中文序列并进行 n-gram 切分 (这里演示 1-gram 和 2-gram)
        chinese_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
        words.extend(chinese_chars) # 1-gram
        
        # 简单 2-gram 组合
        if len(chinese_chars) > 1:
            bigrams = [''.join(chinese_chars[i:i+2]) for i in range(len(chinese_chars)-1)]
            words.extend(bigrams)

        # 过滤
        filtered = [w for w in words if w not in self.stopwords and len(w) >= config.KEYWORD_MIN_LENGTH]
        
        # 统计词频
        freq = Counter(filtered)
        
        # 简单排序返回
        return [item[0] for item in freq.most_common(top_k)]

    def classify_intent(self, text, keywords):
        """简单的意图分类"""
        text_lower = text.lower()
        
        # 1. 检测是否要执行命令
        if any(k in text_lower for k in ['执行', '运行', 'cmd', '敲入', '输入命令']):
            return 'RUN_COMMAND'
            
        # 2. 新增：检测关于 APP 的问题
        if any(k in text_lower for k in ['关于', '版本', '开发者', '谁做的', '技术栈', '介绍自己', '你是什么']):
            return 'ABOUT_APP'
            
        # 3. 时间
        if any(k in text_lower for k in ['时间', '几点', 'date', 'time']):
            return 'GET_TIME'
            
        # 4. 计算
        elif any(k in text_lower for k in ['算', '计算', '加', '减', '乘', '除', 'calc']):
            return 'CALCULATE'
            
        else:
            return 'CHAT'