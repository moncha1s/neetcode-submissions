class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        L = 0
        R = len(s) - 1
        
        while L < R:
            leftChar = s[L]
            rightChar = s[R]

            if not (leftChar.isalnum()):
                L += 1
                continue
            elif not (rightChar.isalnum()):
                R -= 1
                continue

            if leftChar == rightChar:
                L += 1
                R -= 1
                continue
            else:
                return False

        return True