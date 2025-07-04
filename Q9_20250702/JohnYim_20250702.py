class Solution():
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle
    
    def FindFirstOccurrence(self):
        haystack = self.haystack
        needle = self.needle

        return haystack.find(needle)

def main():
    haystack1, needle1 = "sadbutsad", "sad"
    haystack2, needle2 = "leetcode", "leeto"

    sol1 = Solution(haystack1, needle1)
    sol2 = Solution(haystack2, needle2)

    print(sol1.FindFirstOccurrence())
    print(sol2.FindFirstOccurrence())

if __name__ == "__main__":
    main()