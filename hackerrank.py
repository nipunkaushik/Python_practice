# if __name__ == '__main__':
#     a = int(raw_input('Please enter a number'))
#     b = int(raw_input('Please enter a number'))
#     try:
#         a > 1 and a < 10**10
#         b > 1 and b < 10**10
#     except:
#         'Number out of range'
#         exit()
#     add = a + b
#     diff = a - b
#     mul = a * b
#     add = str(add)
#     diff = str(diff)
#     mul = str(mul)
# print add
# print diff
# print mul

# from __future__ import division
# if __name__ == '__main__':
#     div1 = 0
#     a = int(raw_input())
#     b = int(raw_input())
#     div1 = a // b
#     div2 = 0.0
#     div2 = a / b
#     print div1
#     print div2

# a = int(raw_input())
# n = 0
# b = 0
# if a in range(0, 21):
#     while n < a:
#         b = n * n
#         print b
#         n = n + 1


# def is_leap(year):
#     leap = False
#     if year % 4 == 0 and year % 100 != 0:
#         leap = True
#     if year % 400 == 0:
#         leap = True
#     return leap


# year = int(raw_input())
# try:
#     year >= 1900
#     year <= 10**5
# except:
#     print 'Value out of range'
#     quit()
# print is_leap(year)

# from __future__ import print_function
# print(*range(1, int(raw_input()) + 1), sep='')

# thickness = int(raw_input('Please enter an odd number: \n'))
# thickness = 5
# c = 'H'


# if thickness % 2 == 1:
#     for i in range(thickness):
#         print (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)

#     # Top Pillars
#     for i in range(thickness + 1):
#         print (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

#     # Middle Belt
#     for i in range((thickness + 1) / 2):
#         print (c * thickness * 5).center(thickness * 6)

#     # Bottom Pillars
#     for i in range(thickness + 1):
#         print (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

#     # Bottom Cone
#     for i in range(thickness):
#         print ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
# else:
#     print 'Not odd'

# import sys
# print (sys.executable)

# import time

# for i in range(5):
#     print "Hello World"
#     time.sleep(1)

# import textwrap


# def wrap(string, max_width):

#     if len(string) in range(0, 100) and max_width in range(0, len(string)):
#         return textwrap.fill(string, max_width)
#     else:
#         return "Error"


# string, max_width = raw_input(), int(raw_input())
# result = wrap(string, max_width)
# print result

# a = int(raw_input())
# b = int(raw_input())

# try:
#     a > 10
#     b > 5
# except:
#     val = -1
#     if float(val) < 0:
#         raise ValueError('Value out of range')
#     exit()
# print a
# print b
# c = a + b
# print c

# even odd function

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# a = raw_input('Enter a number: ')
# try:
#     a = int(a)
#     result = is_even(a)
#     print result
# except:
#     print ('Please provide an integer')


# Door Mat Problem
# N, M = map(int, raw_input().split())
# for i in range(1, N, 2):
#     print("{}".format(".|." * i).center(M, "-"))
# print("WELCOME".center(M, "-"))
# for i in range(N - 2, -1, -2):
#     print("{}".format(".|." * i).center(M, "-"))

