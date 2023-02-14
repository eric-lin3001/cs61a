"""给定一个整数n，求n各个位上数字的和"""
"""递归算法，sum_digits(n) = sum_digits(n//10) + last
sum_digits(n//10) = sum_digits(n//10//10) + last
sum_digits(n//10//10) 会在某个条件下收敛。
"""
def sum_digits(n):
    if(n<10):
        return n
    else:
        """求整数n的最后一位，和扣掉最后一位的新整数n"""
        last,all_but_last = n % 10, n//10
        return sum_digits(all_but_last) + last

"""
n=987
1. sum_digits(987): last = 7, all_but_last = 98,return sum_digits(98) + 7
2. sum_digits(98): last = 8, all_but_last = 9, return sum_digits(9) + 8
3. sum_digits(9): return 9

so sum_digits(987) = sum_digits(98) + 7 = sum_digits(9) + 8 + 7 = 9 + 8 + 7 = 24
"""

"""给定一个整数n，求n的阶乘，不使用递归"""
def fac(n):
    total,k=1,1
    while k<=n:
        total,k = total * k, k+1
    print(total)
    return total 

"""给定一个整数n，求n的阶乘，使用递归"""
def fac_recur(n):
    if n<=2:
        return n
    else:
        n_minus_one = n - 1
        return fac_recur(n_minus_one) * n

"""
fac_recur(5)
1. fac_recur(5): return fac_recur(4) * 5
2. fac_recur(4): return fac_recur(3) * 4
3. fac_recur(3): return fac_recur(2) * 3
4. fac_recur(2): return 2

so fac_recur(5) = 2 * 3 * 4 * 5
"""

a = fac_recur(5)
print(a)