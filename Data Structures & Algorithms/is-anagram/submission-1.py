class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I will use a frequency table to keep track of each letter 
        # and the # of occurances of each letter

        lengthS = len(s);
        lengthT = len(t);
        if lengthS != lengthT:
            return False

        freqS = {};
        freqT = {};


        for letter in s:
            if letter in freqS:
                freqS[letter] += 1
            else:
                freqS[letter] = 1
        
        for letter in t:
            if letter in freqT:
                freqT[letter] += 1
            else: 
                freqT[letter] = 1
        
        print(freqT)
        print(freqS)

        for letter in freqS:
            if  letter not in freqT:
                return False
            if freqS[letter] != freqT[letter]:
                return False
        return True
        