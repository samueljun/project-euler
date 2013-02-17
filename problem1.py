# Multiples of 3 and 5

total_sum = 0
for num in range(3, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total_sum = total_sum + num
print total_sum
