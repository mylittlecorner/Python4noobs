#!/usr/bin/env python3

def textCount(mylist):
	text=mylist[1]
	count=0
	max_val=1
	max_val_letter=text[0]
	
	for letter in text:
		for compare in text:
			if(letter==compare):
				count=count+1
				if(count>max_val):
					max_val=count
					max_val_letter=letter
			else:
				count=0
	lineappend(max_val_letter*max_val, max_val)

def lineappend(A,B):
	f=open('odp.txt','a')
	f.write(f'{A} {B}\n')
	f.close()

f=open('pary.txt', 'r')
for line in f:
	mylist = line.split(" ")
	textCount(mylist)
f.close()

