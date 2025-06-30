class Solution():
    def __init__(self, nums):
        self.nums = nums

    def CheckDuplicates(self):
        nums = self.nums
        result = []
        result.append(nums[0])
        temp = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if temp == nums[i]:
                temp = nums[i]
                cnt += 1
            else:
                result.append(nums[i])
                temp = nums[i]
        
        for j in range(cnt):
            result.append('_')

        return result


def main():
    nums1 = [1,1,2]
    nums2 = [0,0,1,1,1,2,2,3,3,4]

    sol1 = Solution(nums1)
    sol2 = Solution(nums2)

    print(sol1.CheckDuplicates())
    print(sol2.CheckDuplicates())

if __name__ == "__main__":
    main()