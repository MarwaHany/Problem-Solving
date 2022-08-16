class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hashMap = defaultdict(int)
        t_hashMap = defaultdict(int)
        if len(s) == len(t):
            for i in range(len(s)):
                s_hashMap[s[i]] += 1
                t_hashMap[t[i]] += 1
            if s_hashMap == t_hashMap:
                return True
            return False