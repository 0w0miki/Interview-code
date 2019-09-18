#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[0 for i in range(l)] for j in range(l)]
        res = (0, 0, 0)
        for j in range(l):
            for i in range(j+1):
                dp[i][j] = s[i]==s[j] and (j-i < 2 or dp[i+1][j-1])
                if dp[i][j] and j-i > res[2]:
                    res = (i,j,j-i+1)
        return s[res[0]:res[1]+1]

