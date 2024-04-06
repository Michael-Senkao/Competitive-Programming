/* 
QUESTION:
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
He wants to confuse the students by maximizing the number of consecutive questions with the same 
answer (multiple trues or multiple falses in a row).
You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
*/

class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int left = 0, right = 0, true_count=0, false_count=0;
        int ans = 0, n = answerKey.size();

        while(right < n){
            if(answerKey[right] == 'T'){
                true_count++;
            }else{
                false_count++;
            }

            while(min(true_count, false_count) > k){
                if(answerKey[left] == 'T'){
                    true_count--;
                }else{
                    false_count--;
                }
                left++;
            }

            ans = max(ans, right - left+1);
            right++;
        }

        return ans;
    }
};
