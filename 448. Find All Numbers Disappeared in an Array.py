class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        print (count)
        for i in count.