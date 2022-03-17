#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True 
        if not wordDict:
            return False 
        max_length = len(max(wordDict, key = len))
        def dfs(s, index, max_length, wordDict, memo):
            if index in memo:
                return memo[index]
            if index == len(s):
                return True 
            for end in range(index + 1, len(s) + 1):
                # 剪枝
                if (end - index) > max_length:
                    break
                if s[index: end] not in wordDict:
                    continue
                if dfs(s, end, max_length, wordDict, memo):
                    return True
            memo[index] = False

        return True if dfs(s, 0, max_length, wordDict, {}) else False
# @lc code=end

