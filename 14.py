num = 343 ** 5 + 343**4 + 49**6 - 7**13 - 21
counter = 0

# while num != 0:
#     if num % 7 == 6:
#         counter += 1
#     num //= 7

nums = set()
while num != 0:
    nums.add(num % 7)
    num //= 7

print(len(nums))
print(counter)