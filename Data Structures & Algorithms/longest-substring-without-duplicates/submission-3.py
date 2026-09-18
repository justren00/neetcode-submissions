class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()

        left, right = 0, 0

        while right < len(s):
            if s[right] in chars:

                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1

            chars.add(s[right])
            right += 1

            res = max(res, right - left)

        return res
