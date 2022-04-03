n=int(input())
if n==1:
    print(1)
elif n==2 or n==3:
    print("NO SOLUTION")
else:
    if n&1:
        print(*range(n,0,-2),end=' ')
        print(*range(n-1,0,-2))
    else:
        print(*range(n-1,0,-2),end=' ')
        print(*range(n,0,-2))