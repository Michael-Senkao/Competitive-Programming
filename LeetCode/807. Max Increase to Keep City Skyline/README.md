# [807. Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline)

There is a city composed of <code>n x n</code> blocks, where each block contains a single building shaped like a vertical square prism. 
You are given a <strong>0-indexed</strong> <code>n x n</code> integer matrix <code>grid</code> where <code>grid[r][c]</code> represents the height of the building located in the 
block at row <code>r</code> and column <code>c</code>.

A city's <strong>skyline</strong> is the outer contour formed by all the building when viewing the side of the city from a distance. 
The <strong>skyline</strong> from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of <strong>any number of buildings by any amount</strong> (the amount can be different per building). 
The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the 
city's <strong>skyline</strong> from any cardinal direction.

Return <em>the <strong>maximum total sum<strong> that the height of the buildings can be increased by <strong>without</strong> changing the city's <strong>skyline</strong> from 
any cardinal direction</em>.

### **Example 1:**
<img src="https://assets.leetcode.com/uploads/2021/06/21/807-ex1.png" />
<pre>
<strong>Input:</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>Output:</strong> 35
<strong>Explanation:</strong> The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> grid = [[0,0,0],[0,0,0],[0,0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Increasing the height of any building will result in the skyline changing.
 </pre>

### **Constraints:**

- <code>n == grid.length</code>
- <code>n == grid[r].length</code>
- <code>2 <= n <= 50</code>
- <code>0 <= grid[r][c] <= 100</code>
