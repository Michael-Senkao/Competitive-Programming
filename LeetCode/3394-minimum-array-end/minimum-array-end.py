class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Step 1: Create a bitmask for the last (n-1) bits.
        bit_mask = n - 1
        # Initialize result variable.
        res = 0
        # Current bit position.
        pw = 0
        
        # Step 2: Process each bit of x and bit_mask
        while x > 0 or bit_mask > 0:
            # If current bit of x is 0, use the corresponding bit from bit_mask.
            if x & 1 == 0:
                res |= (bit_mask & 1) << pw
                bit_mask >>= 1  # Shift bit_mask to process the next bit
            else:
                res |= (x & 1) << pw  # Set the bit from x
            
            # Shift x to process the next bit.
            x >>= 1
            # Increment bit position (power counter).
            pw += 1
        
        # Return the final result.
        return res
