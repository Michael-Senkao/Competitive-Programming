class Solution:
	def isPalindrome(self, S):
		'''
      APPROACH: Two pointers
    '''
		start,end = 0,len(S)-1
		
		while start < end:
		    if S[start] != S[end]:
		        return 0
		    start += 1
		    end -= 1
		    
		return 1
