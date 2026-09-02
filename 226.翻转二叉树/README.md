# [226] 翻转二叉树

- **LeetCode 链接**: [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

## 题目描述

给定一棵二叉树的根节点 `root`，翻转这棵二叉树，并返回其根节点。

## 思路

1. **核心思想**：递归翻转左右子树后，交换当前节点的左右孩子，整棵树就完成了左右镜像翻转。
2. **思考过程**：翻转操作对每个节点都是相同的：先让左子树和右子树各自完成翻转，再交换左右子树。
3. **关键点**：递归终止条件是空节点；交换时要保存递归翻转后的左孩子，避免被覆盖。

## 解法

### 方法一：递归
* **思路**：先递归翻转左右子树，再把当前节点的左右孩子交换。
* **代码**：
    ```python
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root
    ```
