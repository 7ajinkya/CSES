# point is to consider only 2s and 5s in the prime factorisation of given factorial.
# 5! = 120 = 2*2*2*3*5. Hence, only 1 zero since only one 2 and one 5
# common observation is that number of 5s <= number of 2s. Hence we only calculate number of 5s
# a quick way to find number of 5s in prime factorisation of a factorial is to keep dividing it by powers of 5
n = int(input())
i = 5
count = 0
while n//i >= 1:
    count += n//i
    i *= 5
print(count)
