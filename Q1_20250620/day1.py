class Solution(object):
    def twoSum(self, nums, target):        
        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                if nums[i] + nums[l] ==target:
                    # print([i,l])
                    return [i, l]

nums = [3,2,3,1,2,3,25,23,5325,23]
target = 26

result = Solution().twoSum(nums, target)

print(f'result: {result}')