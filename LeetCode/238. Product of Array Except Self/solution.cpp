class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        
        //Find the product of elements before each element int the array
        int product = 1;
        for(int i=0; i<n; i++){
            ans.push_back(product);//stores the product before ith element
            product*=nums[i];
        }

        //Find the product of elements after each element and multiply it with the product before that element
        product = 1;
        for(int i=n-1; i>=0; i--){
            ans[i]*=product;
            product*=nums[i];
        }
        return ans;
    }
};
