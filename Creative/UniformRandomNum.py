import random

list=[]
for i in range(5):
    a=random.random()
    list.append(a)
print(list)
print("maximum is ",max(list))
print("Minimum is",min(list))
for i in list:
    a+=i
print(f"Average:",a)
