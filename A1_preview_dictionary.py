'''
輸入商品名稱後，程式需輸出對應的商品編號；若輸入的商品不在指定清單中，則輸出「錯誤」。
'''
#log: There was no lesson when we were given this homework. The TAs kind of expected us to use AI. Well, I have experience and a resolve not to vibe code, so here's my code.
goods=str(input())
product={"Latte": 1, "Americano":2, "Cappuccino":3} #used dictionary
if goods in product: #Great thing about python: it's very easy to understand. This means checking if what we input (goods) is in the dictionary (product).
    print(product[goods])
else:
    print("Error")
