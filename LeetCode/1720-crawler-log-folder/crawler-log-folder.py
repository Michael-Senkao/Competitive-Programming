class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = len(logs)
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        
        return len(stack)