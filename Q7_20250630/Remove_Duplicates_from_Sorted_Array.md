# Q26 - Remove Duplicates from Sorted Array (정렬된 배열에서 중복 제거)

**Difficulty:** Easy | **난이도:** 쉬움  
**Source:** [LeetCode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | **출처:** LeetCode 문제 26번

---

## 📘 Problem Description (문제 설명)

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.  
→ 비내림차순(오름차순 포함)으로 정렬된 정수 배열 `nums`가 주어집니다.  
→ 배열의 중복된 값을 **제자리(in-place)**에서 제거하여, 각 고유한 요소가 한 번씩만 나타나도록 하세요.

The relative order of the elements should be kept the same.  
→ 고유한 요소들의 **상대적인 순서는 유지**해야 합니다.

Then return the number of unique elements in `nums`.  
→ 고유한 요소의 개수 `k`를 반환하세요.

---

## 📌 Additional Notes (추가 설명)

- `nums` 배열의 처음 `k`개의 요소에 고유 값이 채워져 있어야 합니다.
- `k` 이후의 값들은 중요하지 않습니다 (어떤 값이든 상관 없음).

---

## 🧪 Examples (예시)

### Example 1

**Input:** `nums = [1,1,2]`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `2`, `nums = [1,2,_]`  
**Explanation:** 반환값 `k = 2`. 배열의 처음 두 요소는 `1`, `2`여야 하며, 이후 값은 중요하지 않음.

</details>

---

### Example 2

**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`

<details>
<summary>✅ Output 보기</summary>

**Output:** `5`, `nums = [0,1,2,3,4,_,_,_,_,_]`

</details>

---

## 📌 Constraints (제약 조건)

- `1 <= nums.length <= 3 * 10⁴`
- `-100 <= nums[i] <= 100`
- `nums`는 비내림차순으로 정렬되어 있습니다.

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 두 개의 포인터를 사용하세요.
- 하나는 고유 원소를 넣을 위치를 가리키고, 다른 하나는 배열을 순회하며 새 고유 값을 찾습니다.
- 새로운 고유 값이 나오면 고유 원소를 넣을 위치에 덮어씁니다.

</details>