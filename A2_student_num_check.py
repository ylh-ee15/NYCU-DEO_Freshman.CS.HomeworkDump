'''
Setup a list which contains the numbers of your student number.
a) Count how many “1” are contained in your student number.
b) Find out the index of the first “1” in your list.
c) Apply the methods of list to adjust your list to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (from small to large).
'''

st_num=[1,1,5,5,1,4,0,0,4] #Put in your own student number divided with commas. This is mine. Yes I just leaked my personal info somewhat.
n=0
i=0
j=0
'''
#The old-fashoned way, without using count().
for i in st_num:
    if i==1:
        n+=1
print (n)
'''
print(st_num.count(1)) #Count(insert number)=count the required number in the list.
print(st_num.index(1)) #Check the index of the first required number in list (remember indexes start with 0, not 1).
st_num.sort() #Sort the list from a lesser number to a larger number.
print(st_num)
'''
#My initial choice: sorted().
st_num=sorted(st_num) #sorted(): Outputs the sorted list ike sort(), but is temporary and doesn't change the original list. Basically, "st_num=sorted(st_num)" is the same as "st_num.sort()".
print(st_num)
'''
