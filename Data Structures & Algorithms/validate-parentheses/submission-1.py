class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        my_opens = []

        for i in range(len(s)):
            if s[i] in open:
                my_opens.append(s[i])
            elif s[i] in close:
                if len(my_opens) == 0:
                    return False
                if close.index(s[i]) != open.index(my_opens.pop()):
                    return False
        
        return len(my_opens) == 0