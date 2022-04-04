for _ in range(int(input())):
    a, b = map(int, input().split())
    if (a+b) % 3 == 0 and 2*a >= b and 2*b >= a:
        # from observation it's clear that a+b has to be multiple of 3 since we are taking 1 coin from one pile and 2 from other.
        # also, we don't want one pile to end up before the other, hence we check for both the cases and 2*a >= b and 2*b >= a.
        # basically 2*a>=b and 2*b>=a ensures us that we never run out of coins and that there is always 1 coin for 2 coins (or 2 coins for 1 coin)
        print("YES")
    else:
        print("NO")
