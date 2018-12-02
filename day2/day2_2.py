file =open ("day2.txt","r")
words = file.read().split("\n")
def inCommon(a,b):
	u=zip(a,b)
	count = 0
	for i,j in u:
		if i!=j:
			count+=1
	return count
for i in range(0,len(words)):
	for j in range(0,len(words)):
		if inCommon(words[i],words[j]) == 1:
			print("hmm")
			print(words[i])
			print(words[j])