# 训练词向量
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus, LineSentence
from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec
from tqdm import tqdm

# sentences = Text8Corpus(datapath('/home/zhengyi_ma/weiboXG/codes/weibocorpus2'))
# print(list(sentences)[0][:10])

# f = open('/home/zhengyi_ma/weiboXG/codes/weibocorpus2')
# f = open('/home/zhengyi_ma/weiboXG/codes/weibocorpus37G')
# sentences = []
# for line in tqdm(f):
#     sent = line.split()
#     sentences.append(sent)

# f.close()
sentences = LineSentence(datapath('/home/zhengyi_ma/weiboXG/codes/wechatcorpus'))
print("line sentence load success!")
phrases = Phrases(sentences)
print("phrases training success!")
# for phrase, score in phrases.export_phrases(sentences):
#     print(phrase, score)

# f = open("weibocorpus2_phrase","w")
# bigram = Phraser(phrases)
# for sent in bigram[sentences]:
#     f.write(" ".join(sent))

# f.close()
model = Word2Vec(phrases[sentences])
model.save("/home/zhengyi_ma/weiboXG/codes/wechat_phrase_withlargevocab.bin")