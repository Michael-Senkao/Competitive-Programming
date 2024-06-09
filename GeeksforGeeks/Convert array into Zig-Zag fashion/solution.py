class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        
        for i in range(1, n):
            if i % 2 == 1 and arr[i] < arr[i-1] or i % 2 == 0 and arr[i] > arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
            
