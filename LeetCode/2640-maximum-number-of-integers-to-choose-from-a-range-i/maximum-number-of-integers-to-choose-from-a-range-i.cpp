class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        int ans=0, sum=0;
        set<int> arr;
        for(auto i: banned){
            if(i <= n)
                arr.insert(i);
        }
        
        for(int i=1;i<=n;i++){
            if(arr.find(i)==arr.end()){
                sum+=i;
                if(sum<=maxSum){
                    ans++;
                }else{
                    return ans;
                }
            }
        }
        return ans;
    }
};