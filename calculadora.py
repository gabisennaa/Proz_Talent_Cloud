def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2  # Soma
    elif operacao == 2:
        return num1 - num2  # Subtração
    elif operacao == 3:
        return num1 * num2  # Multiplicação
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2  # Divisão
        else:
            return "Erro: Divisão por zero"  # Tratamento de divisão por zero
    else:
        return 0  # Operação inválida
