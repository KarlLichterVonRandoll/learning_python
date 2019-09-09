"""
案例：主题识别（文本分类）
"""
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import numpy as np

train = sd.load_files(
    '../ml_data/20news',  encoding='latin1',
    shuffle=True, random_state=7)
train_x = np.array(train.data)   # 样本输入
train_y = np.array(train.target)  # 样本输出 [0,1,2,0,1,1..]
categories = train.target_names
print(train_x.shape, train_y.shape)
print(categories)

# 整理样本，获取tfidf矩阵，训练模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(train_x)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(tfidf.shape)
# 使用基于多项分布的朴素贝叶斯训练模型
model = nb.MultinomialNB()
model.fit(tfidf, train_y)

# 预测：
test_data = [
    'The curveballs of right handed pitchers '
    'tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
test_bow = cv.transform(test_data)
test_tfidf = tt.transform(test_bow)
pred_y = model.predict(test_tfidf)

for sent, index in zip(test_data, pred_y):
    print(sent, '->', categories[index])
    