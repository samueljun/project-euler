# Smallest multiple

# Heuristic:
# The number must be a multiple of the product of the primes
# 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

for x in range(9699690, 1000000000, 9699690):
    if x % 11 == 0 \
        and x % 12 == 0 \
        and x % 13 == 0 \
        and x % 14 == 0 \
        and x % 15 == 0 \
        and x % 16 == 0 \
        and x % 17 == 0 \
        and x % 18 == 0 \
        and x % 19 == 0 \
        and x % 20 == 0:
            print x
            break

