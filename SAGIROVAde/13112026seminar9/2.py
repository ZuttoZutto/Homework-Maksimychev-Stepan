def rpn_calculator(expr: str):
    tokens = expr.split()
    if not tokens:
        return "Ошибка: пустое выражение"

    stack = []

    for token in tokens:
        try:
            num = float(token)
            stack.append(num)
            continue
        except ValueError:
            pass

        if token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                return f"Ошибка: для оператора '{token}' недостаточно операндов"
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                if right == 0:
                    return "Ошибка: деление на ноль"
                result = left / right
            stack.append(result)
        else:
            return f"Ошибка: неизвестный токен '{token}'"

    if len(stack) == 1:
        return stack[0]
    elif len(stack) == 0:
        return "Ошибка: выражение не содержит значений"
    else:
        return f"Ошибка: в стеке осталось {len(stack)} значений, ожидалось одно"


result = rpn_calculator("3 4 2 1 - * + 5 /")
print(result)