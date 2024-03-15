## Infix to postfix

Procedure: 
1. Create a stack to store the operators.
2. Create a list to store the postfix expression.
3. For each token in the infix expression:
    1. If the token is an operand, append it to the postfix expression.
    2. If the token is an operator, pop all the operators from the stack that have higher or equal precedence than the token, and append them to the postfix expression. Then push the token to the stack.
4. Pop all the remaining operators from the stack and append them to the postfix expression.
    
    ```python
    def infix_to_postfix(infix):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        postfix = []
        for token in infix:
            if token.isalnum():
                postfix.append(token)
            elif token in precedence:
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    postfix.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
        while stack:
            postfix.append(stack.pop())
        return postfix
    ```

    ```python
    infix_to_postfix('a+b*c')
    # Output: ['a', 'b', 'c', '*', '+']
    ```

    ```python
    infix_to_postfix('(a+b)*c')
    # Output: ['a', 'b', '+', 'c', '*']
    ```

    ```python
    infix_to_postfix('a+b*c/d-e')
    # Output: ['a', 'b', 'c', '*', 'd', '/', '+', 'e', '-']
    ```

    ```python
    infix_to_postfix('a+b^c*d-e')

## postfix to infix

Procedure:

1. Create a stack to store the operands.
2. For each token in the postfix expression:
    1. If the token is an operand, push it to the stack.
    2. If the token is an operator, pop two operands from the stack, enclose them in parentheses, and append them to the stack.
3. The top of the stack will contain the infix expression.

    ```python
    def postfix_to_infix(postfix):
        stack = []
        for token in postfix:
            if token.isalnum():
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append('({}{}{})'.format(op1, token, op2))
        return stack[0]
    ```

    ```python
    postfix_to_infix(['a', 'b', 'c', '*', '+'])
    # Output: '(a+(b*c))'
    ```

    ```python
    postfix_to_infix(['a', 'b', '+', 'c', '*'])
    # Output: '((a+b)*c)'
    ```

    ```python
    postfix_to_infix(['a', 'b', 'c', '*', 'd', '/', '+', 'e', '-'])
    # Output: '((a+(b*c/d))-e)'
    ```

    ```python
    postfix_to_infix(['a', 'b', 'c', '^', 'd', '*', 'e', '-'])
    # Output: '(a-(b^c)*d)'
    ```

    ```python
    postfix_to_infix(['a', 'b', '+', 'c', 'd', '+', '*'])
    # Output: '((a+b)*(c+d))'
    ```

## postfix evaluation

Procedure:

1. Create a stack to store the operands.
2. For each token in the postfix expression:
    1. If the token is an operand, push it to the stack.
    2. If the token is an operator, pop two operands from the stack, apply the operator, and push the result back to the stack.
3. The top of the stack will contain the result of the expression.

    ```python
    def postfix_evaluation(postfix):
        stack = []
        for token in postfix:
            if token.isalnum():
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(op1 / op2)
                elif token == '^':
                    stack.append(op1 ** op2)
        return stack[0]
    ```

    ```python
    postfix_evaluation(['2', '3', '+', '5', '*'])
    # Output: 25
    ```

    ```python
    postfix_evaluation(['4', '2', '/', '5', '*'])
    # Output: 10
    ```

    ```python
    postfix_evaluation(['3', '4', '^', '5', '*'])
    # Output: 405
    ```

