def threeSum(nums):
        length = len(nums)
        ans = []
        nums.sort()
        prev = None
        for i in range(length-2):
            a = nums[i]
            if a > 0:
                break
            elif a == prev:
                continue
            elif a <= 0:
                prev = nums[i]
                left = i+1
                right = length - 1
                while (right > left):
                    b = nums[left]
                    c = nums[right]
                    sum = a + b + c
                    if sum > 0:
                        right -= 1
                    elif sum < 0:
                        left += 1
                    elif sum == 0:
                        combo = [a,b,c]
                        if combo not in ans:
                            ans.append([a,b,c])
                        left += 1
        return ans