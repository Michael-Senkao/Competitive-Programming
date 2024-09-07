/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        ListNode *dummy = NULL, *prev = NULL;
        dummy = prev = new ListNode();
        dummy->next = NULL;

        while(head != NULL){
            if(nums_set.find((head->val)) == nums_set.end()){
                prev->next = head;
                prev = head;
            }
            head = head->next;
        }

        prev->next = NULL;
        return dummy->next;
    }
};