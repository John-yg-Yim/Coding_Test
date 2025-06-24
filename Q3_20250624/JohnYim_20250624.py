class Solution:
    def __init__(self, s, Roman):
        self.s = s
        self.Roman = Roman
    
    def Roman2Integer(self):
        s = self.s
        Roman = self.Roman
        sum = 0
        pre_value = 0

        for i in range(len(s)-1, -1, -1):
            if Roman[s[i]] < pre_value:
                sum -= Roman[s[i]]
            else:
                sum += Roman[s[i]]
                pre_value = Roman[s[i]]
        
        return sum

def main():
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    s = ['III', 'LVIII', 'MCMXCIV', 'CDIV']
    sols = [Solution(i, Roman) for i in s]

    for j, sol in enumerate(sols, start=1):
        print(sol.Roman2Integer())

if __name__ == "__main__":
    main()