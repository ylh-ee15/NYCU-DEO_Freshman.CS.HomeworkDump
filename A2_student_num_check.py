'''
Setup a list which contains the numbers of your student number.
a) Count how many “1” are contained in your student number.
b) Find out the index of the first “1” in your list.
c) Apply the methods of list to adjust your list to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

st_num=[1,1,5,5,1,4,0,0,4]
n=0
i=0
j=0
'''
for i in st_num:
    if i==1:
        n+=1
print (n)
'''
print(st_num.count(1))
print(st_num.index(1))
st_num.sort()
print(st_num)
'''
st_num=sorted(st_num)
print(st_num)
'''
