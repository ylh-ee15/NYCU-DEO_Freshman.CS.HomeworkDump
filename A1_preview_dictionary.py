goods=str(input())
product={"Latte": 1, "Americano":2, "Cappuccino":3}
if goods in product:
    print(product[goods])
else:
    print("Error")
