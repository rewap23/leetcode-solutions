class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # O(n) time
        # O(n) space
        # create string we are going to output
        result = ""
        # find the minimum between the two words so we know the shorter and longer words
        min_len = min(len(word1), len(word2))
        # for each letter in the shortest word, append alternatively between word1 and word2
        for letter in range(min_len):
            result += word1[letter] + word2[letter]
        # now if one word is longer than the other append the rest of the longer one to the result
        if len(word2) > len(word1):
            result += word2[min_len:] # add the elements after the minimum length
        else:
            result += word1[min_len:] # add the elements after the minimum length

        return result 


