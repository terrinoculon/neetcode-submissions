class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for val in tokens:
            if val not in ops:
                stack.append(int(val))
            else:
                opr2 = stack.pop()
                opr1 = stack.pop()
                if val == "+":
                    stack.append(opr1+opr2)
                elif val == "-":
                    stack.append(opr1-opr2)
                elif val == "*":
                    stack.append(opr1*opr2)
                elif val == "/":
                    stack.append(int((opr1/opr2)))
        return stack[0]