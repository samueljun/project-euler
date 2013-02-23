# Largest Palindrome Product

# Heuristic:
# 100000a + 10000b + 1000c + 100c + 10b + a
# 100001a + 10010b + 110c
# 11(9091a + 910b + 10c)
# Palindrome must be divisible by 11

max = 0

for x in range(999, 900, -1):
    for y in range(999, 900, -1):
        num = x * y

        num_str = str(num)
        num_str_reverse = num_str[::-1]
        num_reverse = int(num_str_reverse)

        if num == num_reverse and num > max:
            max = num

print max

