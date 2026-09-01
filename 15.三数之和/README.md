# [15] 三数之和

- **LeetCode 链接**: [三数之和](https://leetcode.cn/problems/3sum/)
- **难度**: Medium
- **标签**: `#数组` `#双指针` `#排序`

## 题目描述

给定一个整数数组 `nums`，判断是否存在三个元素 `a`、`b`、`c`，使得 `a + b + c = 0`。返回所有和为 `0` 且不重复的三元组。

## 思路

1. **核心思想**：先将数组排序，固定一个数，再用双指针在剩余区间中寻找另外两个数。
2. **思考过程**：暴力解需要三层循环，时间复杂度为 O(n^3)。排序后可以利用双指针让另外两个数从两端向中间移动，同时通过跳过重复值来避免重复答案。
3. **关键点**：固定数大于 0 时可以直接结束；固定数和指针移动时都要跳过相同元素，避免产生重复三元组。

## 解法

### 方法一：排序 + 双指针
* **思路**：固定第一个数 `nums[i]`，用左右指针在 `i + 1` 到末尾之间寻找和为 `-nums[i]` 的两个数。
* **代码**：
    ```python
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:

            n=len(nums)
            if(not nums or n<3):
                return []
            nums.sort()
            res=[]
            for i in range(n):
                if(nums[i]>0):
                    return res
                if(i>0 and nums[i]==nums[i-1]):
                    continue
                L=i+1
                R=n-1
                while(L<R):
                    if(nums[i]+nums[L]+nums[R]==0):
                        res.append([nums[i],nums[L],nums[R]])
                        while(L<R and nums[L]==nums[L+1]):
                            L=L+1
                        while(L<R and nums[R]==nums[R-1]):
                            R=R-1
                        L=L+1
                        R=R-1
                    elif(nums[i]+nums[L]+nums[R]>0):
                        R=R-1
                    else:
                        L=L+1
            return res
    ```
