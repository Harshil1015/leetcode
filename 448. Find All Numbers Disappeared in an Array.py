class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        result=[]
        length=len(nums)
        for i in range(1,length+1):
            if i not in count:
                result.append(i)
        return result