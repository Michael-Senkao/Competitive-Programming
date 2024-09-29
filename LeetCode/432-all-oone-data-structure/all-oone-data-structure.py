class AllOne:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(set)
        self.max = float('-inf')
        self.min = float('inf')
        

    def inc(self, key: str) -> None:
        key = tuple(key)
        if key in self.freq:
            self.count[self.freq[key]].discard(key)
            if not self.count[self.freq[key]]:
                if self.min == self.freq[key]:
                    self.min = float('inf')
                del self.count[self.freq[key]]
        
        self.freq[key] += 1
        self.count[self.freq[key]].add(key)
        
        self.min = min(self.min, self.freq[key])
        self.max = max(self.max, self.freq[key])
        # print(self.freq)
        # print(self.count)
        # print(self.max, self.min, "\n")

    def dec(self, key: str) -> None:
        key = tuple(key)
        self.count[self.freq[key]].discard(key)
        if not self.count[self.freq[key]]:
            del self.count[self.freq[key]]
            if self.max == self.freq[key]:
                self.max = float('-inf')
            if self.min == self.freq[key]:
                self.min = float('inf') if not self.count else min(self.count.keys())
            
        if self.freq[key] == 1:
            del self.freq[key]
            return

        self.freq[key] -= 1
        self.count[self.freq[key]].add(key)
        self.min = min(self.min, self.freq[key])
        self.max = max(self.max, self.freq[key])
        # print(self.freq)
        # print(self.count)
        # print(self.max, self.min, "\n")
        

    def getMaxKey(self) -> str:
        if self.max < 0:
            return ""
        for s in self.count[self.max]:
            return "".join(s)
        

    def getMinKey(self) -> str:
        if self.max < 0:
            return ""
        for s in self.count[self.min]:
            return "".join(s)
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()