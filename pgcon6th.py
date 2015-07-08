# coding: utf-8
import sys
stick = []

L = int(sys.stdin.readline()) #1行目L
number = int(sys.stdin.readline()) #2行目棒の数
for i in sys.stdin:
	stick.append(int(i)) #3行目～　各棒をリストに追加

answer_num = 0

for a in xrange(0,number):
	for b in xrange(a+1,number):
		if stick[a] + stick[b] >= L:
			break
		for c in xrange(b+1,number):
			if stick[a] + stick[b] + stick[c] == L:
				answer_num += 1

print('answer is %i' % answer_num)
