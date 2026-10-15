"""Mede tempo e quantidade de comparações dos algoritmos."""
import csv
import random
import statistics
import time
from pathlib import Path

from ordenacao import insertion_sort, merge_sort

TAMANHOS = [10, 20, 50, 75, 100, 200, 500, 1000]
REPETICOES = 10
SEMENTE = 2026
ARQUIVO_CSV = Path(__file__).with_name("dados.csv")


class ValorContado:
    """Valor que conta comparações feitas pelos operadores de comparação."""
    total_comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def zerar_contador(cls):
        cls.total_comparacoes = 0

    def __lt__(self, outro):
        type(self).total_comparacoes += 1
        return self.valor < outro.valor

    def __le__(self, outro):
        type(self).total_comparacoes += 1
        return self.valor <= outro.valor

    def __gt__(self, outro):
        type(self).total_comparacoes += 1
        return self.valor > outro.valor


def medir_uma_vez(algoritmo, valores):
    """Retorna (tempo em segundos, comparações) para uma execução."""
    objetos = [ValorContado(v) for v in valores]
    ValorContado.zerar_contador()
    inicio = time.perf_counter()
    if algoritmo == "Insertion Sort":
        resultado = insertion_sort(objetos)
    elif algoritmo == "Merge Sort":
        resultado = merge_sort(objetos)
    elif algoritmo == "sorted()":
        resultado = sorted(objetos)
    else:
        raise ValueError(f"Algoritmo desconhecido: {algoritmo}")
    duracao = time.perf_counter() - inicio
    comparacoes = ValorContado.total_comparacoes
    # Confere que o resultado foi realmente ordenado.
    assert [x.valor for x in resultado] == sorted(valores)
    return duracao, comparacoes


def main():
    rng = random.Random(SEMENTE)
    linhas = []
    algoritmos = ["Insertion Sort", "Merge Sort", "sorted()"]

    for n in TAMANHOS:
        tempos = {alg: [] for alg in algoritmos}
        comparacoes = {alg: [] for alg in algoritmos}
        for _ in range(REPETICOES):
            valores = [rng.randint(0, 10_000) for _ in range(n)]
            # Usa a mesma entrada em cada algoritmo para a comparação ser justa.
            for algoritmo in algoritmos:
                tempo, qtd = medir_uma_vez(algoritmo, valores)
                tempos[algoritmo].append(tempo)
                comparacoes[algoritmo].append(qtd)

        for algoritmo in algoritmos:
            linhas.append({
                "n": n,
                "algoritmo": algoritmo,
                "repeticoes": REPETICOES,
                "tempo_medio_segundos": f"{statistics.mean(tempos[algoritmo]):.10f}",
                "comparacoes_media": f"{statistics.mean(comparacoes[algoritmo]):.2f}",
            })
        print(f"n={n}: medições concluídas")

    with ARQUIVO_CSV.open("w", newline="", encoding="utf-8") as arquivo:
        campos = ["n", "algoritmo", "repeticoes", "tempo_medio_segundos", "comparacoes_media"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)

    print(f"Dados salvos em {ARQUIVO_CSV}")


if __name__ == "__main__":
    main()
