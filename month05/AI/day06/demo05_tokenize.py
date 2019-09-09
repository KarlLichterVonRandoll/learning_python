"""
分词器 文本分词
"""
import nltk.tokenize as tk

doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)

# 把样本按句子进行拆分  sent_list:句子列表
tokens = tk.sent_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
print('-' * 15)
# 把样本按单词进行拆分  word_list:单词列表
tokens = tk.word_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
print('-' * 15)
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
