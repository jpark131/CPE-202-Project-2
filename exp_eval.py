from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass



def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    s = Stack(30)
    tokens = input_str.split( )
    operators = ['+', '-', '*', '/', '**', '<<', '>>']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for char in tokens:
        if char in operators:
            try:
                n2 = s.pop()
                n1 = s.pop()
            except IndexError:
                raise PostfixFormatException('Insufficient operands')
            if char == '+':
                result = n1 + n2
                s.push(result)
            if char == '-':
                result = n1 - n2
                s.push(result)
            if char == '*':
                result = n1 * n2
                s.push(result)
            if char == '/':
                if n2 == 0:
                    raise ValueError('Cannot divide by 0!')
                result = n1 / n2
                s.push(result)
            if char == '**':
                result = n1 ** n2
                s.push(result)
            if char == '<<':
                if type(n1) == float or type(n2) == float:
                    raise PostfixFormatException('Illegal bit shift operand')
                result = n1 << n2
                s.push(result)
            if char == '>>':
                if type(n1) == float or type(n2) == float:
                    raise PostfixFormatException('Illegal bit shift operand')
                result = n1 >> n2
                s.push(result)
        elif char[0] in nums:
            if '.' not in char:
                s.push(int(char))
            else:
                s.push(float(char))
        else:
            raise PostfixFormatException('Invalid token')
    final = s.pop()
    if not s.is_empty():
        raise PostfixFormatException('Too many operands')
    return final

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    s = Stack(30)
    post = ''
    tokens = input_str.split( )
    operators = ['+','-','*','/','^','<<','>>','**','**']
    highest = ['<<','>>']
    high = ['**']
    medium = ['*','/']
    low = ['+','-']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for char in tokens:
        if post == '' and char[0] in nums:
            post += char
        elif char[0] in nums:
            post += ' ' + char
        elif char == '(':
            s.push(char)
        if char in operators:
            if not s.is_empty():
                o2 = s.peek()
            if char in highest or char in high:
                if s.is_empty() or o2 == '(':
                    s.push(char)
                else:
                    while not s.is_empty() and o2 in highest:
                        post += ' ' + s.pop()
                    s.push(char)
            if char in medium:
                if s.is_empty() or o2 == '(':
                    s.push(char)
                else:
                    while not s.is_empty() and o2 not in low:
                        post += ' ' + s.pop()
                        if not s.is_empty():
                            o2 = s.peek()
                    s.push(char)
            if char in low:
                if s.is_empty() or o2 == '(':
                    s.push(char)
                else:
                    while not s.is_empty():
                        post += ' ' + s.pop()
                    s.push(char)
        if char == ')':
            o2 = s.peek()
            while o2 != '(':
                post += ' ' + s.pop()
                if not s.is_empty():
                        o2 = s.peek()
                s.pop()
    while not s.is_empty():
        post += ' ' + s.pop()
    return post

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    s = Stack(30)
    tokens = input_str.split( )
    i = len(tokens) - 1
    operators = ['+','-','*','/','<<','>>','**']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    while i >= 0:
        char = tokens[i]
        if char[0] in nums:
            s.push(char)
            i -= 1
        elif char in operators:
            op1 = s.pop()
            op2 = s.pop()
            inf = op1 + ' ' + op2 + ' ' + char
            s.push(inf)
            i -= 1
    return s.pop()
