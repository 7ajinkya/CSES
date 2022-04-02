n=int(input())
arr=[*map(int,input().split())]
count=0
for i in range(n-1):
    if arr[i]>arr[i+1]:
        count+=(arr[i]-arr[i+1])
        arr[i+1]=arr[i]
print(count)