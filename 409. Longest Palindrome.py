class Solution:
    def longestPalindrome(self, s: str) -> int:
        HashMap = {}
        result = 0
        for c in s:
            HashMap[c] = HashMap.get(c,0) + 1
        for i in HashMap.keys():
            result = result + (HashMap[i]//2) * 2
            if result % 2 == 0 and HashMap[i] % 2 == 1:
                result = result + 1
        return result
                
            # ..
        
            
        