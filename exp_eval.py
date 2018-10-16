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
    tokens = input_str.split()
    result = ''
    operators = ['+', '-', '*', '/', '**', '<<', '>>']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    i = 0
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
    i = 0
    post = ''
    operators = ['+','-','*','/','^','<<','>>','**','**']
    highest = ['<<','>>']
    high = ['**']
    medium = ['*','/']
    low = ['+','-']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    while i < len(input_str):
        char = input_str[i]
        if char == ' ':
            i += 1
        elif post == '' and char in nums:
            post += char
            i += 1
        elif char in nums:
            post += ' ' + char
            i += 1
        elif char == '(':
            s.push(char)
            i += 1
        elif s.is_empty() and char == '<':
            s.push('<<')
            i += 2
        elif s.is_empty() and char == '>':
            s.push('>>')
            i += 2
        elif s.is_empty() and char == '*' and input_str[i + 1] == '*':
            s.push('**')
            i += 2
        elif s.is_empty():
            s.push(char)
            i += 1
        elif char == ')':
            if s.peek() != '(':
                while s.peek() != '(' and not s.is_empty():
                    post += " " + s.pop()
            s.pop()
            i += 1
        elif char == '<':
            o2 = s.peek()
            if o2 in highest and not s.is_empty():
                post += " " + s.pop()
            s.push('<<')
            i += 2
        elif char == '>':
            o2 = s.peek()
            if o2 in highest and not s.is_empty():
                post += " " + s.pop()
            s.push('>>')
            i += 2
        elif char == '*':
            if input_str[i + 1] == '*':
                o2 = s.peek()
                if o2 in highest:
                    post += " " + s.pop()
                s.push('**')
                i += 2
            else:
                o2 = s.peek()
                if o2 in highest or o2 in high or o2 in medium:
                    post += " " + s.pop()
                s.push(char)
                i += 1
        elif char == '/':
            o2 = s.peek()
            if o2 in highest or o2 in high or o2 in medium and not s.is_empty():
                post += " " + s.pop()
            s.push(char)
            i += 1
        elif char in low:
            o2 = s.peek()
            if o2 in highest or o2 in high or o2 in medium or o2 in low and not s.is_empty():
                post += " " + s.pop()
            s.push(char)
            i += 1
    while not s.is_empty():
        post += " " + s.pop()
    return post

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    s = Stack(30)
    i = len(input_str) - 1
    inf = ''
    operators = ['+','-','*','/','<','>','**','**']
    highest = ['<','>']
    high = ['**']
    medium = ['*','/']
    low = ['+','-']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    while i >= 0:
        char = input_str[i]
        if char == ' ':
            i -= 1
        elif char in nums:
            s.push(char)
            i -= 1
        elif char in operators:
            if char == '*':
                if i > 0:
                    if input_str[i - 1] == '*':
                        op1 = s.pop()
                        op2 = s.pop()
                        inf = op1 + ' ' + op2 + ' ' + '**'
                        s.push(inf)
                        i -= 2
                else:
                    op1 = s.pop()
                    op2 = s.pop()
                    inf = op1 + ' ' + op2 + ' ' + char
                    s.push(inf)
                    i -= 1
            elif char == '<' or char == '>':
                op1 = s.pop()
                op2 = s.pop()
                inf = op1 + ' ' + op2 + ' ' + input_str[i-1] + char
                s.push(inf)
                i -= 2
            else:
                op1 = s.pop()
                op2 = s.pop()
                inf = op1 + ' ' + op2 + ' ' + char
                s.push(inf)
                i -= 1
    return s.pop()
