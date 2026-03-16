import regex
from transformers import AutoTokenizer
class SindhiTokenizer:
    def __init__(self, model_path="aakashMeghwar01/SindhiLM-Tokenizer-v1"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        # V3 Regex Shield
        self.pre_tok_regex = regex.compile(r"(?x)(?:[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]*(?:جھ|گھ|کھ|دھ|بھ|پھ|تھ|لھ|مھ|نھ|رھ|وھ)[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]*)|[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]+|[a-zA-Z]+|\d+|[^\s\w]")
    def tokenize(self, text):
        units = self.pre_tok_regex.findall(text)
        final_tokens = []
        for unit in units:
            ids = self.tokenizer.encode(unit, add_special_tokens=False)
            t_list = [self.tokenizer.decode([i]).strip() for i in ids]
            # Anti-shatter logic: if too many tokens for a short word, keep it whole
            if (len(t_list) > 2 and len(unit) < 8) or any(len(t) == 1 for t in t_list if t not in "۾کي"):
                final_tokens.append(unit)
            else:
                final_tokens.extend([t for t in t_list if t])
        return final_tokens