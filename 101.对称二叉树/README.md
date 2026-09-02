# [101] 对称二叉树

- **LeetCode 链接**: [对称二叉树](https://leetcode.cn/problems/symmetric-tree/)
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

## 题目描述

给定一个二叉树的根节点 `root`，检查它是否轴对称。

## 思路

1. **核心思想**：二叉树对称等价于左右两棵子树互为镜像，可以递归比较一棵树的左子树和另一棵树的右子树。
2. **思考过程**：可以先判断两个节点本身是否相等，再递归判断镜像位置上的子树是否也满足条件。
3. **关键点**：两个节点都为空时对称；只有一个为空或值不相等时不对称；根节点为空时也认为是对称树。

## 解法

### 方法一：递归
* **思路**：比较根节点的左右子树是否互为镜像，递归检查 `left.left` 和 `right.right`、`left.right` 和 `right.left`。
* **代码**：
    ```python
    class Solution:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            return self.isSameTree(root.left, root.right)
    ```
