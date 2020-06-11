#encoding=utf-8
import os
import sys
import urllib.parse
import json
from tqdm import tqdm
# 从各种知识图谱，其他材料中提取实体，输出词典

class KGExtractor:
	def __init__(self):
		self.baidubaikePath = "/home/zhengyi_ma/weiboXG/openKG/2019nCoV-baidubaike/baidubaike_infobox.nt"
		self.hudongPath = "/home/zhengyi_ma/weiboXG/openKG/2019nCoV-新冠hudongbaike/hudongbaike_infobox.nt"
		self.wikiPath = "/home/zhengyi_ma/weiboXG/openKG/2019nCoV-新冠znwiki/znwiki_infobox.nt"
		self.medicaldir = "/home/zhengyi_ma/weiboXG/openKG/medical/"
		self.herodir = "/home/zhengyi_ma/weiboXG/openKG/hero/"
		self.eventdir = "/home/zhengyi_ma/weiboXG/openKG/event/"
		self.healthdir = "/home/zhengyi_ma/weiboXG/openKG/health/"
		self.keywordpath = "/home/zhengyi_ma/weiboXG/codes/worddict/keyword0.1.csv"
		self.tencentPath = "/home/zhengyi_ma/TencentEmb/Tencent_AILab_ChineseEmbedding.txt"
		self.outpath = "/home/zhengyi_ma/weiboXG/codes/worddict/openKG_keywords_Tencent.txt"

		self.worddict = {}
	def extractFromBaidubaike(self):
		f = open(self.baidubaikePath,"r")
		for line in f:
			try:
				en1, prop, en2  = line.split()
			except:
				# print(line.split())
				triplets = line.split()
				en2 = ' '.join(triplets[2:])
				en1 = triplets[0]
				prop = triplets[1]
			en1 = en1.replace("<http://www.openkg.cn/2019-nCoV/baidubaike/resource/","").replace(">","")
			en1 = urllib.parse.unquote(en1)
			prop = prop.replace("<http://www.openkg.cn/2019-nCoV/baidubaike/property/","").replace(">","")
			prop = urllib.parse.unquote(prop)
			en2 = en1.replace("<http://www.openkg.cn/2019-nCoV/baidubaike/resource/","").replace(">","")
			en2 = urllib.parse.unquote(en2)
			print(en1,en2,prop)
			self.worddict[en1] = 1
			self.worddict[en2] = 1

	def extractFromhudong(self):
		f = open(self.hudongPath,"r")
		for line in f:
			try:
				en1, prop, en2  = line.split()
			except:
				# print(line.split())
				triplets = line.split()
				en2 = ' '.join(triplets[2:])
				en1 = triplets[0]
				prop = triplets[1]
			en1 = en1.replace("<http://www.openkg.cn/2019-nCoV/hudongbaike/resource/","").replace(">","")
			en1 = urllib.parse.unquote(en1)
			prop = prop.replace("<http://www.openkg.cn/2019-nCoV/hudongbaike/property/","").replace(">","")
			prop = urllib.parse.unquote(prop)
			en2 = en1.replace("<http://www.openkg.cn/2019-nCoV/hudongbaike/resource/","").replace(">","")
			en2 = urllib.parse.unquote(en2)
			# print(en1,en2,prop)
			self.worddict[en1] = 1
			self.worddict[en2] = 1	

	def extractFromWiki(self):
		f = open(self.wikiPath,"r")
		for line in f:
			try:
				en1, prop, en2  = line.split()
			except:
				# print(line.split())
				triplets = line.split()
				en2 = ' '.join(triplets[2:])
				en1 = triplets[0]
				prop = triplets[1]
			en1 = en1.replace("<http://www.openkg.cn/2019-nCoV/znwiki/resource/","").replace(">","")
			en1 = urllib.parse.unquote(en1)
			prop = prop.replace("<http://www.openkg.cn/2019-nCoV/znwiki/property/","").replace(">","")
			prop = urllib.parse.unquote(prop)
			en2 = en1.replace("<http://www.openkg.cn/2019-nCoV/znwiki/resource/","").replace(">","")
			en2 = urllib.parse.unquote(en2)
			# print(en1,en2,prop)
			self.worddict[en1] = 1
			self.worddict[en2] = 1	

	def extractHeroes(self):
		heros = ["钟南山","刘大庆","张新忠","崔嵬","张文宏","曾文聪","于正洲","邓少华",\
			"李兰娟","何建华","梁医生","黄汉明","张定宇","苏莱曼·巴马丁","毛样洪","姜娜",\
			"张继先","宋英杰","陈在华","蒋金波","胡锋","程建阳","李弦梁","武东","马承武","孙训祥","尹祖川","张新忠","章良志",\
	 			"张辉","李文亮"]	
		for h in heros:
			self.worddict[h] = 1

		jsonpath = os.path.join(self.herodir,"character-2019ncov-v0.1.json")
		with open(jsonpath,'r') as load_f:
			load_dict = json.load(load_f)
		# print(load_dict)
		# for k in load_dict:
		# 	print(k)
		graph = load_dict["@graph"]
		# print(len(graph))
		for e in graph:
			if "http://www.openkg.cn/2019-nCoV/character/resource" in e["@id"]:
				# print(e["label"]["@value"])
				self.worddict[e["label"]["@value"]] = 1		

	def extractMedical(self):
		jsonpath = os.path.join(self.medicaldir,"medical-2019ncov-v0.1.json")
		with open(jsonpath,'r') as load_f:
			load_dict = json.load(load_f)
		# print(load_dict)
		# for k in load_dict:
		# 	print(k)
		graph = load_dict["@graph"]
		# print(len(graph))
		for e in graph:
			if "http://www.openkg.cn/2019-nCoV/medical/resource/" in e["@id"]:
				self.worddict[e["label"]["@value"]] = 1
		
	def extractEvent(self):
		jsonpath = os.path.join(self.eventdir,"event-2019ncov-v0.1.json")
		with open(jsonpath,'r') as load_f:
			load_dict = json.load(load_f)
		# print(load_dict)
		# for k in load_dict:
		# 	print(k)
		graph = load_dict["@graph"]
		# print(len(graph))
		for e in graph:
			if "http://www.openkg.cn/2019-nCoV/event/resource/" in e["@id"]:
				self.worddict[e["label"]["@value"]] = 1
				# print(e["label"]["@value"])
	
	def extractHealth(self):
		jsonpath = os.path.join(self.healthdir,"medical-knowledge-graph-4.3.json")
		with open(jsonpath,'r') as load_f:
			load_dict = json.load(load_f)
		# print(load_dict)
		# for k in load_dict:
		# 	print(k)
		# graph = load_dict["@graph"]
		# print(len(graph))
		for e in load_dict:
			for k in e:
				if "rdf-schema" in k:
					arr = e[k]
					for item in arr:
						if "@value" in item:
							# print(item["@value"])
							self.worddict[item["@value"]] = 1
			# if "http://www.openkg.cn/2019-nCoV/event/resource/" in e["@id"]:
			# 	self.worddict[e["label"]["@value"]] = 1
			# 	print(e["label"]["@value"])
	def addkeywords(self):
		f = open(self.keywordpath)
		for line in f:
			cols = line.split(",")
			# print(cols[1])
			self.worddict[cols[1]] = 1
	
	def addTencentWords(self):
		f = open(self.tencentPath)
		cnt = 0
		for line in f:
			word = line.split()[0]
			# print(word)

			self.worddict[word] = 1
			cnt += 1
			print(cnt)
			
	
	def writeDict(self):
		f = open(self.outpath,"w")
		for k in self.worddict:
			f.write(k+"\n")
		f.close()
	
		
		
			

def main():
	kge = KGExtractor()
	kge.extractFromBaidubaike()
	kge.extractFromhudong()
	kge.extractFromWiki()
	kge.extractHeroes()
	kge.extractMedical()
	kge.extractHeroes()
	kge.extractEvent()
	kge.extractHealth()
	kge.addkeywords()
	cnt = 0
	for k in kge.worddict:
		cnt += 1
	print(cnt)
	# kge.addTencentWords()
	kge.writeDict()
	

main()