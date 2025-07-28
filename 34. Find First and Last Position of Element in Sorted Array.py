class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first (nums,target):
            left , right = 0 , len(nums) - 1
            index = -1
            while left <= right :
                mid = (left + right) // 2
                if nums[mid] < target :
                    left = mid + 1
                elif nums[mid] > target : 
                    right = mid -1
                else:
                    index = mid
                    right = mid -1
            return index
        def find_second (nums,target):
            left , right = 0 , len(nums) - 1
            index = -1
            while left <= right :
                mid = (left + right)
                if nums [mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    index = mid
                    left = mid + 1
            return index
        return [find_first(nums,target),find_second(nums,target)]