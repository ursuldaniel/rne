nums = [int(x) for x in open("17.txt")]

sums = []
max_num = max(nums)**2

for i in range(len(nums) - 1):
    x = (nums[i], nums[i + 1])
    current_sum = x[0]**2 + x[1]**2

    # Check if exactly one of the numbers ends with 3
    if (abs(x[0]) % 10 == 3) + (abs(x[1]) % 10 == 3) == 1:
        if current_sum >= max_num:
            sums.append(current_sum)

# Ensure there's no error if sums is empty
if sums:
    print(len(sums), max(sums))
else:
    print(0, 0)
