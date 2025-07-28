class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        # result=[]
        # for i,num in enumerate(nums):
        #     if num == target:
        #         result.append(i)
        # return result 
        # time complexity for thid code is O(nlogn) because for sorting this array is O(nlog n) and for one itteration of loop it will be  O(n) so total time complexity is O(nlogn)
        def first_num (nums,target):
            left = 0
            right = len(nums) 
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid +1
                else :
                    right = mid
            return left 
        def last_num (nums,target):
            left = 0
            right = len(nums) 
            while left< right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left= first_num(nums,target)
        right=last_num(nums,target)
        if left == right:
            return []
        
        return list(range(left,right))
        #  for this binary search the time complexity is O(nlong n + k) this one is better because of in linear search lookup time is O(n) because the loop and in binary search the lookup time is O(logn+k) because of binary search