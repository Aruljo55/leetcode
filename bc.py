class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0  # For the current result
        sign = 1    # 1 means positive, -1 means negative

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * operand
                operand = 0
                result *= stack.pop()  # sign before parenthesis
                result += stack.pop()  # result calculated before parenthesis

        return result + sign * operand
