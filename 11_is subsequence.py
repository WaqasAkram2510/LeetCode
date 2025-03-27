class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype:  bool 
        """
        s_i=0
        if s=='':
            return True
        for i in range(len(t)):
            if s_i<len(s):
               if s[s_i]==t[i]:
                   s_i+=1
        return s_i == len(s)