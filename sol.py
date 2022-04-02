s=input()
c=maxi=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        maxi=max(maxi,c)
    else:
        c=1
print(maxi)