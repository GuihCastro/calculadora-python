import re

DIGIT_OR_DOT_REGEX = re.compile(f'^[0-9.,]$')


def isEmpty(char: str) -> bool:
    return len(char) == 0


def isDigitOrDot(char: str) -> bool:
    return bool(DIGIT_OR_DOT_REGEX.search(char))


def isValidNumber(expression: str) -> bool:
    try:
        float(expression)
        return True
    except ValueError:
        print('Valor inválido.')
        return False
    
def isOperator(char: str) -> bool:
    return char.lower() in '+-**/x÷^'
