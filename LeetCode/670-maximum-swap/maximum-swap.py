class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the integer 'num' into a list of characters representing digits
        nums = list(str(num))
        n = len(nums)  # Store the length of the list (number of digits)
        
        # Initialize three indices:
        # s1 and s2: these will store the indices of the digits to swap
        # max_i: keeps track of the index of the largest digit found from the right
        s1 = s2 = max_i = n - 1

        # Traverse the number's digits from right to left (backward loop)
        for i in range(n-1, -1, -1):
            # If the current digit is greater than the current maximum digit (from the right)
            if nums[i] > nums[max_i]:
                max_i = i  # Update the index of the largest digit found so far
            
            # If the current digit is less than the maximum digit found to the right,
            # this means we could potentially swap it to get a larger number
            if nums[i] < nums[max_i]:
                s1, s2 = i, max_i  # Record the indices of the two digits to swap

        # Swap the digits at indices s1 and s2
        nums[s1], nums[s2] = nums[s2], nums[s1]
        
        # Join the modified list back into a string, convert it to an integer, and return it
        return int("".join(nums))
