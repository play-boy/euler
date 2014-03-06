#-*- coding:utf-8 -*-
#euler005.py

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

求最小的某个数的因子包含连续自然数1-20
'''

# 思路：对所有素因子进行比较，留下指数大的，最后把所有素因子相乘，得到结果


def get_prime_dict(n):
	dictprime = {}
	current = 2
	while current**2 <= n:
		num = 0
		while n % current == 0:
			n /= current
			num += 1
		if num and (not current in dictprime or dictprime[current] < num):
			# print current, num
			dictprime[current] = num
		current += 1
	else:
		if n != 1:
			dictprime[n] = 1
	return dictprime

def fresh_dict(first, second):
	for key in second.keys():
		if not key in first or first[key] < second[key]:
			first[key] = second[key]

dictprime = {2:0}
testnum = 20

for i in range(2, testnum + 1):
	if i in dictprime and dictprime[i] == 0:
		dictprime[i] = 1
		continue
	fresh_dict(dictprime, get_prime_dict(i))

res = reduce(lambda x,y : x*y, [key**dictprime[key] for key in dictprime.keys()])
print res
print dictprime

# 232792560
# {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}
# [Finished in 0.1s]