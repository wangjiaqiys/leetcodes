#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        answer = (0, 0) # (lenth, start_index)
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrome_from(s, mid, mid))
            answer = max(answer, self.get_palindrome_from(s, mid, mid + 1))
        return s[answer[1]: answer[0] + answer[1]]
    
    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1, left + 1
    # @lc code=end
    

