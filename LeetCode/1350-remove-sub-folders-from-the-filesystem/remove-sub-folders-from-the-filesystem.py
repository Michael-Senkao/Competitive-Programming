class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        roots = set()
        result = []

        folder.sort(key=lambda x: x.count('/'))
        
        for f in folder:
            sub_folder = []
            i = 0
            while i < len(f):
                sub_folder.append(f[i] + f[i+1])
                
                i += 2
                while i < len(f) and f[i] != '/':
                    sub_folder[-1] += f[i]
                    i += 1
                
                if tuple(sub_folder) in roots:
                    break
            else:
                roots.add(tuple(sub_folder))

        return ["".join(root) for root in roots]
        