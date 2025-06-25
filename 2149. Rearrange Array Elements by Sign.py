# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         positive=[]
#         negative=[]
#         for num in nums:
#             if num>0:
#                 positive.append(num)
#             else:
#                 negative.append(num)
#         print(positive , negative)
#         new_list=[]
#         for i in range(len(positive)):
#             new_list.append(positive[i])
#             new_list.append(negative[i])
#         return new_list
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pnumber=0
        nnumber=1
        answer=[0]*len(nums)
        for num in nums:
            if num>0:
                answer[pnumber]=num
                pnumber+=2
            else:
                answer[nnumber]=num
                nnumber+=2
        return answer