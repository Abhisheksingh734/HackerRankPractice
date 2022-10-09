N=int(input("enter"))
list=[]
for i in range(N):
    for j in range(N):
        list.insert(i,j)
        print(list)
        list.remove(j)
        list.append(j)
        list.sort()
        list.pop()
        list.reverse()
