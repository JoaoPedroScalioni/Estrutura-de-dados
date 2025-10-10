def h_index_linear(citacoes):
    h_index = 0
    for i, citacao in enumerate(citacoes):
        num_artigos = i + 1
        if citacao >= num_artigos:
            h_index = num_artigos
        else:
            break
    return h_index

def h_index_binaria(citacoes):
    n = len(citacoes)
    baixo, alto = 0, n - 1
    h_index = 0
    while baixo <= alto:
        meio = (baixo + alto) // 2
        num_artigos = meio + 1
        if citacoes[meio] >= num_artigos:
            h_index = num_artigos
            baixo = meio + 1
        else:
            alto = meio - 1
    return h_index

# --- Demonstração do Exercício 2 ---
if __name__ == "__main__":
    citacoes1 = [10, 8, 5, 4, 3]
    citacoes2 = [25, 8, 5, 3, 3]

    print("\n\n--- Exercício 2: Completo ---")
    
    # a) Busca Linear
    print("\n--- a) Usando Busca Linear ---")
    print(f"Citações: {citacoes1} -> Índice-H: {h_index_linear(citacoes1)}")
    print(f"Citações: {citacoes2} -> Índice-H: {h_index_linear(citacoes2)}")

    # b) Busca Binária
    print("\n--- b) Usando Busca Binária ---")
    print(f"Citações: {citacoes1} -> Índice-H: {h_index_binaria(citacoes1)}")
    print(f"Citações: {citacoes2} -> Índice-H: {h_index_binaria(citacoes2)}")