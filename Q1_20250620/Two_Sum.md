# Q1 - Two Sum (두 수의 합)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #1](https://leetcode.com/problems/two-sum/) | **출처:** LeetCode 문제 1번

---

## 📘 Problem Description (문제 설명)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.  
→ 정수 배열 `nums`와 정수 `target`이 주어질 때, 두 수를 더해 `target`이 되는 **두 숫자의 인덱스**를 반환하세요.

You may assume that each input would have exactly one solution, and you may not use the same element twice.  
→ 정답은 항상 **하나만 존재**하며, **같은 원소를 두 번 사용할 수 없습니다.**

You can return the answer in any order.  
→ 반환 순서는 **상관없습니다.**

---

## 🧪 Examples (예시)

### Example 1

**Input:** `nums = [2, 7, 11, 15]`, `target = 9`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `[0, 1]`  
**Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.  
→ `nums[0] + nums[1] == 9` 이므로 `[0, 1]`을 반환합니다.

</details>

---

### Example 2

**Input:** `nums = [3, 2, 4]`, `target = 6`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[1, 2]`

</details>

---

### Example 3

**Input:** `nums = [3, 3]`, `target = 6`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[0, 1]`

</details>

---

## 📌 Constraints (제약 조건)

- `2 <= nums.length <= 10⁴`  
- `-10⁹ <= nums[i] <= 10⁹`  
- `-10⁹ <= target <= 10⁹`  
- Only one valid answer exists.  
→ 정답은 반드시 하나 존재합니다.

---

## 🔍 Follow-up (심화 질문)

Can you come up with an algorithm that has better than O(n²) time complexity?  
→ **O(n²)**보다 효율적인 알고리즘을 떠올릴 수 있나요?

---

<details>
<summary>💡 Hint (힌트 보기)</summary>

- A brute force approach would be checking all pairs — what's the time complexity?  
→ 모든 쌍을 검사하는 완전탐색 방식은 어떤 시간 복잡도를 가질까요?

- Can a hash map help reduce the lookup time?  
→ **해시맵**을 사용하면 탐색 속도를 줄일 수 있을까요?

</details>