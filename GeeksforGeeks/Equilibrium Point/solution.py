class Solution:
    '''
      APPROACH: prefix and suffix sum
    '''
  
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        
        sufix_sum = sum(A)
        prefix_sum = 0

        for i in range(N):
            sufix_sum -= A[i]
            if sufix_sum == prefix_sum:
                return i + 1
            
            prefix_sum += A[i]
        return -1
            
