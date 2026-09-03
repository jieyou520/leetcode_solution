# LeetCode 刷题笔记整理

这里把每道题目的笔记按统一格式整理在一起，方便直接阅读和复习。

## [1] 两数之和

- **题目来源**: LeetCode 第 1 题
- **难度**: Easy
- **标签**: `#数组` `#哈希表`

### 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，在数组中找出和为目标值的两个整数，并返回它们的数组下标。假设每种输入只会对应一个答案，且同一个元素不能使用两次。

### 思路

1. **核心思想**：利用哈希表存储已遍历的元素及其索引，在遍历时检查 `target - nums[i]` 是否已经出现过。
2. **思考过程**：暴力解是枚举每一对 `(i, j)`，时间复杂度为 O(n^2)。哈希表可以把查找补数的时间从 O(n) 降到 O(1)，只需要一次遍历。
3. **关键点**：先查找补数再写入当前元素，避免同一个元素被使用两次；哈希表的键为元素值，值为元素下标。

### 解法

#### 方法一：哈希表
* **思路**：一次遍历，用字典保存已经见过的数字和下标；每遇到一个数字就检查 `target - num` 是否已经在字典中。
* **代码**：
    ```python
    class Solution(object):
        def twoSum(self, nums, target):
            seen = {}
            for i,num in enumerate(nums):
                c = target - num
                if c in seen:
                    return[seen[c],i]
                seen[num] = i
    ```

## [3] 无重复字符的最长子串

- **题目来源**: LeetCode 第 3 题
- **难度**: Medium
- **标签**: `#哈希表` `#字符串` `#滑动窗口`

### 题目描述

给定一个字符串 `s`，找出其中不含有重复字符的最长子串的长度。

### 思路

1. **核心思想**：用哈希表记录每个字符最近一次出现的位置，用动态规划维护以当前字符结尾的最长无重复子串长度。
2. **思考过程**：暴力解需要枚举所有子串并检查是否重复。用哈希表保存字符位置后，可以 O(1) 得到上一个相同字符的位置，从而递推当前最长长度。
3. **关键点**：`tmp` 表示以 `s[j]` 结尾的最长无重复子串长度；当出现重复字符时，新的长度不能超过 `j - i`。

### 解法

#### 方法一：哈希表 + 动态规划
* **思路**：遍历字符串，记录每个字符最近出现的下标，并根据 `j - i` 和上一轮长度递推当前无重复子串长度。
* **代码**：
    ```python
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            dic = {}
            res = tmp = 0
            for j in range(len(s)):
                i = dic.get(s[j], -1)
                dic[s[j]] = j
                tmp = tmp + 1 if tmp < j - i else j - i
                res = max(res, tmp)
            return res
    ```

## [11] 盛最多水的容器

- **题目来源**: LeetCode 第 11 题
- **难度**: Medium
- **标签**: `#数组` `#双指针`

### 题目描述

给定一个长度为 `n` 的整数数组 `height`，其中每个元素代表坐标 `(i, height[i])` 处的一条垂直线。找出其中的两条线，使它们与 `x` 轴共同构成的容器可以容纳最多的水，返回容器可以储存的最大水量。

### 思路

1. **核心思想**：用左右两个指针从数组两端向中间移动，容器的容量由较短的一边和宽度决定，因此每次移动较短的一边。
2. **思考过程**：暴力解是枚举所有左右边界组合，时间复杂度为 O(n^2)。双指针每次都能排除一批不可能更大的组合，把复杂度降到 O(n)。
3. **关键点**：宽度减少时只有提高较短边的高度才可能让容量变大；记录并更新遍历过程中的最大面积。

### 解法

#### 方法一：双指针
* **思路**：左右指针分别指向数组两端，计算当前容器的面积并记录最大值；比较两边高度，移动较矮的一侧继续计算。
* **代码**：
    ```python
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            l_max = []
            x = len(height)-1
            count_right = len(height)-1
            count_left = 0
            area1 = min(height[0],height[-1])*x
            l_max.append(area1)
            for i in range(0,len(height)-1):
                if height[count_left] <= height[count_right]:
                    count_left += 1
                    x -= 1
                    area = min(height[count_left],height[count_right])*x
                    l_max.append(area)
                else:
                    count_right -= 1
                    x -= 1
                    area = min(height[count_left],height[count_right])*x
                    l_max.append(area)
            return max(l_max)
    ```

## [15] 三数之和

- **题目来源**: LeetCode 第 15 题
- **难度**: Medium
- **标签**: `#数组` `#双指针` `#排序`

### 题目描述

给定一个整数数组 `nums`，判断是否存在三个元素 `a`、`b`、`c`，使得 `a + b + c = 0`。返回所有和为 `0` 且不重复的三元组。

### 思路

1. **核心思想**：先将数组排序，固定一个数，再用双指针在剩余区间中寻找另外两个数。
2. **思考过程**：暴力解需要三层循环，时间复杂度为 O(n^3)。排序后可以利用双指针让另外两个数从两端向中间移动，同时通过跳过重复值来避免重复答案。
3. **关键点**：固定数大于 0 时可以直接结束；固定数和指针移动时都要跳过相同元素，避免产生重复三元组。

### 解法

#### 方法一：排序 + 双指针
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

## [42] 接雨水

- **题目来源**: LeetCode 第 42 题
- **难度**: Hard
- **标签**: `#数组` `#双指针`

### 题目描述

给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子下雨之后能接多少雨水。

### 思路

1. **核心思想**：某个位置能接的水量等于它左右两边最大高度中的较小值减去当前高度，用双指针从两端向中间计算。
2. **思考过程**：暴力解需要为每个位置分别求左右最大高度。双指针从两端移动时，可以只维护已经扫过部分的最高高度，一次遍历完成计算。
3. **关键点**：每次移动较矮一侧的指针，并用当前侧的已知最大高度计算积水量；两个方向的最大高度分别用 `leftCeil` 和 `rightCeil` 维护。

### 解法

#### 方法一：双指针
* **思路**：左右指针从两端向中间移动，维护两侧的最大高度，每次按较矮一侧能承接的水量累加。
* **代码**：
    ```python
    class Solution:
        def trap(self, height: List[int]) -> int:
            l, r = 0, len(height) - 1
            cap = 0
            leftCeil, rightCeil = 0, 0

            while l <= r:
                leftCeil = max(leftCeil, height[l])
                rightCeil = max(rightCeil, height[r])

                if leftCeil < rightCeil:
                    cap += leftCeil - height[l]
                    l += 1
                else:
                    cap += rightCeil - height[r]
                    r -= 1

            return cap
    ```

## [49] 字母异位词分组

- **题目来源**: LeetCode 第 49 题
- **难度**: Medium
- **标签**: `#哈希表` `#字符串` `#排序`

### 题目描述

给定一个字符串数组 `strs`，将字母异位词组合在一起。可以按任意顺序返回结果列表。

### 思路

1. **核心思想**：字母异位词排序后的字符串相同，用排序结果作为哈希表的键，把相同键的字符串归入同一组。
2. **思考过程**：暴力解需要两两比较是否为异位词。每个字符串排序后，同一组异位词会得到同一个键，因此一次遍历即可完成分组。
3. **关键点**：排序后的字符串可以作为稳定且唯一的键；用 `defaultdict(list)` 可以避免手动判断键是否存在。

### 解法

#### 方法一：排序 + 哈希表
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

## [94] 二叉树的中序遍历

- **题目来源**: LeetCode 第 94 题
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

### 题目描述

给定一个二叉树的根节点 `root`，返回它的中序遍历结果。

### 思路

1. **核心思想**：按照“左子树、根节点、右子树”的顺序递归遍历整棵二叉树。
2. **思考过程**：中序遍历天然适合递归实现，先递归处理左子树，再加入当前节点值，最后递归处理右子树。
3. **关键点**：递归终止条件是节点为空；空树应该返回空列表。

### 解法

#### 方法一：递归
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

## [101] 对称二叉树

- **题目来源**: LeetCode 第 101 题
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

### 题目描述

给定一个二叉树的根节点 `root`，检查它是否轴对称。

### 思路

1. **核心思想**：二叉树对称等价于左右两棵子树互为镜像，可以递归比较一棵树的左子树和另一棵树的右子树。
2. **思考过程**：可以先判断两个节点本身是否相等，再递归判断镜像位置上的子树是否也满足条件。
3. **关键点**：两个节点都为空时对称；只有一个为空或值不相等时不对称；根节点为空时也认为是对称树。

### 解法

#### 方法一：递归
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

## [102] 二叉树的层序遍历

- **题目来源**: LeetCode 第 102 题
- **难度**: Medium
- **标签**: `#二叉树` `#广度优先搜索` `#队列`

### 题目描述

给一棵二叉树，按从上到下的顺序一层一层地遍历，最后返回一个二维数组：每个数组里放这一层所有节点的值。

### 思路

1. **核心思想**：把每一层当成一波节点来排队处理。先处理当前这一层的节点，顺手把它们的左右孩子收集起来，当成下一层继续处理。
2. **思考过程**：层序遍历不像是递归“一路扎到底”，更像是“一层一层往外扩”。可以先用一个列表装当前层的节点，每看完一层，就用刚收集到的孩子列表替换成新的当前层。
3. **关键点**：空树直接返回空列表；每一层都要用一个新的列表来装下一层，不能把所有层的节点混在一起。

### 解法

#### 方法一：逐层收集节点
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

## [104] 二叉树的最大深度

- **题目来源**: LeetCode 第 104 题
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

### 题目描述

给定一个二叉树的根节点 `root`，返回它的最大深度。二叉树的深度是指从根节点到最远叶子节点的最长路径上的节点数。

### 思路

1. **核心思想**：当前子树的最大深度等于左右子树最大深度中的较大值加一。
2. **思考过程**：递归可以自然地把问题拆成子问题：先求左子树深度和右子树深度，再返回较大值加一。
3. **关键点**：空节点的深度为 0；递归时先处理边界条件再向下深入。

### 解法

#### 方法一：递归
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

## [128] 最长连续序列

- **题目来源**: LeetCode 第 128 题
- **难度**: Medium
- **标签**: `#数组` `#哈希表`

### 题目描述

给定一个未排序的整数数组 `nums`，找出数字连续的最长序列的长度，并且要求算法的时间复杂度为 O(n)。

### 思路

1. **核心思想**：先把所有数字放入哈希集合，只从连续序列的起点开始向后扩展，避免重复统计。
2. **思考过程**：暴力解会对每个数字都向左向右查找，时间复杂度高。用集合保存元素后，查找相邻数字只需要 O(1)；只有当 `num - 1` 不存在时，`num` 才可能是连续序列的起点。
3. **关键点**：先判断 `num - 1` 是否在集合中，保证每个连续序列只被统计一次；集合可以去重，避免相同数字重复计算。

### 解法

#### 方法一：哈希集合
* **思路**：遍历集合中的每个数字，如果它是连续序列的起点，就不断向后查找并更新最长长度。
* **代码**：
    ```python
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            nums_set = set(nums)
            long = 0
            for num in nums_set:
                if num-1 not in nums_set:
                    corrent_num = num
                    corrent_len = 1
                    while corrent_num +1 in nums_set:
                        corrent_len += 1
                        corrent_num += 1
                    long = max(long,corrent_len)
            return long
    ```

## [226] 翻转二叉树

- **题目来源**: LeetCode 第 226 题
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

### 题目描述

给定一棵二叉树的根节点 `root`，翻转这棵二叉树，并返回其根节点。

### 思路

1. **核心思想**：递归翻转左右子树后，交换当前节点的左右孩子，整棵树就完成了左右镜像翻转。
2. **思考过程**：翻转操作对每个节点都是相同的：先让左子树和右子树各自完成翻转，再交换左右子树。
3. **关键点**：递归终止条件是空节点；交换时要保存递归翻转后的左孩子，避免被覆盖。

### 解法

#### 方法一：递归
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

## [283] 移动零

- **题目来源**: LeetCode 第 283 题
- **难度**: Easy
- **标签**: `#数组` `#双指针`

### 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。要求必须在原数组上操作，不能拷贝额外数组。

### 思路

1. **核心思想**：遍历数组时把遇到的 `0` 从当前位置移除并追加到数组末尾，保持非零元素的相对顺序不变。
2. **思考过程**：直接删除元素会让后续下标变化，因此用一个计数器修正当前检查位置；另一种常见做法是用双指针把非零元素依次前移。
3. **关键点**：所有操作都在原数组上完成；移动后要保证剩余的非零元素仍然按原来的相对顺序排列。

### 解法

#### 方法一：原地移除并追加
* **思路**：从头遍历数组，遇到 `0` 就弹出该元素并追加到末尾，同时调整当前遍历位置。
* **代码**：
    ```python
    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            count = 0
            if len(nums) != 1:
                for i in range(0,len(nums)-1):
                    if nums[i+count] == 0:
                        nums.pop(i+count)
                        nums.append(0)
                        count -= 1
            return nums
    ```

## [438] 找到字符串中所有字母异位词

- **题目来源**: LeetCode 第 438 题
- **难度**: Medium
- **标签**: `#字符串` `#哈希表` `#滑动窗口`

### 题目描述

给定两个字符串 `s` 和 `p`，在 `s` 中找到所有 `p` 的异位词的子串，返回这些子串的起始索引。

### 思路

1. **核心思想**：用固定长度的滑动窗口维护 `s` 中与 `p` 等长的子串，并用字符计数比较窗口内容是否和 `p` 的字符组成相同。
2. **思考过程**：暴力解会为每个可能的起点重新统计窗口，时间复杂度高。滑动窗口只需要在右端加入新字符、在左端移除旧字符，即可 O(1) 增量更新计数。
3. **关键点**：窗口长度始终为 `len(p)`；比较两个 `Counter` 相等时记录左端下标，然后移除窗口最左侧字符为下一轮做准备。

### 解法

#### 方法一：滑动窗口 + 哈希计数
* **思路**：维护 `s` 中长度等于 `len(p)` 的窗口计数，和 `p` 的计数相等时记录窗口起点。
* **代码**：
    ```python
    class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            cnt_p = Counter(p)
            cnt_s = Counter()
            ans = []

            for right, c in enumerate(s):
                cnt_s[c] += 1

                left = right - len(p) + 1
                if left < 0:
                    continue

                if cnt_s == cnt_p:
                    ans.append(left)

                cnt_s[s[left]] -= 1

            return ans
    ```

## [543] 二叉树的直径

- **题目来源**: LeetCode 第 543 题
- **难度**: Easy
- **标签**: `#二叉树` `#深度优先搜索` `#递归`

### 题目描述

给一棵二叉树，求它的直径，也就是树中任意两个节点之间最长路径经过的边数。注意这条最长路径不一定经过根节点。

### 思路

1. **核心思想**：最长的路径一定会在某个节点那里“拐个弯”，一边伸进它的左子树，一边伸进它的右子树，所以路径长度就是左子树深度加右子树深度。
2. **思考过程**：如果只想某个节点的左右子树深度，递归就可以完成。问题是路径可能出现在任何一个节点下面，所以要在递归求深度的过程中，把每个节点“左深 + 右深”的结果都记录一下，最后取最大的那个。
3. **关键点**：题目说的直径是边的数量，不是节点的数量；递归往上返回时要返回 `max(左深, 右深) + 1`，但更新答案时要用 `左深 + 右深`。

### 解法

#### 方法一：递归求深度并顺便更新直径
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

## [560] 和为 K 的子数组

- **题目来源**: LeetCode 第 560 题
- **难度**: Medium
- **标签**: `#数组` `#哈希表` `#前缀和`

### 题目描述

给定一个整数数组 `nums` 和一个整数 `k`，统计并返回和为 `k` 的连续子数组的个数。

### 思路

1. **核心思想**：利用前缀和，把“子数组和等于 k”转化为“两个前缀和之差等于 k”，并用哈希表记录前缀和出现的次数。
2. **思考过程**：暴力解需要枚举所有子数组，时间复杂度为 O(n^2)。对于每个前缀和 `sj`，只要之前出现过 `sj - k`，就说明中间这一段子数组的和为 k。
3. **关键点**：先统计 `sj - k` 的个数再加入当前 `sj`，保证使用当前元素之前的前缀和；空前缀和 0 要初始化为 1。

### 解法

#### 方法一：前缀和 + 哈希表
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
