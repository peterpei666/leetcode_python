from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        v = ['a', 'e', 'i', 'o', 'u']

        def vowel(s: str) -> str:
            s1 = ''
            for c in s:
                if c in v:
                    s1 += '*'
                else:
                    s1 += c
            return s1
        
        mp = dict()
        for s in wordlist:
            mp[s + '#'] = s
            s1 = s.lower()
            if not s1 in mp:
                mp[s1] = s
            s2 = vowel(s1)
            if not s2 in mp:
                mp[s2] = s
        ans = []
        for q in queries:
            if q + '#' in mp:
                ans.append(q)
                continue
            s1 = q.lower()
            if s1 in mp:
                ans.append(mp[s1])
                continue
            s2 = vowel(s1)
            if s2 in mp:
                ans.append(mp[s2])
                continue
            ans.append('')
        return ans
