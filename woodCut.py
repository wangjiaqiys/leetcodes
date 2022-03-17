# coding:utf-8

def woodCut(L, target):
    if not L:
        return -1
    start, end = 1, min(max(L), sum(L) // target) # 切的最小长度和最大长度
    if end < 1:
        return 0
    while start + 1 < end:
        mid = start + (end - start) // 2
        if get_count(L, mid) >= target:
            start = mid
        else:
            end = mid
    return end if get_count(L, end) >= target else start

def get_count(L, length):
    return sum([l // length for l in L])

if __name__ == '__main__':
    L = [4, 6, 7, 8]
    target = 3
    max_len = woodCut(L, target)
    print('可切割的最大长度为: ', max_len)

