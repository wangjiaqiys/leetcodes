/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
 */

// @lc code=start
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_set<int> result_set;
        std::unordered_set<int> ref_set(nums1.begin(), nums1.end());
        for (int num : nums2) {
            if (ref_set.find(num) != ref_set.end()) {
                result_set.insert(num);
            }
        }
        return vector<int>(result_set.begin(), result_set.end());
    }
};
// @lc code=end

