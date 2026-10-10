'''
1. Prime Number Check
撰寫一個 Python 程式，判斷給定的整數 n 是否為質數；質數必須大於 1，且只能被 1 和自己整除。

Write a Python program that checks whether a given integer n is a prime number.
A prime number is greater than 1 and divisible only by 1 and itself.
'''
n=int(input())
if n<=1:
    print(False) #1 is not a prime number yet can't be calculated with the code I wrote. So we put it along with 0 and the negative numbers.
elif n==2: 
    #2 is a prime number but can't be found with the code. 
    #See, it can't be in range (2,2) because it will create a paradox that's 2 to 1, since "range(a,b)" means "a<=(the numbers it will run)<b". It will run until b-1.
    print(True)
else:
    for i in range (2,n): #Let the input number get divided by every number from 2 to n-1. (Remember, not n.)
        if n%i==0: #This means when n can be divided by i cleanly, without 餘數.
            print(False)
            break
    else:
        print(True)
