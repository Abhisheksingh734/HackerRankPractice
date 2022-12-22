class Item:
    def calc_total_price(self,x,y):
        return x*y

item1=Item()
item1.name="Phone"
item1.price=200
item1.quantity=5

print(item1.calc_total_price(item1.price,item1.quantity))

item2=Item()
item2.name="Laptop"
item2.price=9000
item2.quantity=3
print(item2.calc_total_price(item2.price,item2.quantity))
