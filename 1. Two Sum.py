class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        other = "a"
        for i, j in enumerate(nums):
            temp = j
            nums[i] = 'a'
            if(temp == other and len(result) < 2):
                result.append(i)
            if(target - temp in nums):
                result.append(i)
                other = target - temp
        return result


if __name__ == '__main__':
    a = Solution()
    s = [3,3]
    print(a.twoSum(s, 6))