from CalculatorSupport import Stack, Operators


def stack_debug():
    print(f"expression_stack:{expression_stack.get_all()}\noperator:{operators}\noperands:{operands}\n")


expression_stack = Stack.ExpressionStack()
operators = Stack.OperatorStack(expression_stack)
operands = Stack.OperandStack(expression_stack)
stack_debug()
operators.push(Operators.Operator)
stack_debug()
operands.push(0)
stack_debug()
operators.push(Operators.Addition)
stack_debug()
operands.push(1)
stack_debug()
operators.pop()
stack_debug()
operands.pop()
stack_debug()
