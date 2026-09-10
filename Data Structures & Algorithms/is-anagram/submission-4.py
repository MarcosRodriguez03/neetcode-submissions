class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        hashMap2 = {}

        for letter in s:
            hashMap[letter] = hashMap.get(letter, 0) + 1
        for letter in t:
            hashMap2[letter] = hashMap2.get(letter, 0) + 1
        
        return hashMap == hashMap2;
            
            
        
