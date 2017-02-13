numbers=[]
print("输入数字的数量：")
length=int(input("length:"))

for i in range(length):
	num=int(input("输入一个数："))
	numbers.append(num)
	
list.sort(numbers)
print("输入的数组为",numbers)

numtoadd=int(input("要插入的数字:"))
numbers.append(numtoadd)
list.sort(numbers)
print(numbers)
				
