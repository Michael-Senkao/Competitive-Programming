class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        priority_queue<pair<int, int>> pqueue;
        vector<string> answer(n);
        
        // Create a max heap priority queue of pairs (score, index)
        for(int i=0; i<n; i++){
            pqueue.push(make_pair(score[i], i));
        }

        // Assign ranks to the top 3 athletes (could be only 2 or 1)
        if(n >= 3){
            answer[pqueue.top().second] = "Gold Medal";
            pqueue.pop();
            answer[pqueue.top().second] = "Silver Medal";
            pqueue.pop();
            answer[pqueue.top().second] = "Bronze Medal";
            pqueue.pop();
        }else if(n==2){
            answer[pqueue.top().second] = "Gold Medal";
            pqueue.pop();
            answer[pqueue.top().second] = "Silver Medal";

            return answer;
        }else{
            answer[0] = "Gold Medal";
            
            return answer;
        }
        
        // Assign ranks to rest of the athletes
        for(int i=4; i<=n; i++){
            answer[pqueue.top().second] = to_string(i);
            pqueue.pop();
        }
        return answer;
    }
};
