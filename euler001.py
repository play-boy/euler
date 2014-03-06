#-*- coding:utf-8 -*-
# euler001.py

# testone = [i for i in range(10) if i % 3 == 0 or i % 5 == 0]
# sumone = sum(testone)
# print sumone

# sumtwo = reduce(lambda x,y : x+y, [i for i in range(10) if i % 3 == 0 or i % 5 == 0])
# print sumtwo
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

某个数以内的所有3，5的倍数的和
'''
def multiples(n, one=3, two=5):
	return reduce(lambda x,y : x+y, [i for i in range(n) if i % one == 0 or i % two == 0])

print multiples(1000)

# 233168
# [Finished in 0.1s]