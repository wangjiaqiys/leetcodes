# coding:utf-8

# 找到可以和word接龙的所有单词
# 如：word = 'hot', dict = {'hot', 'hit', 'hog'}, return ['hit', 'hog']
def get_next_words(word, dict):
    next_words = []
    for i in range(len(word)):
        left, right = word[:i], word[i+1:]
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == char:
                continue
            # 在s中，把位置index的字母替换成c，返回替换后的字符串
            new_word = left + char + right
            if new_word in dict:
                next_words.append(new_word)
    return next_words

