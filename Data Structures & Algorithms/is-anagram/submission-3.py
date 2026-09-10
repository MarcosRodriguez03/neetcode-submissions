class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False

        # create freq table 
        # if !seen a character add it 
        # if seen a character  + 1

        freqS = {}
        freqT = {}
        for i in range(len(s)):
            if s[i] not in freqS:
                freqS[s[i]] = 1; 
            else:
                freqS[s[i]] += 1;

            if t[i] not in freqT:
                freqT[t[i]] = 1;
            else:
                freqT[t[i]] += 1; 

        return freqS == freqT
            