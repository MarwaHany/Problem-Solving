class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complementry = {
          "{":"}",
          "(":")",
          "[":"]",
        }
        if len(s)%2 != 0:
            return False
        for char in s:
            if char in complementry.keys():
                stack.append(complementry[char])
            elif not len(stack):
                return False
            elif char != stack.pop():
                return False
        return len(stack) == 0
        