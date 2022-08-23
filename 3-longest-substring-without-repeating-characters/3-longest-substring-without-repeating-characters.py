class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        visited_chars = dict()
        str_list = []
        start = end = 0
        max_window_size = 0
        while start < len(s):
            # check if char is already visited 
            while visited_chars.get(s[start]):
                to_remove = str_list.pop(0)
                del visited_chars[to_remove]
                end += 1
            visited_chars[s[start]] = 1
            str_list.append(s[start])
            max_window_size = max(max_window_size, start - end + 1)
            start += 1
        return max_window_size