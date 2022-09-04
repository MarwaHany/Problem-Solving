import copy
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        final_res = []
        i = 0
        try:
            while(True):
                check = set()
                for j in range(len(strs)): # ["flower","flow","flight"]
                    check.add(strs[j][i])
                if len(check) == 1:
                    final_res.append(check.pop())
                    i += 1
                else:
                    break;
        except:
            pass
        final_res = list(final_res)
        res_str = ""
        for k in final_res:
            res_str += k
        return res_str