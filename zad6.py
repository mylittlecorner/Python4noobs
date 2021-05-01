#!/usr/bin/env python3

def Para(bigList):
	trigger=True
	while(trigger):
		for i in range(1,len(bigList)):
			liczba1=int(bigList[i-1][0])
			liczba2=int(bigList[i][0])
			slowo1=bigList[i-1][1]
			slowo2=bigList[i][1]
			trigger=False

			if((liczba1<liczba2) or ((liczba1 == liczba2) and (slowo1 < slowo2))):
				tmp=bigList[i-1]
				bigList[i-1]=bigList[i]
				bigList[i]=tmp
				trigger=True
	return bigList


def lineappend(list):
	f=open('odp.txt','a')
	f.write(f'{list[0]} {list[1]}')
	f.close()

bigList=list()
f=open('pary.txt', 'r')
for line in f:
	mylist = line.split(" ")
	mylist[1].replace('\n','')
	bigList.append(mylist)
	#textCount(mylist)
f.close()

for item in bigList:
	print(f'{item[0]} {item[1]}',end="")

print('\n')

bigList=Para(bigList)
for item in bigList:
	print(f'{item[0]} {item[1]}',end="")
	if(int(item[0]) == len(item[1])):
		print(f'!!!!!!{item}!!!!')
