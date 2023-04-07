def countBits(n):
  ans = [0] * (n+1)
  for i,v in enumerate(ans):
    bitCount = 0
    bitInt = i
    while bitInt:
      if bitInt & 1:
        bitCount += 1
        bitInt = bitInt >> 1
        ans[i] = bitCount
  return ans
