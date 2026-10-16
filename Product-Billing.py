class product:
    def __init__(self, productname, price, quantity):
        self.productname = productname
        self.price = price
        self.quantity = quantity

productname=input("Enter the product name: ")
price=float(input("Enter the product price: "))
quantity=int(input("Enter the product quantity: "))
product1=product(productname,price,quantity)
print(f"Product name:{product1.productname}")
print(f"Product price:{product1.price}")
print(f"Product quantity:{product1.quantity}")
print(f"Total price:{product1.price * product1.quantity}")