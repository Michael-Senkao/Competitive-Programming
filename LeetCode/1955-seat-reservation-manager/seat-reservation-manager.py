class SeatManager:

    def __init__(self, n: int):
        self.next = 1
        self.seats = []

    def reserve(self) -> int:
        if self.seats:
            return heappop(self.seats)
        self.next += 1
        return self.next - 1

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)