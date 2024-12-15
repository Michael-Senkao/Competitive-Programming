class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // Max-heap to store (-gain, current_passes, total_students)
        auto compare = [](const pair<double, pair<int, int>>& a, const pair<double, pair<int, int>>& b) {
            return a.first < b.first; // Max-heap based on gain
        };
        priority_queue<pair<double, pair<int, int>>, vector<pair<double, pair<int, int>>>, decltype(compare)> max_heap(compare);

        // Initialize the heap with the initial gains
        for (const auto& cls : classes) {
            int passes = cls[0], total = cls[1];
            double gain = (double)(passes + 1) / (total + 1) - (double)passes / total;
            max_heap.push({gain, {passes, total}});
        }

        // Assign extra students
        while (extraStudents > 0) {
            // Pop class with max gain
            auto top = max_heap.top();
            max_heap.pop();

            double neg_gain = top.first;
            int passes = top.second.first;
            int total = top.second.second;

            // Update class stats
            passes += 1;
            total += 1;

            // Recompute gain and push back to heap
            double new_gain = (double)(passes + 1) / (total + 1) - (double)passes / total;
            max_heap.push({new_gain, {passes, total}});

            extraStudents--;
        }

        // Compute final average
        double total_ratio = 0.0;
        while (!max_heap.empty()) {
            auto top = max_heap.top();
            max_heap.pop();
            int passes = top.second.first;
            int total = top.second.second;
            total_ratio += (double)passes / total;
        }

        return total_ratio / classes.size();
    }
};
