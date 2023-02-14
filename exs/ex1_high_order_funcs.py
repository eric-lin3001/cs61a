""" 对一个关于k的序列,如k^3,求这个序列从k=1开始,到k=n为止的求和结果。 
例如序列为k,n=5时,求1+2+3+4+5的结果;或是序列为k^3,n=5时,1^3+2^3+3^3+4^3+5^3的结果。
下面是对每个序列写函数的做法
"""
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

"""因为对于不同的序列，求和方式非常接近，不应该对每个序列写一个求和函数，而应该定义一个抽象的求和函数，将序列作为参数传入。
下面是写出抽象函数summation的做法，函数term将被作为参数传入，这就是functions as argument。
调用时，可以直接调用summation(n,term)，也可以写个专门的调用函数，对不同的序列进行求和。
"""

def identity(x):
    return x

def cube(x):
    return pow(x,3)

def pi(x):
    return 8 / ((4*x-3) * (4*x-1))

"""抽象函数summation"""
def summation(n,term):
    """Sum the first N items of a sequence
    >>> summation(50,pi)
    15
    """
    total,k = 0,1
    while k<=n:
        total,k = total+term(k),k+1
    return total

"""专门的调用函数，计算序列为8 / ((4*k-3) * (4*k-1))的和"""
def sum_pi(n):
    summation(n,identity)