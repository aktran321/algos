def hammingWeight(n):
  res = 0
  while n:
    if n & 1:
      res += 1
      n = n >> 1
  return res