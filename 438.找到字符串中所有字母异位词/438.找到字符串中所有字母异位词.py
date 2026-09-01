#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
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
# @lc code=end

