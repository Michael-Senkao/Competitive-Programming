class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        unordered_map<int, int> prefix;
        int sum = 0;

        for(int i=0; i<n; i++){
            sum+=nums[i];
            ans += (sum == k);
            if(prefix.find(sum-k) != prefix.end()){
                ans += prefix[sum-k];
            }
            prefix[sum] += 1;
        }
        
        return ans;
    }
};
