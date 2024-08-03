class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n,m = len(nums1),len(nums2)
        heap = []
        result = []
        visited = set()
        heapify(heap)

        heappush(heap, (nums1[0] + nums2[0], 0,0))
        visited.add((0,0))
        while k:
            _, i,j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            if i + 1 < n and (i+1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i+1,j))
                visited.add((i+1, j))
            if j + 1 < m and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result