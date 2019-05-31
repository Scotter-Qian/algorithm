import time

def bubbleSort(s):
    #平均复杂度为O(n^2),稳定的排序
    #assert (type(s)==type(['']))
    length = len(s)
    if length<=1:
        return s
    else:
        for i in range(length-1):
            for j in range(length-i-1):
                if s[j]>s[j+1]:
                    s[j], s[j+1]=s[j+1],s[j]
    return s

def buble_short(s):
    exchanges = True
    num = len(s)-1
    while num>0 and exchanges:
        exchanges = False
        for i in range(num):
            if s[i]>s[i+1]:
                exchanges = True
                s[i],s[i+1] = s[i+1],s[i]
        num = num -1
    return s


def selectSort(s):
    #不稳定，平均复杂度O(n^2)
    assert (type(s)==type(['']))
    length = len(s)
    if length <= 1:
        return s
    def _min(t):
        min_index = t
        for i in range(t, length):
            if s[i] < s[min_index]:
                min_index = i
        return min_index
    for i in range(length):
        min_index = _min(i)
        if i != min_index:
            s[i],s[min_index] = s[min_index], s[i]
    return s

def selection_sort(s):
    for replace_place in range(len(s)-1, 0, -1):
        position_max = 0
        for location in range(1, replace_place+1):
            if s[location] > s[position_max]:
                position_max = location
            s[replace_place],s[position_max] = s[position_max],s[replace_place]
    return s



def insertionSort(s):
    #平均复杂度：O(n**2)
    #空间复杂度：O(1)
    #稳定
    assert (type(s)==type(['']))
    length = len(s)
    if length <=1:
        return s
    for i in range(1,length):
        #取出当前未排序的数
        value = s[i]
        #从后往前，先取未排序数的前一个数（已经排好的数）
        j = i-1
        #若当前未排序的数比排序好的数还小并且还没有到数组的开头
        while j>0 and value<s[j]:
            #排好序的数组往后移一位
            s[j+1] = s[j]
            #取排序好的数的前一个进行比较
            j -= 1
            #当前要插入的排序
        s[j+1] = value
    return s

def merge_sort(s):
    #归并排序的时间复杂度是O(N*logN)
    #归并排序的形式就是一颗二叉树，它需要遍历的次数就是二叉树的深度，而根据完全二叉
    #树的可以得出它的时间复杂度是O(N*logN)
    #归并排序是稳定的算法
    #算法稳定性：假设在数列中存在a[i]=a[j],若在排序之前，a[i]在a[j]前面；并且排序之后，
    #a[i]仍然在a[j]前面，则这个算法是稳定的。
    length = len(s)
    if length <= 1:
        return s
    num = int(length/2)
    left = merge_sort(s[:num])
    right = merge_sort(s[num:])

    def merge(left, right):
        s = []
        m = n = 0
        while m < len(left) and n < len(right):
            if left[m] < right[n]:
                s.append(left[m])
                m += 1
            else:
                s.append(right[n])
                n += 1
        s += left[m:]
        s += right[n:]
        return s

    return merge(left, right)


def quickSort(array, l, r):
    if l<r:
        q = partition(array, l, r)
        quickSort(array, l, q-1)
        quickSort(array, q+1, r)
    return array

def partition(array, l, r):
    x = array[r]
    i = l-1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i],array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

s =[1, 2, 2, 6, 3, 5, 2, 3, 5, 6, 8, 9]
l = 0
r = len(s)-1

print(selection_sort(s))