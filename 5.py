# def count(n):
#     res = 0
#     for i in n:
#         res += int(i)

#     return (res % 2)

for binary in range(1000, 10000):
    # binary = bin(N)[2:]

    sums = []
    sums.append(int(str(binary)[0]) + int(str(binary)[1]))
    sums.append(int(str(binary)[1]) + int(str(binary)[2]))
    sums.append(int(str(binary)[2]) + int(str(binary)[3]))
    sums.remove(min(sums))

    result = (str(min(sums)) + str(max(sums)))
    if result == '613':
        print(binary)