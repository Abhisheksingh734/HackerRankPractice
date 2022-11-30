n=int(input("fibo series upto which term: "))
fibo=[0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(n)]
print(*fibo)


    # Ternary operator (one liner)

# num=int(input())
# num=20 if num>5 else 10
# print(num)
