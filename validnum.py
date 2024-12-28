class Solution:
    def isNumber(self, s):
        import re
        # Define the regex for a valid number
        valid_number = re.compile(
            r"^[+-]?("  # Optional sign
            r"(\d+(\.\d*)?)|"  # Digits optionally followed by '.' and more digits
            r"(\.\d+)"  # Or '.' followed by digits
            r")([eE][+-]?\d+)?$"  # Optional exponent
        )
        # Check if the string matches the regex
        return bool(valid_number.match(s))
