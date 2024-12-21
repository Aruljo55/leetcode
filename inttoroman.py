class Solution:
    def intToRoman(self, num):
        # List of Roman numerals and their corresponding values
        roman_numerals = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]
        
        result = []
        
        # Iterate over the roman_numerals list
        for symbol, value in roman_numerals:
            # Find how many times the current Roman numeral value can fit into num
            while num >= value:
                result.append(symbol)  # Append the corresponding Roman numeral
                num -= value  # Subtract the value from num
        
        # Return the result as a joined string
        return ''.join(result)
