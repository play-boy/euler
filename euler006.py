#-*- coding:utf-8 -*-
#euler006.py

'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

第一百个，和的平方与平方和的差值
'''

# testlist = range(1, 11)
# psum = sum([i**2 for i in testlist])
# sump = sum(testlist)**2
# print psum, sump, sump - psum

def psump(n, power=2):
	tmplist = range(1, n+1)
	psum = sum([i**power for i in tmplist])
	sump = sum(tmplist)**power
	return sump - psum

print psump(100)
# 
# 25164150
# [Finished in 0.1s]