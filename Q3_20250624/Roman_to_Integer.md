# Q13 - Roman to Integer (로마 숫자를 정수로 변환)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #13](https://leetcode.com/problems/roman-to-integer/) | **출처:** LeetCode 문제 13번

---

## 📘 Problem Description (문제 설명)

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.  
→ 로마 숫자는 `I`, `V`, `X`, `L`, `C`, `D`, `M`의 7가지 기호로 표현됩니다.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

- 예를 들어 2는 `II`, 12는 `XII`, 27은 `XXVII`로 표현됩니다.
- 일반적으로 숫자가 큰 기호부터 작은 기호 순서대로 작성됩니다.
- 그러나 4는 `IIII`가 아니라 `IV`로 표기되며, 이는 **작은 수가 큰 수 앞에 올 경우 그 값을 뺀다**는 규칙 때문입니다.

이 규칙이 적용되는 경우는 총 6가지입니다:

- `I`는 `V(5)`, `X(10)` 앞에 올 수 있습니다 → `4(IV)`, `9(IX)`
- `X`는 `L(50)`, `C(100)` 앞에 올 수 있습니다 → `40(XL)`, `90(XC)`
- `C`는 `D(500)`, `M(1000)` 앞에 올 수 있습니다 → `400(CD)`, `900(CM)`

**Given a Roman numeral, convert it to an integer.**  
→ 주어진 로마 숫자를 정수로 변환하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `s = "III"`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `3`  
**Explanation:** `III = 1 + 1 + 1 = 3`  
→ 각각 I = 1이므로 총 3입니다.

</details>

---

### Example 2

**Input:** `s = "LVIII"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `58`  
**Explanation:** `L = 50`, `V = 5`, `III = 3` → `50 + 5 + 3 = 58`

</details>

---

### Example 3

**Input:** `s = "MCMXCIV"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `1994`  
**Explanation:** `M = 1000`, `CM = 900`, `XC = 90`, `IV = 4`  
→ `1000 + 900 + 90 + 4 = 1994`

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= s.length <= 15`  
- `s`는 오직 `'I', 'V', 'X', 'L', 'C', 'D', 'M'` 문자만 포함  
- `s`는 **[1, 3999] 범위 내에서 유효한 로마 숫자**임이 보장됩니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 각 로마 문자의 값을 사전(dict)으로 매핑하면 편리합니다.
- 현재 문자의 값이 **다음 문자보다 작으면 뺄셈**, 그렇지 않으면 덧셈을 합니다.
- 예: `I`가 `V`보다 작으므로 `IV = 5 - 1 = 4`

</details>