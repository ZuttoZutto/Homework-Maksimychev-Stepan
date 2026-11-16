def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c.isdigit() or c == '.':
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                j += 1
            tokens.append(s[i:j])
            i = j
        elif c.isalpha():
            j = i
            while j < len(s) and s[j].isalnum():
                j += 1
            tokens.append(s[i:j])
            i = j
        else:
            tokens.append(c)
            i += 1
    return tokens


PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}


def to_rpn(expr):
    tokens = tokenize(expr)
    output = []
    stack = []

    for token in tokens:
        if token[0].isdigit() or token[0] == '.' or token[0].isalpha():
            output.append(token)
        elif token in PRECEDENCE:
            while (stack
                   and stack[-1] in PRECEDENCE
                   and PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                return "Ошибка: несбалансированные скобки"
            stack.pop()
        else:
            return f"Ошибка: неизвестный токен '{token}'"

    while stack:
        op = stack.pop()
        if op == '(':
            return "Ошибка: несбалансированные скобки"
        output.append(op)

    return ' '.join(output)


print(to_rpn("(3+4*(2-1))/5"))