# Q9 - Palindrome Number (팰린드롬 숫자)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #9](https://leetcode.com/problems/palindrome-number/) | **출처:** LeetCode 문제 9번

---

## 📘 Problem Description (문제 설명)

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.  
→ 정수 `x`가 주어졌을 때, `x`가 **팰린드롬(앞에서부터 읽으나 뒤에서부터 읽으나 같은 수)**이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `x = 121`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `true`  
**Explanation:** 121 reads the same from left to right and from right to left.  
→ 121은 앞에서 읽든 뒤에서 읽든 동일하므로 팰린드롬입니다.

</details>

---

### Example 2

**Input:** `x = -121`

<details>
<summary>✅ Output 보기</summary>

**Output:** `false`  
→ 왼쪽에서 읽으면 `-121`, 오른쪽에서 읽으면 `121-`로 달라지므로 팰린드롬이 아닙니다.

</details>

---

### Example 3

**Input:** `x = 10`

<details>
<summary>✅ Output 보기</summary>

**Output:** `false`  
→ 오른쪽에서 읽으면 `01`이 되어 다르므로 팰린드롬이 아닙니다.

</details>

---

## 📌 Constraints (제약 조건)

- `-2³¹ <= x <= 2³¹ - 1`

---

## 🔍 Follow-up (심화 질문)

Could you solve it **without converting the integer to a string**?  
→ 정수를 **문자열로 변환하지 않고** 해결할 수 있나요?

---

<details>
<summary>💡 Hint (힌트 보기)</summary>

- You can reverse half of the number and compare it with the other half.  
→ 숫자의 절반을 뒤집어서 나머지 절반과 비교하는 방식이 가능합니다.

- Negative numbers and numbers ending in 0 (except 0 itself) can't be palindromes.  
→ 음수나 0으로 끝나는 수(0 자체 제외)는 팰린드롬이 될 수 없습니다.

</details>