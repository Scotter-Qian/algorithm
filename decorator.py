"""
def dec(f):
    n = 3
    def wrapper(*args, **kw):
        return f(*args, **kw)*n
    return wrapper

@dec
def foo(n):
    return n*2

print(foo(2))

@dec 的作用是把原foo函数（待装饰函数）赋值给dec函数（装饰器），然后将
返回值wrapper函数（已装饰函数）重新赋值给foo函数。
"""
"""
def dec(f):
    n=1
    print("--开始装饰--")
    def warraper(*args, **kwargs):
        print("---111---")
        result = f(*args, **kwargs)/4
        return result
    print(n)
    return warraper

@dec
def foo(a):
    print("--%d--"%a)
    return a

print(foo(12))
#首先执行dec())函数，不执行wrapper函数，当遇到return warraper时，执行
#wapper函数，当遇到result = f(*args, **kwargs)/3时，执行dec(foo(12))
#中的foo(12),return 的值是12(return a), 最后，result=12/3,return.返回的
#是经过装饰后的值。
"""
"""
def topk(nums):
    s = []
    for i in nums:
        if i not in s:
            s.append(i)
    t = []
    for j in s:
        b = nums.count(j)
        t.append([b,j])
    print(t)
    t = sorted(t, key=lambda x: x[0])
    print(t)
    t.pop(1)
    print(t)
    #for k in
    if t[-2] != t[-1]:
        return t[-2][1] + t[-1][1]
s = [2,2,2,2,2,3,4,4,4]
print(topk(s))
"""
"""
def  schedule(data):
    s = []
    for i in data:
        if i not in s:
            s.append(i)
    print(s)
    num_total=[]
    for j in s:
        for l in s:
            if j[0] < l[0] and j[1]> l[1]:
                num_total.append(1)
        num = data.count(j)
        #print(num)
        if num > 1:
            num_total.append(num-1)
    return sum(num_total)

t = [(8.0,10.0),(8.0, 10.0),(8.0,10.0),(8.0, 10.0), (12.0,14.5),(9.0,9.5)]
print(schedule(t))


"""
"""
arr = list(map(int, input().split()))
print(arr)
s = 0
for i, m in enumerate(arr):
    s += m*10**(len(arr)-i-1)
print(s)
"""
"""
def fab(n):
    if n<1:
        return "No"
    else:
        if n==1 or n==2:
            return 1
        else:
            return fab(n-1)+fab(n-2)
value = int(input(":"))
result = fab(value)
print(result)
"""
"""
def hanoi(n, x, y, z):
    if n==1:
        print(x,"-->", z)
    else:
        hanoi(n-1, x, z, y)
        print(x, "-->", z)
        hanoi(n-1, y, x, z)
level = int(input(":"))
hanoi(level, "x", "y", "z")

"""
import numpy as np
s = np.random.randint(1,8,7)
print(s, '\n', s.size, '\n', s.shape, "\n", s.dtype, "\n", s.ndim)


