# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         factorial =factorial(n-1)
#         return factorial * (n-1)
    
def factorial1(n):
    assert n>=0 and int(n) == n, 'number must be positive int only'
    print(n)
    if n == 0:
        return 1
    return n + factorial1(n-1)


print(factorial1(-1))

