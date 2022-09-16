class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [0 for char in s]
        c_position = -len(s)
        for i in range(len(s)):
            if s[i] == c:
                c_position = i
            answer[i] = i - c_position
        for i in list(reversed(range(len(s)))):
            if s[i] == c:
                c_position = i
            answer[i] = min(answer[i], abs(i-c_position))
        return answer
            
                
            
                
        