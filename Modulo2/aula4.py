# def saudacao():
#     print('Olá!')

# saudacao()

# def horario (hora):
#     if 1 < hora < 12:
#         return 'Bom dia'
#     elif 12 <= hora < 18:
#         return 'Boa tarde'
#     elif 18 <= hora < 23:
#         return 'Boa noite'
#     else:
#         return 'Hora não compatível'
# hora = int(input('Informe a hora (entre 1 e 23): '))
# mensagem = horario(hora)
# print(mensagem)



# def soma (numero1, numero2, resultado):
#     return f'A soma de {numero1} + {numero2} = {resultado}.'

# numero_1 = float(input('Digite o primeiro número: '))
# numero_2 = float(input('Digite o segundo número: '))
# resultado_exibido = numero_1 + numero_2
# operacao = soma(numero_1, numero_2, resultado_exibido)
# print(operacao)





def calculadora (numero1, numero2, resultado):
    return f' {numero1} {operacao} {numero2} = {resultado}.'

operacao = input('Informe qual a operação escolhida(+-*/): ')
numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
resultado_exibido_soma = numero_1 + numero_2
resultado_exibido_subtracao = numero_1 - numero_2
resultado_exibido_multiplicacao = numero_1 * numero_2
resultado_exibido_divisao = numero_1 / numero_2

if operacao == '+':
    print(calculadora(numero_1, numero_2 , resultado_exibido_soma))
elif operacao == '-':
    print(calculadora(numero_1, numero_2 , resultado_exibido_subtracao))
elif operacao == '*':
    print(calculadora(numero_1, numero_2 , resultado_exibido_multiplicacao))
elif operacao == '/':
    print(calculadora(numero_1, numero_2 , resultado_exibido_divisao))