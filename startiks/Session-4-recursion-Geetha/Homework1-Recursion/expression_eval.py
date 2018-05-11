# Complete the function below.

def generate_all_expressions(s, target):
    flist = gae(s, 0)
    results = []
    for i in flist:
        # get the expression evaluation
        print(i)
        fval = evalexp(i)
        if fval == target:
            # print ("Matched####")
            print(i)
            results.append(i)
            print("something")
    return (results)


def gae(s, start):
    if start == len(s):
        return [""]
    else:
        in_list = gae(s, start + 1)
        f_list = []
        for item in in_list:
            if start == 0:
                f_list.append(s[start] + item)
            else:
                f_list.append("" + s[start] + item)
                f_list.append("+" + s[start] + item)
                f_list.append("*" + s[start] + item)
        return (f_list)


# Two stack solution to evluate expressions
# precedence  if lower precedence comes after higher
# Perform higher precedence operation , push value result to operator and then push operand

def evalexp(exp):
    operator_stack = []
    operand_stack = []
    prevD = 0
    fval = 0
    # print ("eval_exp")
    for i in exp:
        if i == '+':
            if (prevD != 0):
                operator_stack.append(prevD)
                prevD = 0
            if (len(operand_stack) > 0):
                if operand_stack[len(operand_stack) - 1] == '*':
                    fval = int(operator_stack.pop()) * int(operator_stack.pop())
                    operator_stack.append(fval)
                else:
                    operand_stack.append('+')
            else:
                operand_stack.append('+')
        elif i == '*':
            if (prevD != 0):
                operator_stack.append(prevD)
                prevD = 0
            operand_stack.append('*')
        elif i.isdigit():
            prevD = prevD * 10 + int(i)
    operator_stack.append(prevD)
    # After complete stacks are made
    fval = 0
    # print ("eval_exp_end")
    # print (operand_stack)
    # print(operator_stack)
    while len(operand_stack) > 0:
        print(operator_stack)
        operand = operand_stack.pop()
        if operand == '+':
            fval = int(operator_stack.pop()) + int(operator_stack.pop())
            operator_stack.append(fval)
        if operand == '*':
            fval = int(operator_stack.pop()) * int(operator_stack.pop())
            operator_stack.append(fval)

    return operator_stack.pop()
