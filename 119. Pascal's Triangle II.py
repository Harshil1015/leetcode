class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def ncr(n,r):
                result=1
                for i in range(r):
                  result=result*(n-i)//(i+1) 
                return result
        answer = []
        for r in range(rowIndex+1):
            answer.append(ncr(rowIndex,r))
        return answer