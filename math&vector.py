"""
請完成課堂作業，撰寫程式計算兩個向量的 Inner Product、Outer Product 與 Cosine Similarity。
程式需包含 inner()、outer()、cosine_similarity()、display() 四個函式，且不可使用 math、numpy 等模組。
"""
def inner(a,b):
    ans=0
    i=0
    while i < 3:
        ans+=a[i]*b[i]
        i+=1
    return ans

def outer(a,b):
  ans=[[0,0,0],[0,0,0],[0,0,0]]
  i=0
  j=0
  while i <3:
    while j<3:
      ans[i][j]=int(a[i]*b[j])
      j+=1
    i+=1
    j=0
  return ans

def cosine_similarity(a,b):
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
  
