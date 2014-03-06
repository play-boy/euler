#-*- coding:utf-8 -*-
# euler067.py

'''
	By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
	the maximum total from top to bottom is 23.

	3
	7 4
	2 4 6
	8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom in triangle.txt 
	(right click and 'Save Link/Target As...'), 
	a 15K text file containing a triangle with one-hundred rows.

	NOTE: This is a much more difficult version of Problem 18. 
	It is not possible to try every route to solve this problem, as there are 299 altogether! 
	If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
	There is an efficient algorithm to solve it. ;o)
	下载数据，并提取数据，然后找到一种有效的解决方法来处理！
	Good luck to you!
'''
from urllib import urlopen
datastr   = urlopen('http://projecteuler.net/project/triangle.txt').read()
# datastr = '''75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# '''
triangle = []
datastr = datastr.replace(' 0', ' ')
datastr = datastr.replace('\n0', '\n')
# tmplist = datastr.split('\n')
triangle = [[int(i) for i in x.split(' ')] for x in datastr.split('\n')[:-1]]
# for ts in tmplist:
# 	if ts != '':
# 		tmp = []
# 		for s in ts.split(' '):
# 			if s != '':
# 				tmp.append(int(s))
# 		triangle.append(tmp)
# print triangle
# triangle = [[3],
# [7, 4],
# [2, 4, 6],
# [8, 5, 9, 3]]
# 

def dealtri(nectcc, button):
	for i in range(len(nectcc)):
		if button[i] > button[1+i]:
			nectcc[i] += button[i]
		else:
			nectcc[i] += button[i+1]

nectcc = triangle[-1]
for i in range(len(triangle) - 1):
	current = nectcc
	nectcc = triangle[-(i+2)]
	dealtri(nectcc, current)

print nectcc


# 另一种代码方式
# from urllib import urlopen
# import re
# rawTri   = urlopen('http://projecteuler.net/project/triangle.txt').read()
# link     = re.compile(' 0')
# rawTri   = re.sub(link, ' ', rawTri)
# link     = re.compile('\n0')
# rawTri   = re.sub(link, '\n', rawTri)
# triangle = [[int(i) for i in x.split(' ')] for x in rawTri.split('\n')[:-1]]

# if __name__ == '__main__':
#     for row in xrange(len(triangle) - 1):
#         for column in xrange(len(triangle[row + 1])):
#             if column == 0:
#                 triangle[row + 1][column] += triangle[row][column]
#             elif column == len(triangle[row + 1]) - 1:
#                 triangle[row + 1][column] += triangle[row][column - 1]
#             else:
#                 triangle[row + 1][column] += max(triangle[row][column], triangle[row][column - 1])

#     print max(triangle[len(triangle) - 1])


# 结果：
# [7273]
# [Finished in 1.3s]