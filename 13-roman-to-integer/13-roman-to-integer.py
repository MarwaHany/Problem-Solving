class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapper = {
          "I": 1, 
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100, 
          "D": 500,
          "M": 1000
        }
        int_equ = 0
        for i in range(len(s)):
            if i > 0 and roman_mapper[s[i]] > roman_mapper[s[i-1]]:
                int_equ += (-2*roman_mapper[s[i-1]]) + roman_mapper[s[i]]
            else:
                int_equ += roman_mapper[s[i]]
        return int_equ    
        