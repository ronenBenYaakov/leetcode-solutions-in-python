class Solution(object):
    def subarraySum(self, nums, k):
        res, dp, sum = 0, {}, 0

        for n in nums:
            sum += n

            if sum == k:
                res += 1
            
            if sum - k in dp:
                res += dp[sum - k]

            dp[sum] = dp.get(sum, 0)  + 1

        return res
