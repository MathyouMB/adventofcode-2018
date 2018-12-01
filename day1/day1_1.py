file =open ("day1.txt","r")
nums = file.read().split("\n")
answer = 0
for i in range(0,len(nums)):
	if nums[i][0] is '+':
		answer +=(int(nums[i][1:]))
	else:
		answer -=(int(nums[i][1:]))
print(answer)
	