<h2><a href="https://leetcode.com/problems/compare-version-numbers/">165. Compare Version Numbers</a></h2> 
Given two version numbers, <code>version1</code> and <code>version2<code>, compare them.

Version numbers consist of <strong>one or more revisions</strong> joined by a dot <code>'.'</code>. Each revision consists of <strong>digits</strong> and may contain leading zeros. 
Every revision contains <strong>at least one character</strong>. Revisions are <strong>0-indexed from left to right</strong>, with the leftmost revision being revision 0, the next revision 
being revision 1, and so on. For example <code>2.5.33</code> and <code>0.1</code> are valid version numbers.

To compare version numbers, compare their revisions in <strong>left-to-right order</strong>. Revisions are compared using their <strong>integer value ignoring any leading zeros</strong>. 
This means that revisions <code>1</code> and <code>001</code> are considered equal. If a version number does not specify a revision at an index, then treat the revision as <code>0</code>. 
For example, version <code>1.0</code> is less than version <code>1.1</code> because their revision 0s are the same, but their revision 1s are <code>0</code> and <code>1</code> respectively, and <code>0 < 1</code>.

<strong><em>Return the following:</em></strong>
<ul>
  <li>If <code>version1 < version2</code>, return <code>-1</code>.</li>
  <li>If <code>version1 > version2</code>, return <code>1</code>.</li>
  <li>therwise, return <code>0</code>.</li>
</ul>
