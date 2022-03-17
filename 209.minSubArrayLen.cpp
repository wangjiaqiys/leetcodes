/* 
给定一个含有n个正整数的数组和一个正整数target 。
找出该数组中满足其和≥ target的长度最小的连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回0 。
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
*/
#include<iostream>
#include<vector>
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) {
	int result = INT_MAX;
	int slowIndex = 0;
	int curSum = 0;
	for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++) {
    	curSum += nums[fastIndex];
    	while (curSum - nums[slowIndex] >= target) {
        	curSum -= nums[slowIndex];
        	slowIndex++;
    }
    	if (curSum == target) {
            cout << fastIndex - slowIndex + 1 << endl;
        	result = result >= (fastIndex - slowIndex + 1) ? (fastIndex - slowIndex + 1) : result;
        }
	}
	return result;
}

int main() {
    vector<int> nums = {2,3,1,2,4,3}; 
	int target = 7;
    int result = 0;
    result = minSubArrayLen(target, nums);
    cout << result << endl;
    return 0;
}

