#from collections import Counter


#def find_all_anagrams(s, p):
 #   result = []
  #  p_count = Counter(p)
   # s_count = Counter()

    #for i, char in enumerate(s):
     #   s_count[char] += 1

      #  if i >= len(p):
       #     left_char = s[i - len(p)]
        #    s_count[left_char] -= 1
         #   if s_count[left_char] == 0:
          #      del s_count[left_char]

      #  if s_count == p_count:
       #     result.append(i - len(p) + 1)
#
 #   return result


from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return [ ]
        hs=[0]*26
        hp=[0]*26
        res=[]
        k=len(p)
        for i in range(k):
            hs[ord(s[i])-97]+=1
            hp[ord(p[i])-97]+=1
        if hs==hp:res.append(0)
        for i in range(k,len(s)):
            hs[ord(s[i-k])-97]-=1
            hs[ord(s[i])-97]+=1
            if hs==hp:
                res.append(i-k+1)
        return res