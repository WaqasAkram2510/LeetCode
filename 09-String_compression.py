class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        output=[]
        count = 1
        if len(chars)==1:
            return 1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count +=1
            else:
                output.append(chars[i])
                if count!=1:
                    output+=(list(str(count)))
                count=1
        output.append(chars[-1])
        if count!=1:
                    output+=(list(str(count)))
        for i in range(len(output)):
            chars[i] = output[i]
        return len(output)