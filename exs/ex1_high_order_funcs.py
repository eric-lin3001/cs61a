""" Calculate sequences such as 1+2+3+4+5 OR 1^3+2^3+3^3+4^3+5^3"""

def sum_naturals(n):
    """Sum the first N natural numbers
    >>> sum_naturals(5)
    15
    """
    total,k = 0,1
    while k<=n:
        total,k = total+k,k+1
    return total
    
def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    total,k = 0,1
    while k<=n:
        total,k = total+pow(k,3),k+1
    return total

def sum_pi(n):
    total,k = 0,1
    while k<=n:
        total,k = total+8 / ((4*k-3) * (4*k-1)),k+1
    return total

"""Generation: 三个函数的共同点明确，考虑函数代码相同的部分取出,不同的部分(关于k的函数),用参数替代,这里参数是函数。"""

def identity(x):
    return x

def cube(x):
    return pow(x,3)

def pi(x):
    return 8 / ((4*x-3) * (4*x-1))

def summation(n,term):
    """Sum the first N items of a sequence
    >>> summation(50,pi)
    15
    """
    total,k = 0,1
    while k<=n:
        total,k = total+term(k),k+1
    return total