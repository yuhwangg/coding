class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 这道题的本质相当于在一列数组中取出一个或多个不相邻数，使其和最大. 
        # 对于这类求极值的问题首先考虑动态规划Dynamic Programming来解，我们维护一个一位数组dp，
        # 其中dp[i]表示到i位置时不相邻数能形成的最大和，那么递推公式怎么写呢，我们先拿一个简单的例子来分析一下，
        # 比如说nums为{3, 2, 1, 5}， 那么我们来看我们的dp数组应该是什么样的，首先dp[0]=3没啥疑问，再看dp[1]是多少呢，
        # 由于3比2大，所以我们抢第一个房子的3，当前房子的2不抢，所以dp[1]=3，那么再来看dp[2]，由于不能抢相邻的，
        # 所以我们可以用再前面的一个的dp值加上当前的房间值，和当前房间的前面一个dp值比较，取较大值当做当前dp值，所以
        # 可以得到递推公式dp[i] = max(num[i] + dp[i-2], dp[i-1]), 由此看出需要初始化dp[0]和dp[1]，其中dp[0]即为num[0]，
        # dp[1]此时应该为max(num[0], num[1])
        
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        n = len(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]
        
        
        
