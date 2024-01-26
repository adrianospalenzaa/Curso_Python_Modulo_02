# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica (*args): #posso receber quantos argumentos eu quiser
    total = 1
    for numero in args:
        total *= numero  # total = total * numero
    return total

numeros = 10, 2, 3, 4, 5

resultado = multiplica(*numeros)
print(resultado)

"------------------------------------------------------------"

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar (nun):
    if nun % 2 == 0:
        return (f'Numero {nun} e PAR')
    return (f'Nuemro {nun} e Impar')

print(par_impar(140))
print(par_impar(191))
print(par_impar(152))