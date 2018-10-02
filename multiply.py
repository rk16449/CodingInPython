def multAll2(A, k):
    b = []
    b[:] = A
    for i in range(0, len(A)):
        b[i] = b[i] * k
    return b

A = [5,12,31,7,25]
print(multAll2(A, 10))  # should print [50,120,310,70,250]
print(A) # should print [5, 12, 31, 7, 25]
