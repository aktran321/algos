def twoSum(numbers, target):
    length = len(numbers)
    right = length - 1
    left = 0
    for i in range(length):
      sum = numbers[left] + numbers[right]
      if sum == target:
        return [left + 1, right + 1]
      elif sum > target:
        right -= 1
      elif sum < target:
        left += 1
        return None