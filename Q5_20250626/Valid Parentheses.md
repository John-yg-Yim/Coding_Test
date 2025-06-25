# Q20 - Valid Parentheses (유효한 괄호)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #20](https://leetcode.com/problems/valid-parentheses/) | **출처:** LeetCode 문제 20번

---

## 📘 Problem Description (문제 설명)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.  
→ `s` 문자열이 괄호 문자들로만 이루어져 있을 때, 이 문자열이 **올바른 괄호 문자열인지** 판단하세요.

A string is valid if:
1. 열린 괄호는 반드시 **같은 종류의 닫힌 괄호**로 닫혀야 함  
2. 괄호는 **올바른 순서**로 닫혀야 함  
3. 모든 닫힌 괄호는 **대응되는 열린 괄호**가 있어야 함

---

## 🧪 Examples (예시)

### Example 1

**Input:** `s = "()"`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `true`  
**Explanation:** 괄호가 올바르게 짝지어졌습니다.

</details>

---

### Example 2

**Input:** `s = "()[]{}"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `true`

</details>

---

### Example 3

**Input:** `s = "(]"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `false`

</details>

---

### Example 4

**Input:** `s = "([])"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `true`

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= s.length <= 10⁴`  
- `s`는 `'()[]{}'` 문자만 포함됩니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 스택 자료구조를 사용해보세요.
- 열린 괄호는 스택에 push하고,
- 닫힌 괄호가 나오면 스택에서 pop해서 짝이 맞는지 확인하세요.
- 문자열을 순차적으로 검사하다가 불일치가 발생하면 바로 False를 반환할 수 있습니다.

</details>
