file =open ("day3.txt","r")
words = file.read().split("\n")
results = []

grid = [None] * 1000

#wow Im bad


for i in range(0,1000):
	grid[i] = [None] * 1000

def findBetween(s, f, l):
	startindex = s.find(f)
	endindex = startindex + len(f)
	lastindex = s.find(l)
	start = s.index(f) + len(f)
	end = s.index(l, start)
	return s[start:end]

#[xpos,ypos,xlen,ylen]
def convert():
	squares = {}
	for i in range(0,len(words)):
		words[i] += ']'
		words[i] = str.replace(words[i]," ","")
		dimensions = []
		dimensions.append(int(findBetween(words[i],"@",",")))
		dimensions.append(int(findBetween(words[i],",",":")))
		dimensions.append(int(findBetween(words[i],":","x")))
		dimensions.append(int(findBetween(words[i],"x","]")))
		squares[int(findBetween(words[i],"#","@"))] = dimensions
		#print(words[i])
	return squares
squares = convert()
#print(*convert().keys(),sep=',')
def apply(hash):
	for i in range(1,len(hash)):
		#print(hash[i][0])
		#print(hash[i][1])
		#print(hash[i][2])
		#print(hash[i][3])
		for x in range(hash[i][0],hash[i][2]):
			for y in range(hash[i][1],hash[i][3]):
				if grid[x][y] == None:
					#print(i)
					grid[x][y] = i
				else:
					grid[x][y] = "X"

apply(squares)
#print(*grid,sep='\n')
