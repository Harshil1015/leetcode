    class Solution:
        def countHillValley(self, nums: List[int]) -> int:
            count = 0
            # first of all we need to remove all the duplicate element
            nums1= [nums[0]]
            for num in nums[1:]:
                if num != nums1[-1]:
                    nums1.append(num)

            for i in range(1,len(nums1)-1):
                if nums1[i] > nums1[i-1] and  nums1[i] > nums1[i+1] :
                    count += 1  # hill
                elif nums1[i] < nums1[i-1] and nums1[i] < nums1[i+1] :
                    count += 1 #valley
            return count