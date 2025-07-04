# Q58 - Length of Last Word (마지막 단어의 길이)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #58](https://leetcode.com/problems/length-of-last-word/) | **출처:** LeetCode 문제 58번

---

## 📘 Problem Description (문제 설명)

Given a string `s` consisting of words and spaces, return the length of the last word in the string.  
→ 공백과 단어로 이루어진 문자열 `s`가 주어질 때, **마지막 단어의 길이**를 반환하세요.

A word is a maximal substring consisting of non-space characters only.  
→ 단어는 **공백이 아닌 문자로 이루어진 최대 부분 문자열**을 의미합니다.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `s = "Hello World"`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `5`  
**Explanation:** 마지막 단어는 `"World"`이며 길이는 `5`입니다.

</details>

---

### Example 2

**Input:** `s = "   fly me   to   the moon  "`

<details>
<summary>✅ Output 보기</summary>

**Output:** `4`  
**Explanation:** 마지막 단어는 `"moon"`이며 길이는 `4`입니다.

</details>

---

### Example 3

**Input:** `s = "luffy is still joyboy"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `6`  
**Explanation:** 마지막 단어는 `"joyboy"`이며 길이는 `6`입니다.

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= s.length <= 10⁴`
- `s`는 영어 알파벳과 공백 `' '`으로만 구성됩니다.
- `s`에는 적어도 하나의 단어가 포함됩니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 문자열을 공백 기준으로 나눈 후, 마지막 단어의 길이를 구해보세요.
- 공백이 여러 개일 수 있으므로 `.strip()`을 사용하여 양쪽 공백을 제거하면 유용합니다.

</details>