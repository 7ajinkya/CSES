for _ in range(int(input())):
    row,col=map(int,input().split())
    if row==col:
        print(row**2-(row-1))
    elif col<row:
        diag = row**2-(row-1)
        if row&1:
            print(diag-(row-col))
        else:
            print(diag+(row-col))
    else:
        if col&1:
            print(col**2-(row-1))
        else:
            print((col-1)**2+row)