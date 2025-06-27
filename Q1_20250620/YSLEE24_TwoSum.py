
def some_function(num):
    return 1+1 



class Person():
    def __init__(self, name, major):
        self.name = name
        self.major = major

        
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    # print([i, j])
                    return [i, j]


    def some_function(self, num):
        self.twoSum()



# Example 1:
nums = [2,7,11,15]
target = 9

person_object = Person('yeongseo_lee', 'major')

print(f'name: {person_object.name}')
print(f'major: {person_object.major}')

# Example 2:
nums = [3,2,4]
target = 6

result = person_object.twoSum(nums, target)

print(f'result: {result}')

# # Example 3:
# nums = [3,3]
# target = 6
