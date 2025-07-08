    from collections import Counter

class Solution:
    def mostFrequentEven(self, nums):
        counter = Counter(nums)
        ans = []
        max_freq = 0
        
        # Find max frequency among even numbers
        for num, count in counter.items():
            if num % 2 == 0:
                if count > max_freq:
                    max_freq = count
                    ans = [num]  # start fresh
                elif count == max_freq:
                    ans.append(num)
        
        if not ans:  # no even numbers
            return -1
        
        return min(ans)  # return smallest even with max frequency
