# [49] 字母异位词分组

- **LeetCode 链接**: [字母异位词分组](https://leetcode.cn/problems/group-anagrams/)
- **难度**: Medium
- **标签**: `#哈希表` `#字符串` `#排序`

## 题目描述

给定一个字符串数组 `strs`，将字母异位词组合在一起。可以按任意顺序返回结果列表。

## 思路

1. **核心思想**：字母异位词排序后的字符串相同，用排序结果作为哈希表的键，把相同键的字符串归入同一组。
2. **思考过程**：暴力解需要两两比较是否为异位词。每个字符串排序后，同一组异位词会得到同一个键，因此一次遍历即可完成分组。
3. **关键点**：排序后的字符串可以作为稳定且唯一的键；用 `defaultdict(list)` 可以避免手动判断键是否存在。

## 解法

### 方法一：排序 + 哈希表
* **思路**：遍历每个字符串，将其排序后的结果作为键加入哈希表，最后返回所有分组。
* **代码**：
    ```python
    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            seen = defaultdict(list)

            for s in strs:
                key = ''.join(sorted(s))
                seen[key].append(s)

            return list(seen.values())
    ```
