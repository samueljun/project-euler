# Even Fibonacci numbers

num_1 = 1
num_2 = 2
num_sum = num_1 + num_2

even_sum = 0

while num_2 < 4000000:
    if num_2 % 2 == 0:
        even_sum = even_sum + num_2
    num_1 = num_2
    num_2 = num_sum
    num_sum = num_1 + num_2

print even_sum
