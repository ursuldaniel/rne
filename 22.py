def F(x, y):
    if x < y or x == 12 or x == 15:
        return 0
    
    if x == y:
        return 1
    
    if x % 3 == 0 and x % 2 == 0:
        return F(x - 1, y) + F(x // 2, y) + F(x // 3, y)

    if x % 3 != 0 and x % 2 != 0:
        return F(x - 1, y)

    if x % 3 != 0 and x % 2 == 0:
        return F(x - 1, y) + F(x // 2, y)

    if x % 3 == 0 and x % 2 != 0:
        return F(x - 1, y) + F(x // 3, y)

# def f (start, end, s):
#     if start == end and '+++' not in s and '***' not in s:
#         return 1
#     elif start > end:
#         return 0
#     return f(start + 1, end, s + '+')+ f(start*2, end, s + '*')
# print(f(1, 16, ''))
