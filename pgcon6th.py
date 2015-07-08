# coding : utf-8
import sys
import time
stick = []

L = int(sys.stdin.readline())
number = int(sys.stdin.readline())
for i in sys.stdin:
	stick.append(int(i))

answer_num = 0

for a in xrange(0,number):
	for b in xrange(a+1,number):
		if stick[a] + stick[b] >= L:
			break
		for c in xrange(b+1,number):
			if stick[a] + stick[b] + stick[c] == L:
				answer_num +=1

print ('answer is '+ str(answer_num))
