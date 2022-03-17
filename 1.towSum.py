def twoSum(nums, target):
    hashSet = dict()
    for index, num in enumerate(nums):
        if hashSet.get(target - num, None) != None:
            return [hashSet.get(target - num), index]
        hashSet[num] = index
    return [-1, -1]

if __name__ == '__main__':
    res = twoSum([2, 7, 11, 15], 9)
    import pdb;pdb.set_trace()

