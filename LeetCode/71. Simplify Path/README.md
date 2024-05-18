## [71. Simplify Path](https://leetcode.com/problems/simplify-path)

Given an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.

In Unix-style file system context, a single period <code>'.'</code> signifies the current directory, a double period <code>".."</code> denotes moving up one directory 
level, and multiple slashes such as <code>"//"</code> are interpreted as a single slash. In this problem, treat sequences of periods not covered by the 
previous rules (like <code>"..."</code>) as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

- It must start with a single slash <code>'/'</code>.
- Directories within the path should be separated by only one slash <code>'/'</code>.
- It should not end with a slash <code>'/'</code>, unless it's the root directory.
- It should exclude any single or double periods used to denote current or parent directories.
  
Return the new path.

### **Example 1:**
<pre>
<strong>Input:</strong> path = "/home/"

<strong>Output:</strong> "/home"

<strong>Explanation:</strong>

The trailing slash should be removed.
</pre>
 
### **Example 2:**
<pre>
<strong>Input:</strong> path = "/home//foo/"

<strong>Output:</strong> "/home/foo"

<strong>Explanation:</strong>

Multiple consecutive slashes are replaced by a single one.
</pre>
### **Example 3:**
<pre>
<strong>Input:</strong> path = "/home/user/Documents/../Pictures"

<strong>Output:</strong> "/home/user/Pictures"

<strong>Explanation:</strong>

A double period ".." refers to the directory up a level.
</pre>
### **Example 4**:
<pre>
<strong>Input:</strong> path = "/../"

<strong>Output:</strong> "/"

<strong>Explanation:</strong>

Going one level up from the root directory is not possible.
</pre>
### **Example 5:**
<pre>
<strong>Input:</strong> path = "/.../a/../b/c/../d/./"

<strong>Output:</strong> "/.../b/d"

<strong>Explanation:</strong>

"..." is a valid name for a directory in this problem.
</pre>
 

### **Constraints:**

- <code>1 <= path.length <= 3000</code>
- <code>path</code> consists of English letters, digits, period <code>'.'</code>, slash <code>'/'</code> or <code>'_'</code>.
- <code>path</code> is a valid absolute Unix path.
