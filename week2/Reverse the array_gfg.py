class Solution:
    def reverseArray(self, arr):
        # left , right
        left = 0 
        right = len(arr)-1
        # while left < right
        while left < right:
            # temp arr[left]
            temp = arr[left]
            # arr[left] = arr[right]
            arr[left] = arr[right]
            # arr[right] = temp
            arr[right] = temp
            left += 1
            right 