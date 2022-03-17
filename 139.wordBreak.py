# coding:utf-8

def wordBreak(s, wordDict):
    """
    @param: s str
    @param: wordDict list

    @return: True or False
    """
    if not s:
        return True

    if not wordDict:
        return False

    # 最长单词的长度 - 剪枝
    max_length = len(max(wordDict, key = len))

    def dfs(s, index, max_length, word_dict, memo):
        if index in memo:
            return memo[index]
        if index == len(s):
            return True

        for end in range(index + 1, len(s) + 1):
            if (end - index) > max_length:
                break
            word = s[index : end]
            print(word)
            if word not in word_dict:
                continue

            if dfs(s, end, max_length, word_dict, memo):
                return True

        memo[index] = False

    return dfs(s, 0, max_length, wordDict, {})

if __name__ == '__main__':
    #s = "leetcode"
    #wordDict = ['leet', 'code']
    #s = "applepenapple"
    #wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))

