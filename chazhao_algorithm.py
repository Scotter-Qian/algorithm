"""
#顺序查找
def sequential_search(s, item):
    start = 0
    found = False
    while start<len(s) and not found:
        if s[start] ==  item:
            found = True
        else:
            start += 1
    return found
s = [1,2,3,4,5,6]
print(sequential_search(s,2))
print(sequential_search(s,7))
"""

"""
#二分查找

def binary_search(s, item):
    start = 0
    end = len(s)-1
    found = False
    while start<=end and not found:
        middle_point = (start + end)//2
        if s[middle_point] == item:
            found = True
        else:
            if s[middle_point] > item:
                end = middle_point - 1
            else:
                start = middle_point + 1
    return found

s = [0,1,2,3,4]
print(binary_search(s,2))
print(binary_search(s,5))
"""


