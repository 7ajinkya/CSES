from collections import defaultdict as dd
s = input()
d = dd(int)
for i in s:
    d[i] += 1
even = len(s) & 1 == 0
cnt_odd = 0
for i in d:
    if d[i] & 1:
        cnt_odd += 1
        odd_char = i
if cnt_odd > 1 or cnt_odd == 1 and even:
    print("NO SOLUTION")
else:
    f_half = ""
    s_half = ""
    for x in sorted(d.keys()):
        st = (d[x]//2)*x
        f_half = f_half + st
        s_half = st+s_half
    if cnt_odd == 1:
        print(f_half+odd_char+s_half)
    else:
        print(f_half+s_half)
