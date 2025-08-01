class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix= "" # Initialize the prefix as an empty string

        for i in range(len(strs[0])): # Iterate through each character index
            for s in strs: # Check each string in the list
                if i == len(s) or s[i] != strs[0][i]: # If the character at index i is not the same in any string
                    return prefix # If mismatch found, return the prefix
            prefix += strs[0][i] # If all strings have the same character at index i, add it to the prefix

        return prefix