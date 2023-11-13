# Time:  O(nlogn)
# Space: O(n)

import collections


# sort, sliding window
class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        LIMIT_COUNT = 2
        LIMIT_MINUTE = 60
        def to_minute(x):
            return int(x[:2])*60+int(x[2:])
    
        lookup = collections.defaultdict(list)
        for x, t in access_times:
            lookup[x].append(to_minute(t))
        result = []
        for x, ts in lookup.iteritems():
            ts.sort()
            if any(ts[i]-ts[i-LIMIT_COUNT] < LIMIT_MINUTE for i in xrange(LIMIT_COUNT, len(ts))):
                result.append(x)
        return result
