class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> remainders;
        int ans = 0;
        long sum = 0;
        remainders[0] = 1;

        for(int num: nums){
            sum += num;
            int current_remainder = sum%k;
            if(current_remainder < 0){
                current_remainder += k;
            }
            if(remainders.find(current_remainder) != remainders.end()){
                ans += remainders[current_remainder];
                remainders[current_remainder] += 1;
            }else{
                remainders[current_remainder] = 1;
            }
        }
        return ans;
    }
};
