nums = [int(x) for x in open("17.txt")]

counter = 0
max_sum = 0
for i in range(len(nums) - 1):
    if ((nums[i] + nums[i + 1]) % 5 == 0) and ((nums[i] % 3 == 0) or (nums[i + 1] % 3 == 0)):
        counter += 1
        if (nums[i] + nums[i + 1]) > max_sum:
            max_sum = nums[i] + nums[i + 1]
print(counter, max_sum)








# sums = []
# max_num = -10001

# for i in nums:
#     if abs(i) % 10 == 3:
#         max_num = max(max_num, i)

# for i in range(len(nums) - 2):
#     x = (nums[i], nums[i + 1])
#     sum1 = x[0]**2 + x[1]**2

#     c = 0
#     if abs(x[0]) % 10 == 3:
#         c += 1
#     if abs(x[1]) % 10 == 3:
#         c += 1

#     if c == 1 and (sum1 >= max_num**2):
#         sums.append(sum1)

# print(len(sums), max(sums))