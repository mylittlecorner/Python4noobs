#!/usr/bin/env python3

import sys

arg1=int(sys.argv[1])
arg2=int(sys.argv[2])

def sym(a,b):
	if(a!=0):
		sym(a-1, b+1)
		print(a * b)
		sym(a-1, b+1)

sym(arg1,arg2)
