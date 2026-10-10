'''
1. Prime Number Check
撰寫一個 Python 程式，判斷給定的整數 n 是否為質數；質數必須大於 1，且只能被 1 和自己整除。

Write a Python program that checks whether a given integer n is a prime number.
A prime number is greater than 1 and divisible only by 1 and itself.
'''
n=int(input())
if n<=1:
    print(False)
elif n==2:
    print(True)
else:
    for i in range (2,n):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
