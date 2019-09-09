"""
词袋模型
一句话的语义很大程度取决于某个单词出现的次数，所以可以把句子中所有可能出现的单词作为特征名，
每一个句子为一个样本，单词在句子中出现的次数为特征值构建数学模型，称为词袋模型。
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
    'The black dog is in the black room. ' \
    'Running in the room is forbidden. '
print(doc)
# 拆分3个句子，每句话为一个样本
sents = tk.sent_tokenize(doc)
cv = ft.CountVectorizer()
bow = cv.fit_transform(sents)
print(bow.toarray())
print(cv.get_feature_names())