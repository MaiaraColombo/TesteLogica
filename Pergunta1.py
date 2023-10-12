''' Pergunta
 1. Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda. 
 Os itens devem ser modificados no lugar, ou seja, você não ira trocar posições e sim colocar os números “1” no inicio do Array.
 [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21] '''



arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

resultado = [] # Números diferentes de "1" 
count = 0  # Caso encontre um número "1" serão incrementados nessa variável

 #Loop para percorrer o array original
for num in arr:
    if num == 1:
        count += 1
    else:
        resultado.append(num)

resultado = [1] * count + resultado  #Combina as duas partes do array, colocando os números "1" à esquerda



print("Números solicitados: ", arr)
print("Números ordenados conforme o solicitado: ", resultado)