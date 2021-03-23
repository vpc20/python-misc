roman_nums = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))


class RomanNumerals:

    @staticmethod
    def to_roman(n):
        roman_numeral = ''
        for roman, integer in roman_nums:
            while n >= integer:
                roman_numeral += roman
                n -= integer
        return roman_numeral

    @staticmethod
    def from_roman(s):
        n = 0
        i = 0
        for roman, integer in roman_nums:
            while s[i:i + len(roman)] == roman:
                n += integer
                i += len(roman)
        return n

# def intToRoman(n): # less efficient version
#     result = ''
#     while n > 0:
#         for roman, num in roman_nums:
#             while n >= num:
#                 result += roman
#                 n -= num
#     return result

r = RomanNumerals()
print(RomanNumerals.to_roman(1985))
print(RomanNumerals.from_roman('MCM'))
