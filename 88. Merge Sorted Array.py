class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for j in range(n):
        #     nums1[m+j]=nums2[j]
        # nums1.sort() # brute force solution
        p1 = m - 1 
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0 :
            if nums1[p1] > nums2[p2] :
                nums1[p] = nums1[p1]
                p1 -= 1
            else :
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0 :
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        # that is the optimal solution because of the time complexity is O(m+n) and space complexity is O(1) because we merge in place