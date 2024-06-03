class Solution:
    def missingNumber(self,array,n):
      ''' Alternative: Cyclic sort
        i = 0
        
        while i < n-1:
            index = array[i] - 1
            
            while index < n-1 and index != i:
                array[i],array[index] = array[index],array[i]
                index = array[i] - 1
            
            i += 1
        
        for i in range(1,n):
            if array[i-1] != i:
                return i
        return n
        '''
        
        res = 0
        
        # Take all xors
        for i in range(1, n+1):
            res ^= i
        
        # Xor with the numbers in 'array'
        for num in array:
            res ^= num
        
        return res
