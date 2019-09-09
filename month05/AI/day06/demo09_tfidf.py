"""
词袋模型
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import numpy as np

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
# 生成tfidf
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(np.round(tfidf.toarray(), 2))