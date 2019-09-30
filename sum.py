#!/usr/bin/env python

testnum=int(input("please enter the number for test:"))
if (testnum%2) == 0:
	sum=testnum/2*testnum+testnum/2
else:
	sum=(testnum+1)/2*testnum
print (int(sum))
	
sum=0
for i in range(testnum+1):
	sum=sum+i
print (int(sum))
