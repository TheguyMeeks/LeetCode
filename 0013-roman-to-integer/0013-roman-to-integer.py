class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        subtractive_cases = {
            "IV": 4, "IX": 9,
            "XL": 40, "XC": 90,
            "CD": 400, "CM": 900,
        }

        roman_dict = {
            "I": 1, "V": 5,
            "X": 10, "L": 50,
            "C": 100, "D": 500,
            "M": 1000,
        }

        simple_s = s
        pair_list = []
        for char1, char2 in zip(s, s[1:]):
            pair = char1 + char2

            if pair in subtractive_cases:
                simple_s = simple_s.replace(pair, "")
                pair_list.append(pair)

        subtractive_list = [subtractive_cases[pair] for pair in pair_list]

        digits_list = [roman_dict[char] for char in simple_s]

        return sum(digits_list) + sum(subtractive_list)