class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        roots = set()
        result = []
        
        folder = [f.split('/') for f in folder]
        folder.sort(key=lambda x: len(x))
        
        for f in folder:
            sub_folder = []
            for i in range(1, len(f)):
                sub_folder.append(f[i])
                if tuple(sub_folder) in roots:
                    break
            else:
                roots.add(tuple(sub_folder))

        for root in roots:
            curr = []
            for f in root:
                curr.extend(('/', f))
            result.append("".join(curr))
        return result
        