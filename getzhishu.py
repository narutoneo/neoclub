#!bin/env python
import sys

zhishu_list=[]

testnum1=int(input("please enter the first num:"))
testnum2=int(input("please enter the second num:"))

if testnum1>=testnum2:
	print ("the second number master bigger than the first number")
	sys.exit(1)
if testnum1 < 2:
	numlist=range(2,testnum2)
else:
	numlist=range(testnum1,testnum2)
for i in numlist:
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		zhishu_list.append(i)
print (zhishu_list)
