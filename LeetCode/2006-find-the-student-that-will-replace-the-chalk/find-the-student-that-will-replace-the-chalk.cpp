class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        unsigned long sum = 0;
        int i = 0;
        for(int ch: chalk){
            sum += ch;
        }

        k %= sum;
        while(chalk[i] <= k){
            k -= chalk[i];
            i ++;
        }
        return i;
    }
};