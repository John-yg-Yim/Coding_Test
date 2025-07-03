# Q35 - Search Insert Position (삽입 위치 찾기)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #35](https://leetcode.com/problems/search-insert-position/) | **출처:** LeetCode 문제 35번

---

## 📘 Problem Description (문제 설명)

Given a sorted array of distinct integers and a target value, return the index if the target is found.  
→ 정렬된 **중복 없는** 정수 배열 `nums`와 정수 `target`이 주어집니다.  
→ `target`이 존재하면 해당 인덱스를 반환하세요.

If not, return the index where it would be if it were inserted in order.  
→ `target`이 없다면 **삽입 시 위치 인덱스**를 반환하세요.

You must write an algorithm with O(log n) runtime complexity.  
→ O(log n) 시간 복잡도를 가져야 합니다.

---

## 🧪 Examples (예시)

### Example 1

**Input:** `nums = [1,3,5,6]`, `target = 5`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `2`  
**Explanation:** `5`는 `nums[2]`에 있으므로 `2`를 반환합니다.

</details>

---

### Example 2

**Input:** `nums = [1,3,5,6]`, `target = 2`

<details>
<summary>✅ Output 보기</summary>

**Output:** `1`  
**Explanation:** `2`는 `1`과 `3` 사이에 들어가야 하므로 `1` 반환.

</details>

---

### Example 3

**Input:** `nums = [1,3,5,6]`, `target = 7`

<details>
<summary>✅ Output 보기</summary>

**Output:** `4`  
**Explanation:** `7`은 배열 끝에 삽입되어야 하므로 `4` 반환.

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums`는 **오름차순 정렬**되어 있으며 값이 중복되지 않음
- `-10⁴ <= target <= 10⁴`

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 이진 탐색 (binary search)로 `O(log n)` 시간 복잡도를 만족하세요.
- 배열을 순회하며 찾지 말고 중간 값을 비교하며 탐색 범위를 줄여나가세요.

</details>