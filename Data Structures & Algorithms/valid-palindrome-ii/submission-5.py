class Solution:
    def validPalindrome(self, s: str) -> bool:
        #just count num of items that arent equal
        errorCount = 0
        s = s.replace(" ", "")
        L = 0
        R = len(s) - 1
    
        #given the bounds of this check if its the same
        def resolveMismatch(L: int, R: int):
            #check, is s - L a palinfrome OR is s - R a palindrome, 
            # if either is true we can return true
            skipLeft = s[L+1:R+1]
            skipRight = s[L:R]
            return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]


        while L <= R:
            lC = s[L]
            rC = s[R]

            if lC != rC:
                return resolveMismatch(L, R)          
            L += 1
            R -= 1

                
        return True