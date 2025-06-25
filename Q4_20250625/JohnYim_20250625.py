class Solution():
    def __init__(self, strs):
        self.strs = strs
    
    def Common_Prefix(self):
        temp = []
        result = ""
        strs = self.strs

        # 각 단어별 요소 추출 후 리스트로 저장.
        for char in zip(*strs):
            temp.append(char)
        
        # set함수: 중복제거
        # set함수의 길이가 1인 경우 모두 동일.
        for i in range(len(temp)):
            if len(set(temp[i])) == 1:
                result += temp[i][0]

            if result == "":
                result = "There is no Common Prefix"
                
        return result

def main():
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]

    sol1 = Solution(strs1)
    sol2 = Solution(strs2)

    print(sol1.Common_Prefix())
    print(sol2.Common_Prefix())

if __name__ == "__main__":
    main()