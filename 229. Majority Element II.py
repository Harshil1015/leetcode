class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        fre=Counter(nums)
        ans=[]
        for num,count in fre.items():
            if count>n/3:
                ans.append(num)
        return ans