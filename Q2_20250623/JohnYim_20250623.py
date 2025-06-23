class Solution:
    def __init__(self, x):
        self.x = x

    def StringCheck(self):
        x_str = str(self.x)
        return x_str == x_str[::-1]
        
    def IntegerCheck(self):
        x = self.x
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        mid = 0
        while x > mid:
            mid = mid * 10 + x % 10
            x //= 10

        return x == mid or x == mid // 10

def main():
    x = int(input("Input Integer: "))
    sol = Solution(x)

    print("String 처리 회문: ", sol.StringCheck())
    print("Integer 처리 회문: ", sol.IntegerCheck())

if __name__== "__main__":
    main()