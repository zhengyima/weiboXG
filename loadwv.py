#encoding=utf-8
# from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
# from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec
# from tqdm import tqdm
import gensim
from tqdm import tqdm
# import jieba
# import jieba.posseg as pseg
# jieba.load_userdict("/home/zhengyi_ma/weiboXG/codes/worddict/openKG.dic")

# print(' '.join(jieba.cut("李文亮八君子", HMM=True)))
# model = Word2Vec.load("/home/zhengyi_ma/weiboXG/codes/weibo2_phrase.bin")
# model_ncov = Word2Vec.load("/home/zhengyi_ma/weiboXG/codes/weibo2_phrase.bin")

# vector = model.wv['一省包一市']
# print(vector)
# print(model.most_similar(positive='武汉',topn=10))
f = open("/home/zhengyi_ma/weiboXG/codes/worddict/KG_weibo_vocab.txt","w")

model_weibo = gensim.models.KeyedVectors.load_word2vec_format("/home/zhengyi_ma/weibo_100.bin", binary=True, unicode_errors='ignore')
print(len(model_weibo.vocab))
print(model_weibo.vocab['C罗'])
cnt = 0
for w in tqdm(model_weibo.vocab):
    f.write(w+"\n")
    cnt += 1
    # if cnt >= 500:
    #     break

f_src=  open("/home/zhengyi_ma/weiboXG/codes/worddict/openKG.dic")

for w in f_src:
    f.write(w.strip()+"\n")
    
f_src.close()

f.close()
