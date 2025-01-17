class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int> visited;
        deque<int> q;
        int n = rooms.size();

        q.push_back(0);
        visited.insert(0);

        while(!q.empty()){
            int room = q.front();
            q.pop_front();

            for(int key: rooms[room]){
                if(visited.find(key) == visited.end()){
                    q.push_back(key);
                    visited.insert(key);
                }
            }
        }


        return visited.size() == n;
    }
};