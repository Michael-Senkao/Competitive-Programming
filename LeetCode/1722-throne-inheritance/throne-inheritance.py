class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.family = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.root)

    def dfs(self, node):
        stack = [node]
        res = []

        while stack:
            curr = stack.pop()
            if curr not in self.dead:
                res.append(curr)

            for child in self.family[curr][::-1]:
                stack.append(child)

        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()