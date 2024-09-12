from itertools import * 

counter = 0
words = product("АОУ", repeat=5)

counter = 1
for i in words:
    print(counter, i)
    counter += 1
# for word in words:
#     if ''.join(word).count('ЕИ') == 0 and ''.join(word)[0] != 'Й':
#         counter += 1
