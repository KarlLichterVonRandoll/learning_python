"""
电影评论情感分析
分析语料库中movie_reviews文档，通过正面及负面评价进行自然语言训练，实现情感分析。
"""
import nltk.classify as cf
import nltk.corpus as nc
import nltk.classify.util as cu

"""
[ ({'age': 15, 'score1': 95, 'score2': 95}, 'good'),
  ({'age': 15, 'score1': 45, 'score2': 55}, 'bad') ]
"""
pdata = []
# movie_reviews下pos文件夹内所有文件的路径
fileids = nc.movie_reviews.fileids('pos')
# 整理所有正面评论单词，存入pdata列表
for fileid in fileids:
    words = nc.movie_reviews.words(fileid)
    sample = {}
    for word in words:
        sample[word] = True
    pdata.append((sample, 'POSITIVE'))

ndata = []
# movie_reviews下neg文件夹内所有文件的路径
fileids = nc.movie_reviews.fileids('neg')
# 整理所有反面评论单词，存入ndata列表
for fileid in fileids:
    words = nc.movie_reviews.words(fileid)
    sample = {}
    for word in words:
        sample[word] = True
    ndata.append((sample, 'NEGATIVE'))

# 整理训练集、测试集以及输入集与输出集
p_size, n_size = \
    int(len(pdata) * 0.8), int(len(ndata) * 0.8)

train_data = pdata[:p_size] + ndata[:n_size]
test_data = pdata[p_size:] + ndata[n_size:]

# 构建nltk自带的朴素贝叶斯分类器，训练模型
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)

# 样本测试
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']

for review in reviews:
    sample = {}
    words = review.split()
    for word in words:
        sample[word] = True
    pcls = model.classify(sample)
    print(review, '->', pcls)
