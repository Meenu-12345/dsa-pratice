
from rpds import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
       non_dup = list(set(nums))
       nums.clear()
       nums.extend(non_dup)
       return len(nums)

