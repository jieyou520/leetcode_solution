#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            seen[key].append(s)
        
        return list(seen.values())
              
# @lc code=end

