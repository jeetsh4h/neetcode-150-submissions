class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # should use Counter for this
        count_s: dict[str, int] = {}
        for c in s:
            if count_s.get(c) == None:
                count_s[c] = 1
            else:
                count_s[c] += 1
        
        # should use Counter for this
        count_t: dict[str, int] = {}
        for c in t:
            if count_t.get(c) == None:
                count_t[c] = 1
            else:
                count_t[c] += 1
        
        # python now puts the key values in
        # a deterministic order, can just use `==`
        for key, value in count_s.items():
            if key in count_t.keys():
                if value == count_t[key]:
                    continue
                else:
                    return False
            else:
                return False
        
        return True
