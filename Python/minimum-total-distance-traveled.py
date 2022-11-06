# Time:  O(mlogm + nlogn + m * n)
# Space: O(n)

import collections


# sort, dp, prefix sum, mono deque
class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort(), factory.sort()
        dp = [float("inf")]*(len(robot))  # dp[j]: min of factory[:i+1] and robot[:j]
        for i in xrange(len(factory)):
            prefix = 0
            dq = collections.deque([(0, -1)])
            new_dp = [float("inf")]*(len(robot))
            for j in xrange(len(robot)):
                prefix += abs(robot[j]-factory[i][0])
                if j-dq[-1][1] == factory[i][1]+1:
                    dq.pop()
                while dq and dq[0][0] >= dp[j]-prefix:
                    dq.popleft()
                dq.appendleft((dp[j]-prefix, j))
                new_dp[j] = dq[-1][0]+prefix
            dp = new_dp
        return dp[-1]