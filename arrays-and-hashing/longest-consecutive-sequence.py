def longestConsecutive(nums):
        numSet = set(nums)
        longest = 0
        seq = 0
        for i in nums:
            if (i-1) not in numSet:
                while (i+seq) in numSet:
                    seq += 1
                longest = max(longest, seq)
        return seq


import unittest

class TestLongestConsecutive(unittest.TestCase):
    def test_longestConsecutive(self):
        self.assertEqual(longestConsecutive([1,2,3,4,5]), 5)
        self.assertEqual(longestConsecutive([1,2,3,4,6]), 4)
        self.assertEqual(longestConsecutive([1,2,3,4,7]), 4)
        self.assertEqual(longestConsecutive([1,2,3,4,8]), 4)
        self.assertEqual(longestConsecutive([1,2,3,4,9]), 4)
        self.assertEqual(longestConsecutive([1,2,3,4,10]), 4)

if __name__ == '__main__':
    unittest.main()