import math

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
    
    def lengthOfLongestSubstring(self,s):
        subs = [] 
        for char in s:
            charIndex=list(s).index(char)
            charTemp =charIndex
            for c in range(charTemp,len(s)):
                sub = str(s[charIndex:c+1])
                if(len(set(sub)) == len(sub)):
                    print(sub)
                    subs.append(sub)
                else: break
        return max([len(sub) for sub in subs])
    
    def isPalindrome(self,number):
        if number < 0: return False
        strNum=str(number)
        result = int(strNum[::-1])
        if(result == number):
            return True
        else:
            return False
        
    def findMedianSortedArrays(self,nums1,nums2):
        merged = list(nums1 + nums2)
        merged.sort()
        if len(merged) % 2 == 0: return (merged[int(len(merged) / 2)] +  merged[int(len(merged) / 2) - 1]) / 2
        else: return merged[math.floor(len(merged) / 2)]
            
solution = Solution()        
print(solution.subsets([1,2,3]))
print("-------------")
print(solution.addTwoNumbers([1,2,3],[2,3,4]))
print("-------------")
print(solution.lengthOfLongestSubstring("pwwkew"))
print("-------------")
print(solution.isPalindrome(10))
print("-------------")
print(solution.findMedianSortedArrays([1,2],[3,4]))