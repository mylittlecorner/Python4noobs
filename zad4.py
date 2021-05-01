#!/usr/bin/env python3

def ifEvenCalc(mylist):
	item=int(mylist[0])
	if((item % 2 == 0) and (item >4)):
		iterateBothUnevenLists(getUnevenList(item),getUnevenList(item),item)

def iterateBothUnevenLists(unevenListA,unevenListB,item):
	for A in unevenListA:
		for B in unevenListB:
			if((A+B) == item):
				lineappend(item, A, B)


def getUnevenList(item):
	unevenList=list()
	for x in range(item):
		if(x % 2 !=0):
			unevenList.append(x)
	return unevenList

def lineappend(result,A,B):
	f=open('odp.txt','a')
	f.write(f'{result} {A} {B}\n')
	f.close()

f=open('pary.txt', 'r')
for line in f:
	mylist = line.split(" ")
	ifEvenCalc(mylist)
f.close()

