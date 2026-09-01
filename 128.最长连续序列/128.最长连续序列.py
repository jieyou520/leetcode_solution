#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
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

          
# @lc code=end

