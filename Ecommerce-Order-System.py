import random
class Order:
    def __init__(self, order_id, customer_name, product_price, quantity):
        self.order_id=order_id
        self.customer_name=customer_name
        self.product_price=product_price
        self.quantity=quantity

order_id=random.randint(10000,99999)
customer_name=input("Enter the customer name: ")
product_price=float(input("Enter the product price: "))
quantity=int(input("Enter the product quantity: "))
order1=Order(order_id, customer_name, product_price, quantity)


print(f"Order ID:{order1.order_id}")
print(f"Customer name:{order1.customer_name}")
print(f"Product price:{order1.product_price}")
print(f"Product quantity:{order1.quantity}")
print(f"Total price:{order1.product_price * order1.quantity}")