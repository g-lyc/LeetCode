# coding:utf-8


def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low <high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时，low==high
    alist[low] = mid_value

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low-1)

    # 对low右边的列表排序
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)

