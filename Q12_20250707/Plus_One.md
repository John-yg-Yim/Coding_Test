# Q66 - Plus One (플러스 원)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #66](https://leetcode.com/problems/plus-one/) | **출처:** LeetCode 문제 66번

---

## 📘 Problem Description (문제 설명)

You are given a large integer represented as an integer array `digits`,  
where each `digits[i]` is the `i`th digit of the integer.  
→ 큰 정수가 **배열 `digits`**로 주어집니다.  
→ `digits[i]`는 정수의 `i`번째 자리수를 의미합니다 (가장 큰 자리수부터 순서대로).

Increment the large integer by one and return the resulting array of digits.  
→ 이 정수에 **1을 더한 결과를 배열 형태로 반환**하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `digits = [1,2,3]`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `[1,2,4]`  
**Explanation:** `123 + 1 = 124` → `[1,2,4]`

</details>

---

### Example 2

**Input:** `digits = [4,3,2,1]`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[4,3,2,2]`  
**Explanation:** `4321 + 1 = 4322`

</details>

---

### Example 3

**Input:** `digits = [9]`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[1,0]`  
**Explanation:** `9 + 1 = 10` → `[1,0]`

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits`에는 **선행 0이 없음**

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 마지막 자리부터 1을 더하며 올라가세요 (올림(carry) 처리).
- 만약 모든 자리수가 9였다면 배열의 크기가 1 늘어납니다.
- 파이썬의 문자열/정수 변환 없이 자리수 연산으로 해결해보세요.

</details>