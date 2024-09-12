for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                # (z ∧ y) ∨ ((x → z ) ≡ (y → w))
                f = ((z and y) or ((x <= z) == (y <= w)))
                if f == False:
                    print(w,z,y,x, int(f))

# 1 0 0 0
# 1 0 1 0
# 1 0 0 0