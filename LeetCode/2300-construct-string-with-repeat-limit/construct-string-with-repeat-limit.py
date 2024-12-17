
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s) # count and match all appearing characters
        heap = []
        heapq.heapify(heap) # max heap
        for key,value in count.items():
            heapq.heappush(heap,(-ord(key),value))
        res = []
        max_ch, max_v = heapq.heappop(heap)
        while heap:
            repeat = min(repeatLimit,max_v)
            for _ in range(repeat):
                res.append(chr(-max_ch))
            max_v-=repeat
            if max_v and heap:
                next,next_v = heapq.heappop(heap)
                res.append(chr(-next))
                if next_v > 1:
                    heapq.heappush(heap,(next,next_v-1))
            elif heap:
                max_ch,max_v = heapq.heappop(heap)
        if not res or res[-1]!=chr(-max_ch):
            for _ in range(min(repeatLimit,max_v)):
                res.append(chr(-max_ch))
        return ''.join(res)