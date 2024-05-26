import math
import functools    

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
        if len(s) != 0:
            for char in s:
                charIndex=list(s).index(char)
                charTemp =charIndex
                for c in range(charTemp,len(s)):
                    sub = str(s[charTemp:c+1])
                    if len(set(sub)) == len(sub) :
                        print(sub)
                        subs.append(sub)
                    else: break
            return max([len(sub) for sub in subs])
        return 0
    
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
        
    def reverse(self,x):
        num = x
        if num < 0:
            num = abs(num)
        
        sum = 0
        while num != 0:
            digit = num % 10
            sum = sum * 10 + digit
            num //= 10
            
        if(x < 0):
            return sum - (sum * 2)
        else:
            return sum
        
    def twoSum(self,nums,target):
        for num in nums:
            numIndex = list(nums).index(num)
            nn = nums[numIndex + 1:]
            for n in nn:
                nIndex = list(nums).index(n) 
                if n + num == target: return sorted([nIndex ,numIndex])
    
    def isValidSudoku(self,board:list):
        for row in board:
            rowIndex = board.index(row)
            
            answeredItemsRow = []
            answeredItemsBox = []
            
            for col in row:
                colIndex = list(row).index(col)
                
                if col != ".":
                    answeredItemsRow.append(col)
                
                if colIndex + 1 % 3 == 0 and rowIndex == colIndex:
                    answeredItemsBox.append(row[colIndex - 2:colIndex + 1])
                    answeredItemsBox.append(board[rowIndex - 1][colIndex - 2:colIndex + 1])
                    answeredItemsBox.append(row[rowIndex - 1][colIndex - 2:colIndex + 1])
            
            if len(list(set(answeredItemsRow))) != len(list(answeredItemsRow)): return False
            
            while "." in answeredItemsBox: answeredItemsBox.remove(".")
            if len(set(answeredItemsBox)) != len(answeredItemsBox): return False
            
        answeredItemsCol = []
        rowIndex = 0
        colIndex = 0
        while colIndex < 9:
            while rowIndex < 9:
                if board[rowIndex][colIndex] != ".":
                    answeredItemsCol.append(board[rowIndex][colIndex])
                rowIndex += 1
            colIndex += 1
                
        if len(set(answeredItemsCol)) != len(answeredItemsCol): return False
        
        return True

solution = Solution()        
print(solution.subsets([1,2,3]))
print("-------------")
print(solution.addTwoNumbers([1,2,3],[2,3,4]))
print("-------------")
print(solution.lengthOfLongestSubstring("aab"))
print("-------------")
print(solution.isPalindrome(10))
print("-------------")
print(solution.findMedianSortedArrays([1,2],[3,4]))
print("-------------")
print(solution.reverse(-121))
print("-------------")
print(solution.twoSum([3,2,4],6))
print("-------------")
print(solution.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))