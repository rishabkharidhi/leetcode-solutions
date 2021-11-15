class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sml=strs[0]
        x=''
        y=''
        f=0
        for i in range(0,len(strs)):
            if len(strs[i])<len(sml):
                sml = strs[i]
        for i in range(0, len(sml)):
            x+=sml[i]
            for j in range(0,len(strs)):
                if x == (strs[j])[:len(x)]:
                    f=1
                    #print((strs[j])[:len(x)],x)
                else:
                    f=0
                    break
                #print((strs[j])[:len(x)],x)
            
            if f==1:
                y=x
            else:
                break
        return y
