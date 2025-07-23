#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1
#         while left <= right:
#             mid = (left+right) // 2
#             if target > nums[mid] :
#                 left = mid+1
#             elif target < nums[mid]:
#                 right = mid-1
#             else:
#                 return mid
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(nums,low,high,target):
            if low > high:
                return -1
            mid = (low+high) // 2
            if nums[mid] == target:
                    return mid
            elif target > nums[mid] :
                return search(nums,mid+1,high,target)
            elif target < nums[mid] :
                return search(nums,low,mid-1,target)	
        return search(nums,0,len(nums)-1,target)