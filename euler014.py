#-*- coding:utf-8 -*-
#euler014.py

'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

3x+1问题求解
'''
# 思路：从上往下遍历，若已经包含在内，那么就不需要再次运算

def refreshdict(resdic, resli):
	if resli == []:
		return
	tmp = resli.pop()
	pos = 0
	if tmp in resdic:
		pos = resdic[tmp]
	for i in range(len(resli)):
		pos += 1
		resdic[resli[len(resli) - i - 1]] = pos

targetnum = 999999

# i = targetnum
resdic = {}
for i in range(targetnum):
	tmp = targetnum - i
	# tmp = i + 1
	resli = []
	while tmp != 1:
		if not tmp in resdic:
			resli.append(tmp)
			if tmp % 2 == 0:
				tmp /= 2
			else:
				tmp = 3*tmp + 1
		else:
			resli.append(tmp)
			break

	refreshdict(resdic, resli)

# res = resdic.values()
# print max(res)
mmax = 1
for key,value in resdic.items():
	if value > mmax:
		mmax = value
		mkey = key
print mmax, mkey

print resdic[837799]
# print resdic[1]
# 534 2513398
# [Finished in 5.5s]
# 结果需要处理下，837799
# 统计结果有出入，不知道是哪里算错了


