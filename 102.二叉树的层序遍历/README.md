# [102] 二叉树的层序遍历

- **LeetCode 链接**: [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
- **难度**: Medium
- **标签**: `#二叉树` `#广度优先搜索` `#队列`

## 题目描述

给一棵二叉树，按从上到下的顺序一层一层地遍历，最后返回一个二维数组：每个数组里放这一层所有节点的值。

## 思路

1. **核心思想**：把每一层当成一波节点来排队处理。先处理当前这一层的节点，顺手把它们的左右孩子收集起来，当成下一层继续处理。
2. **思考过程**：层序遍历不像是递归“一路扎到底”，更像是“一层一层往外扩”。可以先用一个列表装当前层的节点，每看完一层，就用刚收集到的孩子列表替换成新的当前层。
3. **关键点**：空树直接返回空列表；每一层都要用一个新的列表来装下一层，不能把所有层的节点混在一起。

## 解法

### 方法一：逐层收集节点
* **思路**：用 `cur` 表示当前层的节点，遍历它们把值记下来，同时把左右孩子收集到 `nxt` 里，然后让 `cur = nxt` 继续下一层。
* **代码**：
    ```python
    class Solution:
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            ans = []
            cur = [root]
            if root is None:
                return []
            while cur:
                vals = []
                nxt = []
                for node in cur:
                    vals.append(node.val)
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                ans.append(vals)
                cur = nxt
            return ans
    ```
