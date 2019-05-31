"""
import math

def search(n):
    s = []
    for i in n:
        if i not in s:
            s.append(i)
    return s

def calculate_entropy(m):
    s = search(m)
    c_e = 0
    for j in s:
        pro = m.count(j)/len(m)
        c_e -= pro*math.log2(pro)
    return c_e


def calculate_conditional_entropy(x,y):
    s_x = search(x)
    c_c_e = 0
    for i in s_x:
        y = []
        pro = x.count(i)/len(x)
        for j in range(len(x)):
            if x[j] == 'i':
                y.append(y[j])
                print(y)
        entropy_condition_y = calculate_entropy(y)
        c_c_e -= pro * entropy_condition_y
    return c_c_e

def calculate_entropy_gain(x, y):
    ent = calculate_entropy(y)
    cent = calculate_conditional_entropy(x, y)
    ceg = ent - cent
    return ceg

if __name__=="__main__":
    n = int(input("please input a number of data set:"))
    x = []
    y = []
    for i in range(n):
        data = input().strip().split(",")
        x.append(data[0])
        y.append(data[1])
    print(calculate_entropy_gain(x, y))
"""







