"""
词干提取
文本样本中的单词的词性与时态对于语义分析并无太大影响，所以需要对单词进行词干提取。
"""
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
pt_stemmer = pt.PorterStemmer()
lc_stemmer = lc.LancasterStemmer()
sb_stemmer = sb.SnowballStemmer('english')
for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print('%8s %8s %8s %8s' % (
        word, pt_stem, lc_stem, sb_stem))
