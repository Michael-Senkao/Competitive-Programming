class Solution:
	def print2largest(self,arr, n):
		largest = arr[0]
		second_largest = -1
		
		for num in arr:
		    if num > largest:
		        second_largest = largest
		        largest = num
		    elif num > second_largest and num != largest:
		        second_largest = num
		        
        return second_largest
