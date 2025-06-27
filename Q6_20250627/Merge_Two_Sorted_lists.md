# Q21 - Merge Two Sorted Lists (두 정렬 리스트 병합하기)

**Difficulty:** Easy | **난이도:** 쉬움
**Source:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) | **출처:** LeetCode 문제 21번

---

## 📘 Problem Description (문제 설명)

You are given the heads of two sorted linked lists `list1` and `list2`.
→ 정렬된 두 연결 리스트 `list1`과 `list2`의 **헤드 노드**가 주어집니다.

Merge the two lists into one sorted list.
→ 두 리스트를 하나의 **정렬된 연결 리스트**로 병합하세요.

The list should be made by **splicing together the nodes** of the first two lists.
→ 결과 리스트는 주어진 두 리스트의 노드를 **이어 붙여서(splice)** 만들어야 합니다.

Return the **head** of the merged linked list.
→ 병합된 연결 리스트의 **헤드 노드**를 반환하세요.

---

## 🧪 Examples (예시)

### Example 1

![Merge Two Sorted Lists](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`

<details>
<summary>✅ Output & Explanation (정답과 해설 보기)</summary>

**Output:** `[1,1,2,3,4,4]`
**Explanation:** 정렬된 상태를 유지하면서 노드를 차례로 이어 붙입니다.

</details>

---

### Example 2

**Input:** `list1 = []`, `list2 = []`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[]`

</details>

---

### Example 3

**Input:** `list1 = []`, `list2 = [0]`

<details>
<summary>✅ Output 보기</summary>

**Output:** `[0]`

</details>

---

## 📌 Constraints (제약 조건)

- 두 리스트의 노드 수는 `0 ~ 50`개 사이
- 각 노드의 값은 `-100 <= Node.val <= 100`
- 두 리스트는 **비내림차순(non-decreasing order)**으로 정렬되어 있음

---

## 💡 Hint (힌트 보기)

<details>
<summary>💡 Hint</summary>

- 새 리스트를 만들 필요 없이, 기존 노드들을 재배열하세요.
- 더미 노드를 하나 만들고, 두 리스트를 순차적으로 비교하면서 작은 쪽을 연결해 주세요.
- 마지막에는 남아 있는 노드를 통째로 붙이면 됩니다.

</details>