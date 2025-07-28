class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for i,num in enumerate(nums):
            if num == target:
                result.append(i)
        return result 
        # time complexity for thid code is O(nlogn) because for sorting this array is O(nlog n) and for one itteration of loop it will be  O(n) so total time complexity is O(nlogn)