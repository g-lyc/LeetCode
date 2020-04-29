# coding:utf-8

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # j = [1, 2, 3, n-1]
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)