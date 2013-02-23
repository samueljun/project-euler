#Largest prime factor

num = 600851475143
curr_num = 2
prime_nums = []

while curr_num < num:
    if num % curr_num == 0:
        num = num / curr_num
        prime_nums.append(curr_num)
    curr_num += 1

prime_nums.append(num)
print prime_nums
print num

