
class Solution:
    def segregateElements(self, arr):
      
        j=0
        for i in range(len(arr)):
            if arr[i]>=0:
                arr[i],arr[j] = arr[j],arr[i]
                j+1

        # all +ve would be one side and all the -ve will be another side, but -ve one will not be in order

