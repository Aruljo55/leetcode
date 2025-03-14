class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                sign = char
                num = 0
        return sum(stack)
