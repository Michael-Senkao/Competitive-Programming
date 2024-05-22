class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        queue = deque(range(n))
        ans = [0]*n

        for card in deck:
            ans[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())

        return ans
