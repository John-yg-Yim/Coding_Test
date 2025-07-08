# Q67 - Add Binary (이진수 덧셈)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #67](https://leetcode.com/problems/add-binary/) | **출처:** LeetCode 문제 67번

---

## 📘 Problem Description (문제 설명)

Given two binary strings `a` and `b`, return their sum as a binary string.  
→ 이진수 문자열 `a`와 `b`가 주어질 때, 이 둘을 **덧셈한 결과를 이진수 문자열로 반환**하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `a = "11"`, `b = "1"`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `"100"`  
**Explanation:** `11₂ + 1₂ = 100₂`

</details>

---

### Example 2

**Input:** `a = "1010"`, `b = "1011"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `"10101"`  
**Explanation:** `1010₂ + 1011₂ = 10101₂`

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= a.length, b.length <= 10⁴`
- `a`와 `b`는 **'0' 또는 '1'로만 구성된 이진 문자열**
- 선행 0은 포함되지 않음 (단, `"0"` 하나만 있을 경우는 예외)

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 두 문자열을 끝에서부터 오른쪽에서 왼쪽으로 진행하면서 한 자리씩 더합니다.
- `carry` 변수를 활용해 올림을 추적해야 합니다.
- 최종 결과는 **역순(reverse)** 으로 구성될 수 있으니 주의하세요.
- 파이썬의 내장 `bin()` 또는 `int(a, 2) + int(b, 2)` 후 `bin()` 으로 푸는 것도 가능하지만, 자리수 연산으로 직접 구현하는 것도 추천됩니다.

</details>