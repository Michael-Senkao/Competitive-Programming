from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calender = SortedList()

    def book(self, start: int, end: int) -> bool:
        if not self.binarySearch(start, end):
            return False

        self.calender.add((start, end))
        return True

    
    def binarySearch(self, start, end):
        if not self.calender: 
            return True

        left,right = 0, len(self.calender) - 1
        while left <= right:
            mid = left + (right - left)//2
            if start >= self.calender[mid][1]:
                left = mid + 1
            elif end <= self.calender[mid][0]:
                right = mid - 1
            else:
                return False
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)