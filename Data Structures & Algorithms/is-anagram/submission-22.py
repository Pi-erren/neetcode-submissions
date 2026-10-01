class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                freq_s[s[i]] = freq_s.get(s[i], 0) + 1
                freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        return freq_s == freq_t

