#coding=utf-8
import os 
import json
import math
def is_chinese(string):
	"""
	检查整个字符串是否包含中文
	:param string: 需要检查的字符串
	:return: bool
	"""
	noisy_names = ["易烊","蔡徐坤","迪丽热巴","华晨宇","李现","谢娜","杨幂","刘诗诗","世勋","王源","鹿晗","黄子韬","笑cry","旦增尼玛","喵喵","粽粽","嗒嗒",'丨丨','艹艹']
	for nm in noisy_names:
		if nm in string.replace("_","").strip():
			return False 

	string = string.replace("万","").replace("亿","")
	for ch in string:
		if u'\u4e00' <= ch <= u'\u9fff':
			string_split = string.split("_")
			if len(string_split) > 1 and string_split[0].strip() != "" and string_split[1].strip() != "":
				return True
			# return True
	return False

class newWordsHandler:
	def __init__(self):
		self.datadir = "/home/zhengyi_ma/newwords/"
		filenames =  os.listdir(self.datadir)
		self.sortedFilenames = sorted(filenames)
		self.outputdir = "/home/zhengyi_ma/newwords2"



	def newWordsReward(self):
		oldwords = {}
		fn_cnt = 0
		for fn in self.sortedFilenames:
			
			data = json.loads(open(os.path.join(self.datadir, fn),'r').read())
			# for word_score in data:
			# 	word = word_score['word']
			# 	score = word_score['score']
			topn = 10
			delta = 3
			cnt = 0
			topnWordScores = []
			for i in range(len(data)):
				word = data[i]['word']
				score = data[i]['score']
				if not is_chinese(word):
					continue
				topnWordScores.append([word, score])
				if word in oldwords and fn_cnt - oldwords[word] <= delta:
					data[i]['score']  /= 2 
				cnt += 1

				oldwords[word] = fn_cnt
				
				if cnt == topn:
					break
			fn_cnt += 1

			result_out = sorted(data, key=lambda x: x['score'], reverse=True)
			fn_w = os.path.join(self.outputdir, fn)
			f_w = open(fn_w, "w")
			f_w.write(json.dumps(result_out,ensure_ascii=False))
			f_w.close()

			# for i in range(len(topnWordScores)):
			# 	word = topnWordScores[i][0]
			# 	score = topnWordScores[i][1]
			# 	if word in oldwords:


	def newWordsReward_Window(self):
		oldwords = {}
		fn_cnt = 0
		for fn in self.sortedFilenames:
			
			data = json.loads(open(os.path.join(self.datadir, fn),'r').read())
			# for word_score in data:
			# 	word = word_score['word']
			# 	score = word_score['score']
			topn = 10
			delta = 3
			cnt = 0
			windowSize = 8
			topnWordScores = []
			for i in range(len(data)):
				word = data[i]['word']
				score = data[i]['score']
				if not is_chinese(word):
					continue
				topnWordScores.append([word, score])
				if word in oldwords:
					scale = 0
					for last_cnt in oldwords[word]:
						if fn_cnt - last_cnt <= windowSize:
							scale += 1
					data[i]['score'] /= math.pow(2, scale)

				cnt += 1
				
				# oldwords[word] = fn_cnt

				if word not in oldwords:
					oldwords[word] = []
				oldwords[word].append(fn_cnt)

				
				if cnt == topn:
					break
			
			fn_cnt += 1
			
			newdata = []
			for d in data:
				if is_chinese(d['word']):
					newdata.append(d)
			# print()


			result_out = sorted(newdata, key=lambda x: x['score'], reverse=True)
			fn_w = os.path.join(self.outputdir, fn)
			f_w = open(fn_w, "w")
			f_w.write(json.dumps(result_out,ensure_ascii=False))
			f_w.close()

			# for i in range(len(topnWordScores)):
			# 	word = topnWordScores[i][0]
			# 	score = topnWordScores[i][1]
			# 	if word in oldwords:
			
			 
				



def main():
	nH = newWordsHandler()
	nH.newWordsReward_Window()

main()