'''Pergunta
4. Dado o array [9, 2, 3, 1, 4] encontre todos os números que estão faltando para completar o intervalo 0 a n, 
onde n é o maior número dentro do array. Adicione os números faltando dentro do array. '''


def range_completo(arr):
    if not arr: # Verifica se a lista está vazia.
        return [] # Retorna uma lista vazia se o array original também estiver vazio

    n = max(arr)  # Encontra o maior número no array
    for num in range(n + 1):
        if num not in arr:
            arr.append(num) # Adiciona os números que faltam ao array

arr = [9, 2, 3, 1, 4]
print("Array incompleto: ", arr)
range_completo(arr)
print("Array completo: ", arr)


