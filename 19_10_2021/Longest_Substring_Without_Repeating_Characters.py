# Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Tags: Facebook, Google, Microsoft, Amazon



# Idea:
# Sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_char  = len(s)
        length    = 0
        char_hash = {} # Stores the current index + 1 of the character, associate line 18, 21

        start = 0
        for end in range(num_char):
            if s[end] in char_hash: # Exist before
                start = max(char_hash[s[end]], start) # Jump to the stored index
            
            length = max(length, end - start + 1) 
            char_hash[s[end]] = end + 1
        
        return length