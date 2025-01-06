class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls_to_left = int(boxes[0])
        moves_to_left = 0
        balls_to_right = int(boxes[-1])
        moves_to_right = 0

        # Single pass: calculate moves from both left and right
        for i in range(1,n):
            # Left pass
            moves_to_left += balls_to_left
            balls_to_left += int(boxes[i])
            answer[i] += moves_to_left

            # Right pass
            j = n - 1 - i
            moves_to_right += balls_to_right
            balls_to_right += int(boxes[j])
            answer[j] += moves_to_right

        return answer