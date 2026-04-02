from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(lambda: [])
        for word in strs:
            anagram_hash[str(sorted(word))].append(word)
        
        return [val for val in anagram_hash.values()]