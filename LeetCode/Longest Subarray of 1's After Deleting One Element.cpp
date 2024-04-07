/* 
QUESTION:
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.
*/

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        int left = 0, right = 0, zeros = 0;
        
        // Iterate over nums with a dynamic window
        while(right < n){
            // If currrent element is zero, increase the count of zeros in the window
            if(nums[right] == 0){
                zeros++;
            }

            // Shrink the window until there is at most 1 zero in the window
            while(left <= right && zeros > 1){
                if(nums[left] == 0){
                    zeros--;
                }

                left++;
            }
            
            // Choose the best window
            ans = max(ans, right - left);
            right++;
        } 

        return ans;
    }
};
