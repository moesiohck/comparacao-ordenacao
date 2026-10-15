"""Algoritmos de ordenação por inserção e intercalação."""


def insertion_sort(lista):
    """Ordena a lista in-place por inserção e devolve a mesma lista."""
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def merge_sort(lista):
    """Devolve uma nova lista ordenada usando intercalação (Merge Sort)."""
    if len(lista) <= 1:
        return lista[:]

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
