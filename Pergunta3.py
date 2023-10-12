'''Pergunta

3. Dado o array de números inteiros [1, 15, 2, 7, 2, 5, 7, 1, 4] crie uma função que recebe um argumento X e retorne true ou false 
caso haja no array uma combinação de soma entre dois números que resulte no input X. 
Exemplo: Se X=2, a função deve retornar true pois existem dois números 1 dentro do array 1+1 = 2. 
Caso X=1231 a função deve retornar false pois não existe uma combina de dois números capazes de somar 1231.
'''

arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
print(f'Array informado: {arr}')

valor = int(input('Informe um número: '))

a = False # Inicializa a variável "a" como False, será usada para indicar se uma combinação foi encontrada

for x in range(0, 9):
    for y in range(0, 9):
        if x != y and arr[x] + arr[y] == valor:   # Verifica se 'x' é diferente de 'y' e se a soma dos elementos nos índices x e y é igual a "valor"
            a = True  # Se encontrar uma combinação, define "a" como True
            break

print(a)