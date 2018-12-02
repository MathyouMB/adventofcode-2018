file =open ("day2.txt","r")
words = file.read().split("\n")
results = []
def countWord(s):
	commonletters = {}
	for k in range(0,len(s)):
		if s[k] in commonletters.keys():
			commonletters[s[k]] +=1
		else:
			commonletters[s[k]] =1
	return(commonletters)

for i in range(0,len(words)):
	results.append(countWord(words[i]).values())

count2 = 0
count3 = 0
for i in range(0,len(results)):
	if 2 in results[i]:
		count2+=1
	if 3 in results[i]:
		count3+=1
print(count2)
print(count3)
print(count2*count3)