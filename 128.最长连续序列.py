#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or nums is None:
            return 0
        if len(nums) == 1:
            return 1
        nums = sorted(list(set(nums)))
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
# @lc code=end

