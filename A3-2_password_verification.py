'''
2. Password Verification System
撰寫一個簡單的密碼驗證程式。
正確密碼為 python123，使用者最多有 3 次輸入機會。

密碼正確：輸出 Login successful，並立即停止程式。
密碼錯誤且長度小於 6：輸出 Password too short。
其他錯誤密碼：輸出 Incorrect password。
若 3 次皆失敗：輸出 Account locked。
'''

password="python123"
for i in range(3): #will run the code 3 times, as in 3 input chances
    pwdinput=input()
    if pwdinput==password:
        print("Login successful")
        break
    elif len(pwdinput)<6: #len() is for calculating the length of the function
        print("Password too short")
    else:
        print("Incorrect password")
else: #Format is important kids, remember to line this one up with the "for i in range(3):".
    print("Account locked")
