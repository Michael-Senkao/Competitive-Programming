'''
In this challenge, you will be given  integers, n and m. There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int, input().split())

A = defaultdict(list)
B = []

for i in range(1, n+1): 
    A[input()].append(i)
    
for i in range(m):
    B.append(input())

for char in B:
    if len(A[char]) == 0:
        print(-1)
    else:
        for index in A[char]:
            print(index, end=" ")
        print()
