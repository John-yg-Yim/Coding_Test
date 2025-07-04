class Solution():
    def __init__(self, s):
        self.s = s
    
    def LengthLastWorld(self):
        s = self.s
        return len(s.strip().split()[-1])

def main():
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"

    sol1 = Solution(s1)
    sol2 = Solution(s2)
    sol3 = Solution(s3)

    print(sol1.LengthLastWorld())
    print(sol2.LengthLastWorld())
    print(sol3.LengthLastWorld())

if __name__ == "__main__":
    main()