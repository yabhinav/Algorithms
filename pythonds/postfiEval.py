from basic.Stack import Stack


# Create an empty stack called operandStack. Convert the string to a list by
# using the string method split. Scan the token list from left to right.
# If the token is an operand, convert it from a string to an integer and push
# the value onto the operandStack.     If the token is an operator, *, /, +,
# or -, it will need two operands. Pop the operandStack twice. The first pop
# is the second operand and the second pop is the first operand. Perform the
# arithmetic operation. Push the result back on the operandStack. When the
# input expression has been completely processed, the result is on the stack.
# Pop the operandStack and return the value.
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if is_int(token) :
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return  False

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
print(postfixEval("12 8 + 3 2 + /"))
