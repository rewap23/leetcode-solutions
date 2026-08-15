class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for idx in range(len(strs[0])):
            char = strs[0][idx]
             # check this character position against all other strings
            for string in strs[1:]:
                if idx == len(string) or string[idx] != char:
                    return strs[0][:idx]

        return strs[0]
        

        

        