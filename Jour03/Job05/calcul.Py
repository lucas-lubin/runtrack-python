def calcul(a, b, c):
    num1 = a
    operator = b
    num2 = c

    if operator == '+':
        resultat = num1 + num2

    elif operator == '-':
        resultat = num1 - num2
    
    elif operator == '*':
        resultat = num1 * num2
    
    elif operator == '/':
        if num2 != 0:
            resultat = num1 / num2
        else:
            return "c'est pas bon parce que c'est 0, recommence"
    elif operator == '%':
        resultat = num1 % num2
    else:
        return "opération est nulle, va te changer"

    return resultat

print(calcul(15, '+', 7))