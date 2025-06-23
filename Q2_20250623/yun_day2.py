class Solution:
    def __init__(self, x):
        self.x = x

    def yun(self):
        x=self.x
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False



    def yun2(self):
        x = self.x
        # 음수는 회문이 될 수 없다고 가정
        if x < 0:
            return False

        original = x
        reversed_num = 0
        # 1의 자리부터 차례로 꺼내서 뒤집은 수를 만듭니다
        while x != 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return reversed_num == original
    
def main():
    x =int(input('숫자를 입력하세요'))
    sol = Solution(x)

    print("String 처리 회문: ", sol.yun())
    print("Integer 처리 회문: ", sol.yun2())

if __name__== "__main__":
    main()
