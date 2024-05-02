class Solution {
public:
    int findMaxK(vector<int>& nums) {
        //Pointers to traverse the array from both ends
        int left_pointer = 0, right_pointer = nums.size() - 1;

        // Sort the array in ascending order
        sort(nums.begin(), nums.end());

        // Use two pointers to traverse the array from both ends
        while(left_pointer < right_pointer && nums[left_pointer] < 0 && nums[right_pointer] > 0){
            if(abs(nums[left_pointer]) == nums[right_pointer]){
                return nums[right_pointer];// Match found
            }
            if(abs(nums[left_pointer]) > nums[right_pointer]){
                left_pointer++;
            }else{
                right_pointer--;
            }
        }

        //No such integer exists in the array
        return -1;
    }
};
