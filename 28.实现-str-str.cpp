/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */

// @lc code=start
class Solution {
public:
    void get_next(int *nxt, const string &t) {
        int j = 0, k = -1;
        nxt[0] = -1;
        int tlen = t.size();
        while (j < tlen) {
            if (k == -1 || t[j] == t[k]) {
                nxt[++j] = ++k;
            }
            else {
                k = nxt[k];
            }
        }
    }
    int strStr(string haystack, string needle) {
        if (needle.size() == 0) {
            return 0;
        }
        int nxt[needle.size() + 1];
        get_next(nxt, needle);
        int start = 0, j = 0;
        int slen = haystack.length();
        int tlen = needle.length();
        while (start < slen && j < tlen) {
            if (j==-1 || haystack[start] == needle[j]) {
                start++, j++;
            }
            else {
                j = nxt[j];
            }
        }
        if (j >= tlen) {
            return start - tlen;
        }
        else {
            return -1;
        }
    }
};
// @lc code=end

