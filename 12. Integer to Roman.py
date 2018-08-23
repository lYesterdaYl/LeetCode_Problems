class Solution:
    def romanToInt(self, num):
        """
        :type s: str
        :rtype: int
        """

        result = ""
        s = str(num)

        if len(s) == 3:
            hun = int(s[0])
            ten = int(s[1])
            inte = int(s[2])

        if len(s) == 2:
            ten = int(s[0])
            inte = int(s[1])

        if len(s) == 1:
            inte = int(s[0])

        if len(s) == 4:
            thou = int(s[0])
            hun = int(s[1])
            ten = int(s[2])
            inte = int(s[3])
            for i in range(0, thou):
                result += "M"

        if len(s) >= 3:
            if hun >= 5 and hun != 9:
                result += "D"
                for i in range(0, hun - 5):
                    result += "C"
            elif hun < 5 and hun != 4:
                for i in range(0, hun):
                    result += "C"
            elif hun == 4:
                result += "CD"
            elif hun == 9:
                result += "CM"
        if len(s) >= 2:
            if ten >= 5 and ten != 9:
                result += "L"
                for i in range(0, ten - 5):
                    result += "X"
            elif ten < 5 and ten != 4:
                for i in range(0, ten):
                    result += "X"
            elif ten == 4:
                result += "XL"
            elif ten == 9:
                result += "XC"
        if len(s) >= 1:

            if inte >= 5 and inte != 9:
                result += "V"
                for i in range(0, inte - 5):
                    result += "I"
            elif inte < 5 and inte != 4:
                for i in range(0, inte):
                    result += "I"
            elif inte == 4:
                result += "IV"
            elif inte == 9:
                result += "IX"

        return result





if __name__ == '__main__':
    a = Solution()
    s = "58"
    print(a.romanToInt(s))