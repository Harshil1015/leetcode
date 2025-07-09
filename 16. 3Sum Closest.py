class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float("inf")

        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            while j < k :
                current_sum = nums[i] + nums[j] + nums[k]
                
                if abs (target - current_sum ) < abs(target - closest_sum) :
                    closest_sum = current_sum
                
                if current_sum < target :
                    j+=1
                elif current_sum > target:
                    k-=1
                else:
                    return target
        return closest_sum