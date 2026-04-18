def longestCommonPrefix(self, strs):
        strs.sort()
        n = len(strs)
        prefix = strs[0]
        for i in range(n):
            while(not strs[i].startswith(prefix)):
                prefix = prefix[:-1]

                if(prefix is ""):
                    return ""
        return prefix
