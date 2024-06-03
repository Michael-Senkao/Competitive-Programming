#Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        stack = []
        
        for num in A:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
            
        return stack
