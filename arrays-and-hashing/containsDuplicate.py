# Given an integer array "nums", return true if any value appears twice, false if every element is distinct
nums = [1,2,3,4]
def duplicate(nums):
  #brute force is pick a number, check all other numbers, keep looping until you reach the end or
  # you find a match... O(n^2) time

  # or make a hash table... 
  hashset = set()
  length = len(nums)
  for i in nums:
    if i in hashset:
      return True
    else:
      hashset.add(nums[i])
  return False