class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        if not s:
            return NestedInteger()

        if s[0] != '[':  # Base case: single integer
            return NestedInteger(int(s))

        stack = []
        num = None
        negative = False

        for char in s:
            if char == '-':
                negative = True
            elif char.isdigit():
                if num is None:
                    num = 0
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(NestedInteger())
            elif char == ',' or char == ']':
                if num is not None:
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                    num = None
                    negative = False
                if char == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]
