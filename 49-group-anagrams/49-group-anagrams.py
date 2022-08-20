from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        char_count_dict = defaultdict(list) 
        for word in strs:
            count= [0] * 27
            for char in word:
                try:
                    count[ord(char) - ord("a")] += 1
                except:
                    count[26] += 1
                    
            char_count_dict[tuple(count)].append(word)
        return char_count_dict.values()
        