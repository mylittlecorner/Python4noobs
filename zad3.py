#!/usr/bin/env python3

import sys

n=int(sys.argv[1])
w=0

while(n!=0):
	w=w + (n % 10)
	n=int(n/10)

print(w)
