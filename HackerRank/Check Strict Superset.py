'''
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
sets = []
for i in range(n):
    sets.append(set(map(int, input().split())))

for _set in sets:
    if not(_set.issubset(A) and len(_set) != len(A)):
        print(False)
        break
else:
    print(True)
