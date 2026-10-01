class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in freq_s: freq_s[s[i]] = 1
                else: freq_s[s[i]] += 1
                if t[i] not in freq_t: freq_t[t[i]] = 1
                else: freq_t[t[i]] += 1
        
        for freq in freq_s:
            if freq not in freq_t: return False
            if freq_s[freq] != freq_t[freq]: return False
        return True

