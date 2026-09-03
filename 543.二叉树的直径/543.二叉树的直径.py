#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
    
# @lc code=end

