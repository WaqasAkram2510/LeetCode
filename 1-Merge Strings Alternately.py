class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        word1_len= len(word1)
        word2_len = len(word2)
        i = min(word1_len,word2_len)
        j=0
        while j<i:
            output = output + word1[j] + word2[j]
            j+=1
        output = output + word1[i:] + word2[i:]
        return output