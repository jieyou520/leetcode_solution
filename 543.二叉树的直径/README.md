# [543] 二叉树的直径

- **LeetCode 链接**: [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

## 题目描述

给一棵二叉树，求它的直径，也就是树中任意两个节点之间最长路径经过的边数。注意这条最长路径不一定经过根节点。

## 思路

1. **核心思想**：最长的路径一定会在某个节点那里“拐个弯”，一边伸进它的左子树，一边伸进它的右子树，所以路径长度就是左子树深度加右子树深度。
2. **思考过程**：如果只想某个节点的左右子树深度，递归就可以完成。问题是路径可能出现在任何一个节点下面，所以要在递归求深度的过程中，把每个节点“左深 + 右深”的结果都记录一下，最后取最大的那个。
3. **关键点**：题目说的直径是边的数量，不是节点的数量；递归往上返回时要返回 `max(左深, 右深) + 1`，但更新答案时要用 `左深 + 右深`。

## 解法

### 方法一：递归求深度并顺便更新直径
* **思路**：递归算出每个节点的左右子树深度，用 `l + r` 更新全局答案，向上返回时只返回较深那一边再加 1。
* **代码**：
    ```python
    class Solution:
        def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            ans = 0
            def getDepth(node):
                nonlocal ans
                if not node:
                    return 0
                l = getDepth(node.left)
                r = getDepth(node.right)
                ans = max(ans,l+r)
                return max(l,r)+1
            getDepth(root)
            return ans
    ```
