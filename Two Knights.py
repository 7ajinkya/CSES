for i in range(1, int(input())+1):
    total_ways_of_placing_two_knights = i*i*(i*i-1)//2
    total_ways_of_placing_two_knights_such_that_they_attack_each_other = 4 * \
        (i-1)*(i-2)
    print(total_ways_of_placing_two_knights -
          total_ways_of_placing_two_knights_such_that_they_attack_each_other)
