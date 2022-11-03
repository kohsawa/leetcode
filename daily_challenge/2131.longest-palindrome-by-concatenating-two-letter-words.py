#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        w_cnt: dict[str, int] = defaultdict(lambda:0)
        for w in words:
            w_cnt[w] += 1
        
        c = mirror = in_mid = 0
        ws = set(words)

        for w in ws:
            if w[0] == w[1]:
                if w_cnt[w] % 2 == 1:
                    in_mid = 1
                mirror += w_cnt[w] // 2
            elif w[::-1] in w_cnt and w_cnt[w[::-1]] > 0:
                c += min(w_cnt[w], w_cnt[w[::-1]])
                w_cnt[w] = w_cnt[w[::-1]] = 0

        return (c + mirror) * 4 + in_mid * 2
        
# @lc code=end

