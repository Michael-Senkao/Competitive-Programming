class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i = 0
        n = len(formula)

        while i < len(formula):
            ch = formula[i]
            i += 1
            if ch in {'(', ')'}:
                stack.append(ch)
            elif ch.isalpha():
                element = ch
                while i < len(formula) and formula[i].islower():
                    element += formula[i]
                    i += 1

                count = ""
                while i < len(formula) and formula[i].isnumeric():
                    count += formula[i]
                    i += 1
                if not count:
                    count = "1"

                stack.append([element, int(count)])
            else:
                while i < n and formula[i].isnumeric():
                    ch += formula[i]
                    i += 1
                stack.pop()
                j = -1
                ch = int(ch)
                while stack[j] != '(':
                    stack[j][1]*= ch
                    j -= 1
                stack.pop(j)
                
        count = defaultdict(int)
        for x in stack:
            if x[0].isalpha():
                count[x[0]] += x[1]
                
        res = [key for key in count.keys()]
        res.sort()
        for i,e in enumerate(res):
            if count[e] > 1:
                res[i] += str(count[e])

        # print(res)
        return "".join(res)

