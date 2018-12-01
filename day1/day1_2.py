file =open ("day1.txt","r")
nums = file.read().split("\n")
answer = 0
answers = []

def repeat():
	for i in range(0,len(nums)):
		global answer
		global answers
		if nums[i][0] is '+':
			answer +=(int(nums[i][1:]))
			if answer in answers:
				print(answer)
				break
			else:
				answers.append(answer)	
		else:
			answer -=(int(nums[i][1:]))
			if answer in answers:
				print(answer)
				break
			else:
				answers.append(answer)	
	repeat()
repeat()
