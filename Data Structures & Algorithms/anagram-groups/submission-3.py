class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this creates a hashMap that will create an empty list when there is nothing 
        res = defaultdict(list)  

        
        for s in strs:
            # create a key list of 26 0
            count = [0] * 26

            #
            for c in s:
                # get the number of the char
                count[ord(c) - ord("a")] += 1
                # grab the key int and add 1 to count the occurance of that letter 
            # use the key to append the string to the hashmap list 
            
            res[tuple(count)].append(s)
        return list(res.values())