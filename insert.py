numbers=[]
print("输入数字的数量：")
length=int(input("length:"))

for i in range(length):
	num=int(input("输入一个数："))
	numbers.append(num)
	
numbers.sort()

numtoadd=int(input("要插入的数字:"))
if numtoadd>=numbers[length-1]:
	numbers.append(numtoadd)
else:
	for i in range(length-1):
		if numtoadd<numbers[i]:
			temp1=numbers[i]
			numbers[i]=numtoadd
			for j in range(i+1,length-1):
				temp2=numbers[j]
				numbers[j]=temp1
				temp1=temp2
			break
print(numbers[0:length])
				
