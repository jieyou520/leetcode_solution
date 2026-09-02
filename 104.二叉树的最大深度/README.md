# [104] 二叉树的最大深度

- **LeetCode 链接**: [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

## 题目描述

给定一个二叉树的根节点 `root`，返回它的最大深度。二叉树的深度是指从根节点到最远叶子节点的最长路径上的节点数。

## 思路

1. **核心思想**：当前子树的最大深度等于左右子树最大深度中的较大值加一。
2. **思考过程**：递归可以自然地把问题拆成子问题：先求左子树深度和右子树深度，再返回较大值加一。
3. **关键点**：空节点的深度为 0；递归时先处理边界条件再向下深入。

## 解法

### 方法一：递归
* **思路**：空节点返回 0，否则返回左右子树最大深度的较大值加 1。
* **代码**：
    ```python
    class Solution:
        def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
    ```
