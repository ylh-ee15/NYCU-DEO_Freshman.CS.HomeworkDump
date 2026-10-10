"""
請完成課堂作業，撰寫程式計算兩個向量的 Inner Product、Outer Product 與 Cosine Similarity。
程式需包含 inner()、outer()、cosine_similarity()、display() 四個函式，且不可使用 math、numpy 等模組。
"""
#In case you don't know what the required math work, search the internet. You're absolutely allowed to do so.
def inner(a,b): # define the 函式 inner product (I used 內積, which we learned in high school. I have no idea if they are the exact same thing, but the outcomes are indeed the same.)
    ans=0
    i=0
    while i < 3: #It's a space vector so there's x, y and z, which is 3 in a row.
        ans+=a[i]*b[i] #Just do the high school multiplication thing.
        i+=1
    return ans

def outer(a,b): # define the 函式 outer product (I had to look up the formula for this, because this is the vector output version of high school 外積. https://www.geeksforgeeks.org/python/outer-product-on-vector/)
  ans=[[0,0,0],[0,0,0],[0,0,0]] #make a 3*3 矩陣
  i=0
  j=0
    #Nested loop incoming! Nested loops means after the inner loop finished, the outer loop will run the inner loop again.
  while i <3:
    while j<3:
      ans[i][j]=int(a[i]*b[j]) #So this means we get a 3*3 矩陣. [i][j] is mathematically 第i行第j列.
      j+=1
    i+=1
    j=0
  return ans

def cosine_similarity(a,b): #Out of high school range. https://www.geeksforgeeks.org/dbms/cosine-similarity/
  ans=0
  mag_a=pow((pow(a[0],2)+pow(a[1],2)+pow(a[2],2)),1/2)
  mag_b=pow((pow(b[0],2)+pow(b[1],2)+pow(b[2],2)),1/2)
  ans=round((inner(a,b)/(mag_a*mag_b)),4)
  return ans

def display(a,b):
  print(f"The inner product of {a} and {b} is {inner(a,b)}.")
  print(f"The outer product of {a} and {b} is {outer(a,b)}.")
  print(f"The cosine similarity of {a} and {b} is {cosine_similarity(a,b)}.")

n=[1,2,3]
m=[4,5,6]

display(n,m)
  
