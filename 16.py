def F(n):
    if n == 1:
        return 0
    
    if n > 1:
        return F(n - 1) + n
    
def G(n):
    if n == 1:
        return 1
    
    if n > 1:
        return G(n - 1) * n

    
print(F(5))
print(G(5))