n=input()
n=int(n)
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

password="python123"
for i in range(3):
    pwdinput=input()
    if pwdinput==password:
        print("Login successful")
        break
    elif len(pwdinput)<6:
        print("Password too short")
    else:
        print("Incorrect password")
else:
    print("Account locked")
