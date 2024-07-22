class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_index = [(index, name) for index,name in enumerate(names)]
        names_index.sort(key = lambda x: -heights[x[0]])
        # print(names_index)
        return [name for index,name in names_index]