# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
            "I": 1,  "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        romans = roman_table.keys()
        sum = 0
        while s:
            for r in romans:
                if s.startswith(r):
                    sum += roman_table[r]
                    s = s[len(r):]
                    break
        return sum
