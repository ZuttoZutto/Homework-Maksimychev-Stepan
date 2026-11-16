def scatter(s):
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


def parse(tokens):
    pos = [0]

    def peek():
        return tokens[pos[0]] if pos[0] < len(tokens) else None

    def take():
        t = peek()
        pos[0] += 1
        return t

    def expr():
        node = term()
        while peek() in ('+', '-'):
            op = take()
            node = (op, node, term())
        return node

    def term():
        node = factor()
        while peek() in ('*', '/'):
            op = take()
            node = (op, node, factor())
        return node

    def factor():
        t = take()
        if t == '(':
            node = expr()
            take()
            return node
        return t

    node = expr()
    assert pos[0] == len(tokens)
    return node


def to_prefix(node):
    if isinstance(node, str):
        return node
    op, left, right = node
    return f"{op} {to_prefix(left)} {to_prefix(right)}"


def to_postfix(node):
    if isinstance(node, str):
        return node
    op, left, right = node
    return f"{to_postfix(left)} {to_postfix(right)} {op}"


def polish(s):
    tree = parse(scatter(s))
    return to_prefix(tree), to_postfix(tree)


print(polish("(3+4*(2-1))/5"))