class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dictionary to store the unique key value pairs (keys - letter count) (values - list of anagrams)
        res = defaultdict(list)
        
        # Loop over each string in the list given
        for s in strs:
            # when you reach a new word create a counting hash table that keeps track of letter frequencies
            count = [0]*26

            # We loop over each character in the string and store the values in count unique for that word
            for c in s:
                
                # maps 0 to "a" and letters ahead are 1 2 3...
                # increments the value as per c in the hashmap
                count[ord(c)-ord("a")]+=1

            # append the string for each unique letter frequency for the input list
            res[tuple(count)].append(s)

        return list(res.values())



