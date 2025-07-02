# Q28 - Find the Index of the First Occurrence in a String (문자열에서 첫 번째 발생 인덱스 찾기)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | **출처:** LeetCode 문제 28번

---

## 📘 Problem Description (문제 설명)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.  
→ 문자열 `haystack`에서 `needle`이 처음 나타나는 위치의 인덱스를 반환하세요.  
→ 만약 `needle`이 포함되어 있지 않다면 `-1`을 반환하세요.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `haystack = "sadbutsad"`, `needle = "sad"`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `0`  
**Explanation:** `"sad"`는 인덱스 `0`과 `6`에서 나타나며, 첫 번째는 `0`이므로 `0`을 반환합니다.

</details>

---

### Example 2

**Input:** `haystack = "leetcode"`, `needle = "leeto"`

<details>
<summary>✅ Output 보기</summary>

**Output:** `-1`  
**Explanation:** `"leeto"`는 `"leetcode"`에 포함되지 않으므로 `-1`을 반환합니다.

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= haystack.length, needle.length <= 10⁴`
- `haystack`과 `needle`은 소문자 영어 알파벳만 포함됩니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- Python의 `str.find()` 또는 `str.index()` 같은 메서드를 사용할 수 있습니다.
- 직접 풀어보려면 슬라이딩 윈도우 또는 브루트포스 방식으로 두 문자열을 비교하세요.
- KMP (Knuth-Morris-Pratt) 같은 고급 문자열 탐색 알고리즘을 연습해도 좋습니다.

</details>