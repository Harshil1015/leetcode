class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        value=max(count,key=count.get)
        return value