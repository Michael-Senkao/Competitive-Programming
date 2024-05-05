class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
       
        int n = nums.size();
        const int LIMIT = pow(10, 9) + 7;
        unsigned int ans = 0;
        int index = n - 1;

        vector<int> range_sum(n,0);

        // Compute the range sum from the requests
        for(auto request: requests){
            range_sum[request[0]] += 1;

            if(request[1] + 1 < n){
                range_sum[request[1] + 1] -= 1;
            }
        }

        // Compute the prefix sum of the range sum
        for(int i=1; i<n; i++){
            range_sum[i] += range_sum[i-1];
        }

        // Sort both nums and the prefix sum arrays
        sort(nums.begin(), nums.end());
        sort(range_sum.begin(), range_sum.end());

        // Greedy method: multiply the highest prefix sum with the highest value in nums. 
        //Do the same for the 2nd, 3rd,... highests and sum them to get the answer
        while(index >= 0 && range_sum[index]){
            ans = (ans + ((unsigned long)nums[index]*range_sum[index])) % LIMIT;
            index -= 1;
        }

        return ans;
    }
};
