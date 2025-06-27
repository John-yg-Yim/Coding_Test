from collections import defaultdict

# 정수 배열 Example과 정수 target이 주어질 때 두 수를 더해 target이 되는 두 숫자의 인덱스를 반환하시오.

nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

class TwoSumSolution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def brute_force(self):
        result = []
        n = len(self.nums)
        for i in range(n):
            for j in range(i+1, n):
                if self.nums[i] + self.nums[j] == self.target:
                    result.append((i, j))
        return result
    
    def hashmap(self):
        revers_dict = defaultdict(list)
        result = []

        for i, num in enumerate(self.nums):
            temp = self.target - num
            if temp in revers_dict:
                for j in revers_dict[temp]:
                    result.append((j, i))
            revers_dict[num].append(i)
        
        return result
    
def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9
    solver1 = TwoSumSolution(nums1, target1)
    print("Brute Force:", solver1.brute_force())
    print("Hashmap: ", solver1.hashmap())

    nums2 = [3, 2, 4]
    target2 = 6
    solver2 = TwoSumSolution(nums2, target2)
    print("Brute Force:", solver2.brute_force())
    print("Hashmap: ", solver2.hashmap())

    nums3 = [3, 3]
    target3 = 6
    solver3 = TwoSumSolution(nums3, target3)
    print("Brute Force:", solver3.brute_force())
    print("Hashmap: ", solver3.hashmap())

if __name__=="__main__":
    main()
