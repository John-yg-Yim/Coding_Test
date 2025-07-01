class Solution():
    def __init__(self, nums, val):
        self.nums = nums
        self.val = val
    
    def RemoveElement(self):
        nums = self.nums
        val = self.val
        dup_cnt = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == val:
                dup_cnt += 1
            else:
                cnt += 1
        
        for j in range(dup_cnt):
            nums.remove(val)
            nums.append('_')
        
        return cnt, nums

def main():
    nums1, val1 = [3,2,2,3], 3
    nums2, val2 = [0,1,2,2,3,0,4,2], 2

    sol1 = Solution(nums1, val1)
    sol2 = Solution(nums2, val2)

    k1, result1 = sol1.RemoveElement()
    k2, result2 = sol2.RemoveElement()

    print(f"Example 1: k = {k1}, nums = {result1}")
    print(f"Example 1: k = {k2}, nums = {result2}")

if __name__ == "__main__":
    main()