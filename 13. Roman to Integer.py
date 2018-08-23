class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        jump = -1
        for i, j in enumerate(s):
            if(jump != i):
                if(i + 1 < len(s)):
                    if(number[s[i]] - number[s[i+1]] < 0):
                        result += abs(number[s[i]] - number[s[i+1]])
                        jump = i + 1
                    else:
                        result += number[j]
                else:
                    result += number[j]
        return result

if __name__ == '__main__':
    a = Solution()
    s = "LVIII"
    print(a.romanToInt(s))