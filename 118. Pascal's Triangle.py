class Solution(object):
    def generate(self, numRows):
        def ncr(n,r):
            result=1
            for i in range(r):
                result=result*(n-i)//(i+1)
            return result
        answer=[]
        for n in range(numRows):
            row=[]
            for r in range(n+1):
                row.append(ncr(n,r))
            answer.append(row)
        return answer