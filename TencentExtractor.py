#encoding=utf-8
import os
import sys
import json


class TencentExtractor:
	def __init__(self):
		self.openkgPath = "/home/zhengyi_ma/weiboXG/codes/worddict/openKG.dic"
		self.tencentPath = "/home/zhengyi_ma/TencentEmb/Tencent_AILab_ChineseEmbedding.txt"
		self.outpath = "/home/zhengyi_ma/weiboXG/codes/worddict/openKG_keywords_Tencent.txt"

		# self.tencentPath = "/home/zhengyi_ma/weiboXG/codes/worddict/openKG_keywords_Tencent2.txt"
		# self.outpath = "/home/zhengyi_ma/weiboXG/codes/worddict/openKG_keywords_Tencent3.txt"		

		self.worddict = []
	
	
	def addTencentWords(self):
		f = open(self.tencentPath)
		
		cnt = 0
		for line in f:
			
			# if cnt == 1075504:
			# 	cnt += 1
			# 	continue
			# fw = open("test.w","w")
			# fw.write(str(cnt))
			# fw.close()
			self.worddict.append(line)
			cnt += 1
			print(cnt)
		
		# for line in open(self.openkgPath):
		# 	line = line.strip()
		# 	self.worddict[line] = 1
			
			
	
	def writeDict(self):
		f = open(self.outpath,"w")
		for k in self.worddict:
			f.write(k)
		f.close()

			

def main():
	kge = TencentExtractor()

	kge.addTencentWords()
	# kge.writeDict()
	

main()