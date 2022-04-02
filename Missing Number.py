n=int(input())
arr=[*map(int,input().split())]
add=0
for i in arr:
    add+=i 
print((n*(n+1)//2) - add)