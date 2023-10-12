'''Pergunta 
2. Dada a seguinte arvore binária de palavras, faça uma função que busque nessa arvore pela palavra-chave. 
O output da sua função deve ser o caminho até chegar no item procurado. 
Por exemplo, se o input de buscar for “goiaba” o output deve ser uma string “Maça -> morango -> Goiaba”.'''

class Node: # Representa um nó
    def __init__(self, data):
        self.data = data
        self.left = None  # Nó filho esqueda
        self.right = None  # Nó filho direita

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node


# Função para encontrar o caminho da raiz a um nó específico
def caminho(raiz, fruta_alvo, caminho_atual=[]):
    if raiz is None:
        return None
    caminho_atual.append(raiz.data)
    
    if raiz.data == fruta_alvo:
        return caminho_atual
    
    # Procura nos ramos esquerdo e direito
    caminho_esquerda = caminho(raiz.left, fruta_alvo, caminho_atual.copy())
    if caminho_esquerda:
        return caminho_esquerda
    
    caminho_direita = caminho(raiz.right, fruta_alvo, caminho_atual.copy())
    if caminho_direita:
        return caminho_direita
    
    return None

 # Cria a árvore binária com as frutas
if __name__ == '__main__':
    tree = BinaryTree('Maça')
    tree.root.left = Node('Morango')
    tree.root.left.left = Node('Goiaba')
    tree.root.left.right = Node('Limão')
    tree.root.right = Node('Pera')
    tree.root.right.left = Node('Abacaxi')
    tree.root.right.left.left = Node('Laranja')
    tree.root.right.left.left.left = Node('Banana')
    tree.root.right.left.left.right = Node('Cebola')

# Mapeia as frutas para os nós correspondentes
mapeamento_de_frutas = {
    'Maça': tree.root,
    'Morango': tree.root.left,
    'Goiaba': tree.root.left.left,
    'Limão': tree.root.left.right,
    'Pera': tree.root.right,
    'Abacaxi': tree.root.right.left,
    'Laranja': tree.root.right.left.left,
    'Banana': tree.root.right.left.left.left,
    'Cebola': tree.root.right.left.left.right
}

while True:
    print()
    print("Maça, Morango, Goiaba, Limão, Pera, Abacaxi, Laranja, Banana, Cebola")
    nome_da_fruta = input("Informe o nome da fruta que deseja (ou 'Sair' para sair): ")

    if nome_da_fruta == 'Sair':
        break

    if nome_da_fruta in mapeamento_de_frutas:
        nó_selecionado = mapeamento_de_frutas[nome_da_fruta]

        # Encontra o caminho da raiz à fruta selecionada
        caminho = caminho(tree.root, nome_da_fruta, [])
        
        if caminho:
            print("Caminho para a fruta: ")
            print(' => '.join(caminho))
        else:
            print('Não foi possível encontrar um caminho.')
    else:
        print('Fruta não encontrada. Tente novamente.')

        