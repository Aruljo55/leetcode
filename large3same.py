class Solution:
    def largestGoodInteger(self, num):
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                cur = num[i:i + 3]
                if cur > ans:
                    ans = cur
        return ans
