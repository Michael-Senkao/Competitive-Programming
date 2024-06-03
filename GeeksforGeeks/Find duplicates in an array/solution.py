class Solution:
    def duplicates(self, arr, n): 
	   ''' 
    		INTUITION: Find the frequency of each number in 'arr' in place
   	   '''
	   res = []
	   for num in arr:
	       num %= n # Get the actual value at current index
	       arr[num] += n # Increment the value at index 'num' by 'n'
	   
	   for i in range(n):
	       if arr[i]//n > 1: 
	           res.append(i) # Frequency of arr[i] is greater than 1
	   return res if res else [-1]
