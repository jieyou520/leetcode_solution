# [94] 二叉树的中序遍历

- **LeetCode 链接**: [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

## 题目描述

给定一个二叉树的根节点 `root`，返回它的中序遍历结果。

## 思路

1. **核心思想**：按照“左子树、根节点、右子树”的顺序递归遍历整棵二叉树。
2. **思考过程**：中序遍历天然适合递归实现，先递归处理左子树，再加入当前节点值，最后递归处理右子树。
3. **关键点**：递归终止条件是节点为空；空树应该返回空列表。

## 解法

### 方法一：递归
* **思路**：定义一个辅助函数，当前节点为空时直接返回，否则依次处理左子树、当前节点、右子树。
* **代码**：
    ```python
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            def inorder(node):
                if node is None:
                    return
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
            inorder(root)
            return res
    ```
