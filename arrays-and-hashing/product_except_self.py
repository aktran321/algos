
def productExceptSelf(nums):
        prefix = 1
        postfix = 1
        length = len(nums)
        ans = [1] * length
        for i in range(length):
            ans[i] *= prefix
            prefix *= nums[i]
        
        for i in range(length -1,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
