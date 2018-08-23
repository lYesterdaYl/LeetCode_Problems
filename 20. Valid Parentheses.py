class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        dict = {')': '(', ']': '[', '}': '{'}
        for i in s:

            if i in dict.values():
                result.append(i)
                print(len(result))
            elif i in dict.keys() and dict[i] in result:
                if result[len(result) - 1] == dict[i]:
                    del result[len(result) - 1]
            else:
                return False
        return result == []



if __name__ == '__main__':
    a = Solution()
    s = "]"
    print(a.isValid(s))