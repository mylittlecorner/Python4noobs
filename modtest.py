#!/usr/bin/env python3

import sys
a=int(sys.argv[1])
b=int(sys.argv[2])

def mod(a,b):
	return a % b

def ile(a,b):
	cnt=0
	while((cnt*b)+mod(a,b)<a):
		cnt=cnt+1
	return [cnt,cnt*b]

print(f'{a} podzielilismy przez {b} zostalo {mod(a,b)}')
print(f'w {a} miesci sie {ile(a,b)[0]} zsumowanych liczb {b} czyli {ile(a,b)[1]}')
