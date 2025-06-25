# Q14 - Longest Common Prefix (가장 긴 공통 접두사)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #14](https://leetcode.com/problems/longest-common-prefix/) | **출처:** LeetCode 문제 14번

---

## 📘 Problem Description (문제 설명)

Write a function to find the **longest common prefix string** amongst an array of strings.  
→ 문자열 배열이 주어졌을 때, 이들 사이에서 **가장 긴 공통 접두사**를 찾아 반환하세요.

If there is no common prefix, return an empty string `""`.  
→ 공통 접두사가 없다면, 빈 문자열 `""`을 반환하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `strs = ["flower","flow","flight"]`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `"fl"`  
**Explanation:** 모든 문자열에서 `"fl"`로 시작하므로 공통 접두사는 `"fl"`입니다.

</details>

---

### Example 2

**Input:** `strs = ["dog","racecar","car"]`

<details>
<summary>✅ Output 보기</summary>

**Output:** `""`  
**Explanation:** 세 문자열 간 공통 접두사가 없습니다.

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= strs.length <= 200`  
- `0 <= strs[i].length <= 200`  
- `strs[i]`는 비어 있지 않다면, 오직 소문자 알파벳(a~z)으로만 구성됩니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 공통 접두사를 찾는 가장 간단한 방법은 첫 번째 문자열을 기준으로 **다른 모든 문자열과 비교**하는 것입니다.
- 접두사가 더 이상 매칭되지 않으면 바로 잘라냅니다.
- Python의 `zip()` 함수로 문자의 열(column) 단위 비교도 가능합니다.

</details>