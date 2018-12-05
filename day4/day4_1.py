import re
file =open ("day4.txt","r")
words = file.read().split("\n")
results = []

for word in words:
	timeRe = re.compile('\[(\d{4})')
	parsed = timeRe.match(word).groups()
	print(parsed)