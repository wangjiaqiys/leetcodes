/*
 * @lc app=leetcode.cn id=459 lang=cpp
 *
 * [459] 重复的子字符串
 */

// @lc code=start
class Solution {
public:
    void get_next(int* nxt, const string& t) {
        int j = 0, k = -1;
        nxt[0] = -1;
        int tlen = t.length();
        while (j < tlen) {
            if (k == -1 || t[j] == t[k]) {
                nxt[++j] = ++k;
            }
            else {
                k = nxt[k];
            }
        }
    }
    bool repeatedSubstringPattern(string s) {
        if (s.size() == 0) {
            return false;
        }
        int slen = s.size();
        int nxt[slen + 1];
        get_next(nxt, s);
        if (nxt[slen] != -1 && nxt[slen] != 0 && (slen % (slen - nxt[slen]) == 0)) {
            return true;
        }
        return false;
    }
};
// @lc code=end

