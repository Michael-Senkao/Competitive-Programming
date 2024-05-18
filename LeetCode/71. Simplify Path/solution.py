class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        i = 0

        while i < n:
            current = path[i]
            i += 1
            if current  != '/':
                while i < n and path[i] != '/':
                    current += path[i]
                    i += 1
            else:
                while i < n and path[i] == '/':
                    current += path[i]
                    i += 1
                    
            
            if current =='..':
                if stack:
                    stack.pop()
                    stack.pop()
            elif current[0] != '/' and current != '.':
                stack.extend(['/', current])

            
        if not stack:
            stack = ['/']

        return "".join(stack)
