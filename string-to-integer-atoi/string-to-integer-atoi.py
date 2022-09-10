class Solution:       
    def myAtoi(self, s: str) -> int:
        integer_map = {f'{i}': i for i in range(10)}
        if len(s.replace(" ", "")) == 0 or (len(s) == 1 and s[0] == '-'): return 0
        s = s[s.index(s.replace(" ", "")[0]):]
        neg = True if s[0] == '-' else False
        if neg:
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        num_len = 0
        try:
            while integer_map.get(s[num_len]) is not None:
                num_len+=1
        except:
            pass
        num_len-=1
        j = 0
        res = 0
        while num_len >= 0 :
            res += integer_map.get(s[j])*10**num_len
            num_len-=1
            j+=1
        if neg and (-1* res < -1*2**31): 
            return -1*2**31
        elif not neg and res > 2**31 - 1:
            return 2**31 - 1
        return res if not neg else -1*res

            
                
        