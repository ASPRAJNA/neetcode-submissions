class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrom=s.replace(" ","")
        palindrom=palindrom.lower()
        punc=["'",'"',"?","!",".",",",":"]
        for x in punc:
            if x in palindrom:
                palindrom=palindrom.replace(x,"")
        if palindrom == palindrom[::-1]:
            return True 
        else:
            return False
