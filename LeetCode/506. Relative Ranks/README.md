<strong>**QUESTION**</strong>

You are given an integer array <code>score</code> of size <code>n</code>, where <code>score[i]</code> is the score of the <code>ith</code> athlete in a competition. All the scores are guaranteed to be <strong>unique<strong>.

The athletes are <strong>placed<strong> based on their scores, where the <code>1<sup>st</sup></code> place athlete has the highest score, the <code>2<sup>nd</sup></code> place athlete has the <code>2<sup>nd</sup></code> highest score, and so on. The placement of each athlete determines their rank:

- The <code>1<sup>st</sup></code> place athlete's rank is <code>"Gold Medal"</code>.
- The <code>2<sup>nd</sup></code> place athlete's rank is <code>"Silver Medal"</code>.
- The <code>3<sup>rd</sup></code> place athlete's rank is <code>"Bronze Medal"</code>.
- For the <code>4<sup>th</sup></code> place to the <code>n<sup>th</sup></code> place athlete, their rank is their placement number (i.e., the <code>x<sup>th</sup></code> place athlete's rank is <code>"x"</code>).
Return an array <code>answer</code> of size <code>n</code> where <code>answer[i]</code> is the <strong>rank</strong> of the <code>i<sup>th</sup></code> athlete.


<strong>Example 1:</strong>

<strong>Input:</strong> score = [5,4,3,2,1]
<strong>Output:</strong> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
<strong>Explanation:</strong> The placements are [1st, 2nd, 3rd, 4th, 5th].

<strong>Example 2:</strong>

<strong>Input:</strong> score = [10,3,8,9,4]
<strong>Output:</strong> ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
<strong>Explanation:</strong> The placements are [1st, 5th, 3rd, 2nd, 4th].

 
<strong>Constraints:</strong>

- <code>n == score.length</code>
- <code>1 <= n <= 104</code>
- <code>0 <= score[i] <= 106</code>
- All the values in <code>score</code> are <strong>unique</strong>.
