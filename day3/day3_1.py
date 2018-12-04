file =open ("day3.txt","r")
words = file.read().split("\n")
results = []

def findBetween(s, f, l):
	startindex = s.find(f)
	endindex = startindex + len(f)
	lastindex = s.find(l)
	start = s.index(f) + len(f)
	end = s.index(l, start)
	return s[start:end]

def convert():
	squares = {}
	for i in range(0,len(words)):
		words[i] += ']'
		words[i] = str.replace(words[i]," ","")
		dimensions = []
		dimensions.append(findBetween(words[i],"@",","))
		dimensions.append(findBetween(words[i],",",":"))
		dimensions.append(findBetween(words[i],":","x"))
		dimensions.append(findBetween(words[i],"x","]"))
		squares[findBetween(words[i],"#","@")] = dimensions
		print(words[i])
	return squares
print(*convert().values(),sep='\n')