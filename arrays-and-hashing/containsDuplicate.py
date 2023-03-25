def duplicate(nums):
  hashset = set()
  for i in nums:
    if i in hashset:
      return True
    else:
      hashset.add(i)
  return False


import unittest

class TestDuplicate(unittest.TestCase):
    def test_duplicate_true(self):
        nums = [1,2,3,4,4]
        self.assertTrue(duplicate(nums))

    def test_duplicate_false(self):
        nums = [1,2,3,4]
        self.assertFalse(duplicate(nums))

if __name__ == '__main__':
    unittest.main()