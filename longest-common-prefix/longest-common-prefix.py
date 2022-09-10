class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any([not(s) for s in strs]):
            return ""
        common = ""
        i = 0
        while(i<201):
            try:
                char = strs[0][i]
                if all([char == s[i] for s in strs]):
                    common += strs[0][i]
                else:
                    break
                i += 1
            except Exception as e:
                break
        return common
        
            
        