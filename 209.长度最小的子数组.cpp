/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // int result = 0;
        // int slowIndex = 0;
        // int curSum = 0;
        // for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++) {
        //     curSum += nums[fastIndex];
        //     while (curSum - nums[slowIndex] >= target) {
        //         curSum -= nums[slowIndex];
        //         slowIndex++;
        //     }
        //     if (curSum >= target) {
        //         if (result == 0 || result > (fastIndex - slowIndex + 1)) {
        //             result = fastIndex - slowIndex + 1;
        //         }
        //     }
        // }
        // return result;
        int result = INT_MAX;
        int start = 0; // 起始指针
        int curSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            curSum += nums[i];
            while (curSum - nums[start] >= target) {
                curSum -= nums[start++];
            }
            if (curSum >= target) {
                result = result > (i - start + 1) ? (i - start + 1) : result;
            }
        }
        return INT_MAX == result ? 0 : result;
    }
};
// @lc code=end

