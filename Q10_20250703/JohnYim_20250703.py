class Solution:
    def __init__(self, nums):
        self.nums = nums

    def BinarySearch(self, target, left=0, right=None):
        nums = self.nums

        if right is None:
            right = len(nums) - 1

        if left > right:
            return left

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.BinarySearch(target, mid + 1, right)
        else:
            return self.BinarySearch(target, left, mid - 1)

def main():
    nums = [1, 3, 5, 6]
    targets = [5, 2, 7]

    sol = Solution(nums)

    for t in targets:
        result = sol.BinarySearch(t)
        print(result)

if __name__ == "__main__":
    main()