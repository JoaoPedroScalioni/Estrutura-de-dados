def quicksort(arr, baixo, alto):
    if baixo < alto:
        pi = particao(arr, baixo, alto)
        quicksort(arr, baixo, pi - 1)
        quicksort(arr, pi + 1, alto)

def particao(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def busca_linear_para_insercao(arr, alvo):
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i
        if arr[i] > alvo:
            return i
    return len(arr)

def busca_binaria_para_insercao(arr, alvo):
    baixo, alto = 0, len(arr) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return baixo

# --- Demonstração ---
if __name__ == "__main__":
    arr_desordenado = [10, 7, 8, 9, 1, 5, 12, 3]
    alvo_existente = 7
    alvo_inexistente = 6

    print("--- Exercício 1: Completo ---")
    print(f"Array original: {arr_desordenado}")

    quicksort(arr_desordenado, 0, len(arr_desordenado) - 1)
    arr_ordenado = arr_desordenado
    print(f"Array ordenado: {arr_ordenado}\n")

    # a) Busca Linear
    print("--- a) Usando Busca Linear ---")
    indice_linear_existente = busca_linear_para_insercao(arr_ordenado, alvo_existente)
    print(f"Buscando pelo alvo {alvo_existente}: Índice {indice_linear_existente}")

    indice_linear_inexistente = busca_linear_para_insercao(arr_ordenado, alvo_inexistente)
    print(f"Buscando pelo alvo {alvo_inexistente}: Índice de inserção {indice_linear_inexistente}\n")

    # b) Busca Binária
    print("--- b) Usando Busca Binária ---")
    indice_binario_existente = busca_binaria_para_insercao(arr_ordenado, alvo_existente)
    print(f"Buscando pelo alvo {alvo_existente}: Índice {indice_binario_existente}")

    indice_binario_inexistente = busca_binaria_para_insercao(arr_ordenado, alvo_inexistente)
    print(f"Buscando pelo alvo {alvo_inexistente}: Índice de inserção {indice_binario_inexistente}")