#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = dict()
        for index, num in enumerate(nums):
            if hashSet.get(target - num, None):
                return [hashSet.get(target - num) - 1, index] # 考虑到第0个位置，dict.get() 也是 False
            hashSet[num] = index + 1
        return [-1, -1]
# @lc code=end

