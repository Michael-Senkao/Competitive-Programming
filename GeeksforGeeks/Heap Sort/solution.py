class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        max_index = i
        left = 2*i + 1
        right = left + 1
        
        if left < n and arr[left] > arr[max_index]:
            max_index = left
        if right < n and arr[right] > arr[max_index]:
            max_index = right
        if max_index != i:
            arr[max_index],arr[i] = arr[i],arr[max_index]
            self.heapify(arr, n, max_index)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n, -1, -1):
           self.heapify(arr, n, i)
    
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr, i, 0)
