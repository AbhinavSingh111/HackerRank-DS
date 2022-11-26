https://leetcode.com/problems/excel-sheet-column-number/submissions/

171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = dict(zip(letters, val))
        for ch in s:
            res = res * 26 + d[ch]
        return res
        
