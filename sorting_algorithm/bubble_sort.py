# coding:utf-8

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            # 班长从头走到尾
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

