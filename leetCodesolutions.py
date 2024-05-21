import functools as func

class Solution:
    
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [item + [num] for item in result]
        return result
    
    def addTwoNumbers(self,l1,l2):
        biggestDigit = 10 ** (len(l1) - 1)
        n1 = 0
        for n in reversed(l1):
            n1 += n * biggestDigit
            biggestDigit /= 10
            
        biggestDigit = 10 ** (len(l2) - 1)
        n2 = 0
        for n in reversed(l2):
            n2 += n * biggestDigit
            biggestDigit /= 10
            
        result = int(n1 + n2)
        return [num for num in str(result)]
        
print(Solution().addTwoNumbers([1,2,3],[2,3,4]))
print(Solution().subsets([1,2,3]))