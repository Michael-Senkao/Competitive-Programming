from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Initialize a frequency array to count the bits in the current window
        bit_freq = [0] * 30
        left = 0
        n = len(nums)
        k_bits = [int(bit) for bit in bin(k)[2:]]  # Binary representation of k as a list of bits
        min_length = n + 1  # Start with an impossibly large length for comparison

        def remove_from_window(index):
            """Update bit frequency when removing nums[index] from the window."""
            val = nums[index]
            bit_pos = 29
            while val:
                if val & 1:
                    bit_freq[bit_pos] -= 1
                val >>= 1
                bit_pos -= 1

        def is_window_valid():
            """Check if the current window's OR result meets or exceeds k."""
            # Find the highest bit position with a 1 in both bit_freq and k_bits
            i = 0
            j = 0
            freq_bit_length = 30
            k_bit_length = len(k_bits)
            
            # Skip leading zeros in bit_freq
            while i < 30 and bit_freq[i] == 0:
                i += 1
                freq_bit_length -= 1
            
            # Skip leading zeros in k_bits
            while j < len(k_bits) and k_bits[j] == 0:
                j += 1
                k_bit_length -= 1
            
            # Compare the positions to quickly decide validity
            if freq_bit_length > k_bit_length:
                return True
            if k_bit_length > freq_bit_length:
                return False

            # Check bit-by-bit alignment of freq and k
            while i < 30 and j < len(k_bits):
                if bit_freq[i] and k_bits[j]:
                    i += 1
                    j += 1
                elif k_bits[j]:  # Required bit in k not in freq
                    return False
                elif bit_freq[i]:  # Extra bit in freq not needed by k
                    return True
                else:
                    i += 1
                    j += 1

            return True

        for right in range(n):
            # Update bit frequency by adding the current number nums[right]
            num = nums[right]
            bit_pos = 29
            while num:
                bit_freq[bit_pos] += (num & 1)
                num >>= 1
                bit_pos -= 1
            
            # Try shrinking the window from the left as long as it's valid
            while left <= right and is_window_valid():
                min_length = min(min_length, right - left + 1)
                remove_from_window(left)
                left += 1

        return min_length if min_length <= n else -1