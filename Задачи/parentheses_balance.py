# Функция принимает строку и выводит True, если баланс скобок соблюден, иначе выводится False
def parentheses_balance(a: str) -> bool:
    count = 0
    for i in range(len(a)):
        if a[i] == "(":
            count += 1
        if a[i] == ")":
            if count == 0:
                return False
            count -= 1

    return count == 0


assert (parentheses_balance("()") is True)
assert (parentheses_balance("()(") is False)
assert (parentheses_balance("())") is False)
assert (parentheses_balance("(())()") is True)
assert (parentheses_balance("(()())()") is True)
assert (parentheses_balance("((())") is False)
assert (parentheses_balance(")()") is False)
assert (parentheses_balance("(") is False)
assert (parentheses_balance(")") is False)


