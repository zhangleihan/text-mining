import json


def main():
	with open('comments_multiple_json.json','r',encoding='utf-8') as f:
	    punctuation = []
	    wordcount = {}
	    for line in f:
	        comment_obj = json.loads(line)
	        comment_text = comment_obj['comments']
	        for c in comment_text:
	            i = ord(c)
	            if ((i >= 33 and i <= 47) or (i >= 58 and i <= 64) or (i >= 91 and i <= 96) or (i >= 123 and i <= 126)):
	                punctuation.append(c)
	                comment_text = comment_text.replace(c, ' ').strip()
	        words = comment_text.split(' ')
	        for word in words:
	            if len(word) == 0:
	                continue
	            if word not in wordcount:
	                wordcount[word]=1
	            else:
	                wordcount[word]+=1 
	print('标点符号包括：\n')
	print(set(punctuation))

	print('\n词频统计：\n')
	print(json.dumps(wordcount))

	print('\n词频统计(降序)：\n')
	print(sorted(wordcount.items(), key = lambda item:item[1], reverse = True))

if __name__ == '__main__':
	main()