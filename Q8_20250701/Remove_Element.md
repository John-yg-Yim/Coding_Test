# Q27 - Remove Element (원소 제거)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #27](https://leetcode.com/problems/remove-element/) | **출처:** LeetCode 문제 27번

---

## 📘 Problem Description (문제 설명)

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.  
→ 정수 배열 `nums`와 정수 `val`이 주어질 때, `val`과 같은 값을 **제자리(in-place)** 에서 모두 제거하세요.

The order of the elements may be changed.  
→ 요소들의 순서는 **바뀌어도 상관 없습니다.**

Then return the number of elements in `nums` which are not equal to `val`.  
→ `val`과 **다른 값**이 몇 개인지(`k`)를 반환하세요.

---

## 📌 Additional Notes (추가 설명)

- `nums`의 처음 `k`개의 요소는 `val`이 아닌 값이어야 합니다.
- `k` 이후의 값들은 어떤 값이 와도 상관 없습니다.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `nums = [3,2,2,3]`, `val = 3`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `2`, `nums = [2,2,_,_]`  
**Explanation:** 반환값 `k = 2`. 처음 두 요소는 `2`, `2`여야 하며, 이후는 중요하지 않음.

</details>

---

### Example 2

**Input:** `nums = [0,1,2,2,3,0,4,2]`, `val = 2`

<details>
<summary>✅ Output 보기</summary>

**Output:** `5`, `nums = [0,1,4,0,3,_,_,_]`

</details>

---

## 📌 Constraints (제약 조건)

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 배열을 앞에서부터 순회하며 `val`과 다른 값을 덮어쓰는 방식으로 풀어보세요.
- 두 포인터 또는 단일 포인터를 사용해도 됩니다.
- 순서가 중요하지 않으므로 `val`인 요소와 배열 끝 요소를 swap하는 전략도 가능합니다.

</details>