from collections import defaultdict

# we can use the frequency map as the key to the 
# hash table. this only works because we know the
# problem constrains the strs to be only of a-z
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            anagram_hash[str(sorted(word))].append(word)
        
        return list(anagram_hash.values())