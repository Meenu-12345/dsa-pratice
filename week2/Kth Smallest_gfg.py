class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        #sort the array usind sort() method
        arr.sort()
        return arr[k-1] 
        
