class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: strb
        :rtype: str
        """
        self.s = s
        vowelsInList=[]
        s = list(s)
        vowel=['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i] in vowel:
                vowelsInList.append(s[i])
        j = len(vowelsInList)
        for i in range(len(s)):
            if s[i] in vowel: 
                s[i] = vowelsInList[j-1]
                j-=1
        return ''.join(s)