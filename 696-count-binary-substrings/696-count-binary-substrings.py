class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 00110011
        prev_block_count = 0
        current_block_count = 1
        binary_count = 0
        prev = s[0]
        for i in range(1,len(s)):
            if s[i] == prev:
                current_block_count += 1
            else:
                binary_count += min(prev_block_count, current_block_count)
                prev_block_count, current_block_count = current_block_count, 1
            prev = s[i]
        binary_count += min(prev_block_count,current_block_count)
        return binary_count
        
            
                
            
                
                
                
            