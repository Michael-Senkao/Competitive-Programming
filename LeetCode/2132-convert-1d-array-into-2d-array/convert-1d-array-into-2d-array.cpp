class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int len = original.size();
        if(len != m * n){
            return {};
        }

        vector<vector<int>> result;
        for(int i = 0; i < len; i += n){
            vector<int> arr;
            for(int j = i; j < i + n; j += 1){
                arr.push_back(original[j]);
            }

            result.push_back(arr);
        }

        return result;
    }
};