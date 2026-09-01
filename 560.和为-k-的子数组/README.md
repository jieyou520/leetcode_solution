# [560] 和为 K 的子数组

- **LeetCode 链接**: [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
- **难度**: Medium
- **标签**: `#数组` `#哈希表` `#前缀和`

## 题目描述

给定一个整数数组 `nums` 和一个整数 `k`，统计并返回和为 `k` 的连续子数组的个数。

## 思路

1. **核心思想**：利用前缀和，把“子数组和等于 k”转化为“两个前缀和之差等于 k”，并用哈希表记录前缀和出现的次数。
2. **思考过程**：暴力解需要枚举所有子数组，时间复杂度为 O(n^2)。对于每个前缀和 `sj`，只要之前出现过 `sj - k`，就说明中间这一段子数组的和为 k。
3. **关键点**：先统计 `sj - k` 的个数再加入当前 `sj`，保证使用当前元素之前的前缀和；空前缀和 0 要初始化为 1。

## 解法

### 方法一：前缀和 + 哈希表
* **思路**：先求出所有前缀和，再遍历每个前缀和，用哈希表统计之前出现过的前缀和次数。
* **代码**：
    ```python
    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            s = [0] * (len(nums) + 1)
            for i, x in enumerate(nums):
                s[i + 1] = s[i] + x

            cnt = defaultdict(int)
            ans = 0
            for sj in s:
                ans += cnt[sj - k]
                cnt[sj] += 1
            return ans
    ```
