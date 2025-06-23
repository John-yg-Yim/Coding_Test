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
        x=self.x
        is_palindrome = True                 
        for i in range(len(x) // 2):     
            if x[i] != x[-1 - i]:      
                is_palindrome = False        
                break
        
        return is_palindrome
    
def main():
    x =int(input(''))
    sol = Solution(x)

    print("String 처리 회문: ", sol.yun())
    print("Integer 처리 회문: ", sol.yun2())

if __name__== "__main__":
    main()
