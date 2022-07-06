class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        @ashot-gimishyan
        06.07.2022
        """

        i = 1
        prev = ""
        count = 0
        while True:
            if i == len(strs[0]) + 1:
                return prev
            tmp = strs[0][:i]
            for word in strs:
                if word.startswith(tmp):
                    count += 1
                    continue
            if count % len(strs) == 0:
                i += 1
                prev = tmp
                count = 0
                continue
            return prev



'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
     
