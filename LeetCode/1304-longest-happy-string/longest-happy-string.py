class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def pushTwo(ch):
            result.extend([ch, ch])
                
        def pushOne(ch):
            result.append(ch)
                
        max_heap = []
        result = []

        if a:
            max_heap.append((-a, 'a'))
        if b:
            max_heap.append((-b, 'b'))
        if c:
            max_heap.append((-c, 'c'))
        
        if not max_heap:
            return ""
        if len(max_heap) == 1:
            if max_heap[0][0] < -1:
                pushTwo(max_heap[0][1])
            else:
                pushOne(max_heap[0][1])
            return "".join(result)

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first, ch = heapq.heappop(max_heap)
            second, sec_ch = heapq.heappop(max_heap)

            f,s = -1,-1
            if first < -1:
                pushTwo(ch)
                f = 2
            else:
                pushOne(ch)
                f = 1
            
            if abs(first) - abs(second) > 2 or second == -1:
                pushOne(sec_ch)
                s = 1
            else:
                pushTwo(sec_ch)
                s = 2

            first += f
            second += s
            if first != 0:
                heappush(max_heap, (first, ch))
            if second != 0:
                heappush(max_heap, (second, sec_ch))

        if not max_heap or max_heap[0][1] == result[-1]:
            return "".join(result)
        if max_heap[0][0] < -1:
            pushTwo(max_heap[0][1])
        else:
            pushOne(max_heap[0][1])

        return "".join(result)