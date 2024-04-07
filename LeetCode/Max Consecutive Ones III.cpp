/* 
QUESTION:
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.
*/


class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        int left = 0, right = 0, zeros = 0;

        // Iterate over nums with a dynamic window
        while(right < n){
            if(nums[right] == 0){
                zeros++;
            }

            // Shrink the window until the current window contains not more than k zeros
            while (left <= right && zeros > k){
                if(nums[left] == 0){
                    zeros--;
                }

                left++;
            }

            // Choose the best answer
            ans = max(ans, right - left + 1);
            right++;
        } 

        return ans;
    }
};
