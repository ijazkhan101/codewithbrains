
# n (n-1 ) (n-2) (n-2).....(2)(1)
# 5(4)  (3)(2)(1)


def factorial(n):
    if n ==1 or n==0:
        return 1
    
    results = n* factorial(n-1)
    return results
    
def determinant(n):
    pass 


if __name__ == '__main__':
    print(factorial(5))