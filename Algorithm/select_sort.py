
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1): # j: 0 ~ n-2
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [9, 16, 17, 15, 11, 26]

    print(li)
    select_sort(li)
    print(li)