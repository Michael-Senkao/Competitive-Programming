class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> answer(n,0);

        for(auto booking: bookings){
            answer[booking[0]-1] += booking[2];
            
            if(booking[1] < n){
                answer[booking[1]] -= booking[2];
            }
        }

        for(int i=1; i<n; i++){
            answer[i] += answer[i-1];
        }

        return answer;
    }
};
