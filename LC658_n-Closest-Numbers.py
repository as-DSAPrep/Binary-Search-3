"""
Using Max - Heap
we Use Max Heap. Put the values and their abs distance to x in the heap
Maintain heap size of k and pop out elements with max distance if heap starts growing
Ultimately return heap values in sorted manner
TC = nlog k +klogk 
SC = space required to store the elements in the heap = O(k)
"""

import heapq

class comparator:
    def __init__(self, val, diff):
        self.val = val
        self.diff = diff
    def __lt__(self, other):
        #If the distance is same go for the lower value
        if self.diff==other.diff:
            return self.val>other.val
        else:
            return self.diff>other.diff
        
        
        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []
        for i in range(len(arr)):
            heapq.heappush(maxheap, comparator(arr[i], abs(arr[i]-x)))
            
            if len(maxheap)>k:
                heapq.heappop(maxheap)
                
        result = []
        while len(maxheap)!=0:
            result.append(heapq.heappop(maxheap).val)
        return sorted(result)

"""
Two pointer Approach : we will maintain pointers at the start and end of the arry and move away from the position where the distance is more, keep doing this till the distance between two pointers is = k
        in case we come across same values at two pointers, we move away from the right(to pick the smaller element)

Time Complexity: O(n-k)
Space Complexity: O(1)

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)==0:
            return []
        n = len(arr)
        start = 0
        end = n-1
        #Till the gap is greated than k, keep on reducing the gap
        while end-start+1>k:
            start_dis = abs(arr[start]-x)
            end_dis = abs(arr[end]-x)
            
            if start_dis>end_dis:
                start+=1
            else:
                end-=1
        result = []
        for i in range(start, end+1):
            result.append(arr[i])
            
        return result
            
        
"""
*MODIFIED* Binary Search approach

We will do binary search to find the correct location for start index, we will not look for the element while searching
low = 0 
high = n-k
Our start index will never go beyond this. But, we will be taking an element extra on the RHS to handle the case of equal distances
we will consider the lower index, and we will be sure that it will be on the left side and we have to keep moving towards left

At every instance, we assume mid to be the start index and the range of result would be [mid to mid+k-1]
We find the distances from these positions and keep moving towards the size where the distance is reduced

""" 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 0:
            return []
        n = len(arr)
        low = 0
        high = n-k
        
        while low<high:
            mid = low+(high-low)//2
            
            start_dis = x -arr[mid]
            end_dis = arr[mid+k]-x
            
            if start_dis>end_dis:
                low = mid+1
            else:
                high = mid
                
        result = []
        for i in range(low, low+k):
            result.append(arr[i])
            
        return result
