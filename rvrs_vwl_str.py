"""REVERSE VOWELS OF A STRING:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede" """
class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        i=0
        j=len(l)-1
        v=['a','e','i','o','u','A','E','I','O','U']
        while(i<j):
            if l[i] in v and l[j] in v:
              #  l[i],l[j]=l[j],l[i]   Direct Swaping
               #   l[j]=l[i]
                 temp=l[i]   #using temporary variable`
                 l[i]=l[j]
                 l[j]=temp
                 i+=1
                 j-=1
            elif l[i] not in v and l[j] in v:
                i+=1
            elif l[i] in v and l[j] not in v:
                    j-=1
            else:
                i+=1
                j-=1
        return ''.join(l)    
            

