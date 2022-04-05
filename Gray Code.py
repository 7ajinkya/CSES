def ans(n):
    if n == 1:
        return ['0', '1']
    newans = ans(n-1)
    finalans = []
    for i in newans:
        finalans += ['0'+i]
    for i in newans[::-1]:
        finalans += ['1'+i]
    return finalans


n = int(input())
print(*ans(n), sep='\n')
