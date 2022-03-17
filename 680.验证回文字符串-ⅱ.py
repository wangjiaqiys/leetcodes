#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start



class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     if not s:
    #         return False
    #     left, right = 0, len(s) - 1
        
    #     while left < right:
    #         if s[left] != s[right]:
    #             break
    #         left += 1
    #         right -= 1

    #     if left >= right:
    #         return True

    #     return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
    
    # def isPalindrome(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]: 
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        left, right = self.findDifference(s, 0, len(s) - 1)
        if left >= right:
            return True
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isPalindrome(self, s, left, right):
        left, right = self.findDifference(s, left, right)
        return left >= right

    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right
# @lc code=end

