counter = 0

r1 = range(0, 100)
r2 = range(0, 100)


for A in range(0, 100):
    counter = 0
    for x in r1:
        for y in r2:
            if (y + 2 * x < A) or (x > 30) or (y > 20) == True:
                counter += 1
    if counter == 10000:
        print(A)

# for a in range(0, 300): 
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (y + 2 * x < a) or (x > 30) or (y > 20):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break