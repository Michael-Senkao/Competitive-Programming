'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 
types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    
    arr = []
    for i in range(N):
        command, *line = input().split()
        if command == 'insert':
            arr.insert(int(line[0]), int(line[1]))
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(int(line[0]))
        elif command == 'append':
            arr.append(int(line[0]))
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
            
