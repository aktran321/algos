def topfreqeunt(nums, k):
    #[1,1,1,2,3,3]
    # k = 2
    # ans = [1,3]
    ans = []
    count = {}
    freqMap = [ [] for i in range(len(nums) + 1)]
    for i in nums:
        count[i] = count.get(i,0) + 1
    for v,f in count.items():
        # [ [], [2], [3], [1], [], [], [] ]
        # count = {1:3, 2:1, 3:2}
        freqMap[f].append(v)
    # now, lets loop through freqMap backwards and enter in values until length of ans = k
    for i in range(len(freqMap)-1, 0, -1):
        for n in freqMap[i]:
            ans.append(n)
        if len(ans) == k:      
            return ans  
        
import unittest

class TestTopFrequent(unittest.TestCase):
    def test_topfreqeunt(self):
        self.assertEqual(topfreqeunt([1,1,1,2,3,3], 2), [1,3])

if __name__ == '__main__':
    unittest.main()