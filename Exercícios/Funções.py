# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica (*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

resultado = multiplica(*numeros)
print(resultado)

"------------------------------------------------------------"

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def numero (x, y):
    if x % y == 0:
        return ('Numero e PAR')
    else:
        return ('Nuemro e Impar')

resultado_2 = numero (11,2)
print(resultado_2)