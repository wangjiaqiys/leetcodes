# coding:utf-8

def longestConsecutive(nums):
    if not nums or nums is None:
        return 0
    if len(nums) == 1:
        return 1
    nums.sort()
    import pdb;pdb.set_trace()
    slow, fast = 0, 1
    tmp = slow 
    length = 0
    while slow < len(nums) and fast < len(nums):
        if nums[fast] - nums[tmp] == 1:
            tmp += 1
            fast += 1
        else:
            length = max(length, fast - slow)
            slow = fast 
            tmp = slow 
            fast += 1
    return max(length, fast - slow)

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))

