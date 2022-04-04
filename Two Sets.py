n = int(input())
if n*(n+1)//2 & 1:
    print("NO")
else:
    print("YES")
    if n & 1:
        m1 = n
        print(n//2)
        for i in range(n//2):
            print(m1, end=' ')
            if m1 & 1:
                m1 -= 3
            else:
                m1 -= 1
        m2 = n-1
        print()
        print(n//2+1)
        for i in range(n//2+1):
            print(m2, end=' ')
            if m2 & 1:
                m2 -= 3
            else:
                m2 -= 1
    else:
        m1 = n
        print(n//2)
        for i in range(n//2):
            print(m1, end=' ')
            if m1 & 1:
                m1 -= 1
            else:
                m1 -= 3
        m2 = n-1
        print()
        print(n//2)
        for i in range(n//2):
            print(m2, end=' ')
            if m2 & 1:
                m2 -= 1
            else:
                m2 -= 3
