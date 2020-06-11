
#encoding=utf-8
#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
import os
# sys.path.append("../")
import jieba
import jieba.posseg as pseg
import json
#/home/zhengyi_ma/weiboXG/dataset/part-00011-cefb8d7b-df78-4ae0-bc03-031ac3b1135c-c000.json.gz
import gzip
from tqdm import tqdm
# 读json.gz数据，分词，输出为glove的输入文件

class gloveCorpusGenerator:

	def __init__(self):
		# self.worddictPath = "worddict/userdict.txt"
		# self.datadir = "/home/zhengyi_ma/weiboXG/dataset/"
		# jieba.load_userdict(self.worddictPath)
		# self.outpath = "./weibocorpus"
		# self.worddictPath = "worddict/openKG.dic"
		self.worddictPath = "worddict/KG_weibo_vocab.txt"
		# self.datadir = "/home/zhengyi_ma/weiboXG/dataset37G/output"
		# self.datadir = "/home/zhengyi_ma/weibo-original-200225/weibo-original-output"
		# self.datadir = "/home/zhengyi_ma/weiboXG/dataset37G/output/Date=2020-02-10/"
		self.datadir = "/home/zhengyi_ma/weiboXG/wechat-filter-output/"
		self.dir = False
		# self.dir = True
		jieba.load_userdict(self.worddictPath)
		# self.outpath = "./weibocorpus_Date=20200210"
		# self.worddictPath = "worddict/openKG_keywords_Tencent.txt"
		# self.datadir = "/home/zhengyi_ma/weiboXG/dataset/"
		# jieba.load_userdict(self.worddictPath)
		# self.outpath = "./weibocorpus3"
		# self.outpath = "./weibocorpus3_withlargevocab"
		# self.outpath = "./weibocorpus4_withrepose"
		# self.outpath = "./weibocorpus6_withrepost"
		self.outpath = "./wechatcorpus"

	def test(self):
		testlist = [
		('今天天气不错', ('今天', '天气')),
		('如果放到post中将出错。', ('中', '将')),
		('我们中出了一个叛徒', ('中', '出')),
		]

		for sent, seg in testlist:
			print('/'.join(jieba.cut(sent, HMM=True)))
			print("-"*40)
	
	def jsongzHandler(self, out_f, datapath):
		fp = gzip.open(datapath, 'rt', encoding='utf-8')
		for l in fp:
			# print(l)
			weibo = json.loads(l)
			# weiboText = (weibo["Text"] + weibo["DataS_r_weibo_content"]).strip().replace(" ","").replace("/","").replace("@","").replace("！","").replace("!","")\
			# .replace("?","").replace("？","").replace(":","").replace("：","").replace(",","").replace("，","").replace("[","").replace("]","")\
			# .replace(".","").replace("。","")
			# weiboText = (weibo["weibo_content"] + weibo["r_weibo_content"]).strip().replace(" ","").replace("/","").replace("@","").replace("！","").replace("!","")\
			# .replace("?","").replace("？","").replace(":","").replace("：","").replace(",","").replace("，","").replace("[","").replace("]","")\
			# .replace(".","").replace("。","")
			weiboText = (weibo["content"] ).strip().replace(" ","").replace("/","").replace("@","").replace("！","").replace("!","")\
			.replace("?","").replace("？","").replace(":","").replace("：","").replace(",","").replace("，","").replace("[","").replace("]","")\
			.replace(".","").replace("。","")

			weiboText_aftercut = ' '.join(jieba.cut(weiboText, HMM=True))
			out_f.write(weiboText_aftercut+"\n")
		fp.close()


	def genCorpus(self):
		jsondatas = os.listdir(self.datadir)
		corpusFile = self.outpath
		out_f = open(corpusFile,"w")

		if self.dir:
			for d in tqdm(jsondatas):
				dirPath = os.path.join(self.datadir, d)
				jsondatas2 = os.listdir(dirPath)
				for df in tqdm(jsondatas2):
					datapath = os.path.join(dirPath, df)
					# print(datapath)
					self.jsongzHandler(out_f, datapath) 
		else:
			for d in tqdm(jsondatas):
				datapath = os.path.join(self.datadir,d)
				# print(datapath)
				self.jsongzHandler(out_f, datapath)
		out_f.close()
	
def main():
	
	gcg = gloveCorpusGenerator()
	# gcg.test()

	# root_dir = "/home/zhengyi_ma/weiboXG/dataset37G/output"
	# dataset_by_days = os.listdir(root_dir)
	# for dbd in tqdm(dataset_by_days):
	# 	dataset_dir = os.path.join(root_dir, dbd)
	# 	gcg.datadir  = dataset_dir
	# 	# print(dbd)
	# 	gcg.outpath = os.path.join("/home/zhengyi_ma/weiboXG/dataset37_bydays/", dbd)
	# 	print(gcg.datadir)
	# 	print(gcg.outpath)
	# 	gcg.genCorpus()
		
	gcg.genCorpus()

main()
