class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):                
                if sum(nums[i:j+1])==k:
                    total+=1
        return total
        