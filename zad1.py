#!/usr/bin/env python3

import sys

def czy_k_podobne(A,B,k,n):
	if(len(sys.argv)<3):
		for k in range(n):
			if((A[:(k)-1]==B[(n-k+1)-1:(n)-1] and A[(k+1)-1:(n)-1]==B[:(n-k)-1]) or (k==0 and A==B)):
				print(f'PRAWDA (k):{k}')
			else:
				print(f'FALSZ (k):{k}')
	else:
		if((A[:(k)-1]==B[(n-k+1)-1:(n)-1] and A[(k+1)-1:(n)-1]==B[:(n-k)-1]) or (k==0 and A==B)):
				print('PRAWDA')
		else:
			print('FALSZ')



n=int(sys.argv[1])
k=None
if(len(sys.argv)>2):
	k=int(sys.argv[2])

if(n<=0):
	print("liczba calkowita n musi byc wieksza niz zero!")
	sys.exit()

A=list()
B=list()

for i in range(n):
	A.append(int(input(f'Wpisz {i+1} element tabeli A:')))

for i in range(n):
	B.append(int(input(f'Wpisz {i+1} element tabeli B:')))

print(f'A:{A}\nB:{B}')
czy_k_podobne(A,B,k,n)

