We have an array of integers, <code>nums</code>, and an array of <code>requests</code> where <code>requests[i] = [starti, endi]</code>. The <code>ith</code> request asks for the sum of <code>nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]</code>. Both <code>starti</code> and <code>endi</code> are 0-indexed.

<em>Return the maximum total sum of all requests</em> <strong>among all permutations</strong> of <code>nums</code>.

Since the answer may be too large, return it <strong>modulo</strong> <code>109 + 7</code>.
