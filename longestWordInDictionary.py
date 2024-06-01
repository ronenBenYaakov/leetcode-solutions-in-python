class Solution(object):
    def findLongestWord(self, s, dictionary):
        dp, mx = {}, 0

        for w in dictionary:
            pw, ps, n, m = 0, 0, len(w), len(s)

            while ps < m and pw < n:
                if s[ps] == w[pw]:
                    pw += 1
                ps += 1

            if pw == n:
                dp[n] = dp.get(n, []) + [w]
                mx = max(n, mx)

        if mx == 0:
            return ""
        
        dp[mx].sort()

        return dp[mx][0]
