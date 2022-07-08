class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a = '('
        b = ')'
        c = '['
        d = ']'
        e = '{'
        f = '}'

        opens = [a,c,e]
        closes = [b,d,f]

        a_count = 0
        b_count = 0
        c_count = 0
        d_count = 0
        e_count = 0
        f_count = 0

        lst = list()
        for i in s:
            if i in opens:
                lst.append(i)

            if i in closes:
                if len(lst) == 0:
                    return False
                num = lst.pop()
                if num == a and i != b:
                    return False
                if num == c and i != d:
                    return False
                if num == e and i != f:
                    return False
        if len(lst) != 0:
            return False

        return True



'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''
