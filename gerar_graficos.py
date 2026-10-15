"""Gera gráficos a partir de dados.csv. Requer matplotlib."""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

PASTA = Path(__file__).with_name("graficos")
PASTA.mkdir(exist_ok=True)
dados = defaultdict(list)

with Path(__file__).with_name("dados.csv").open(encoding="utf-8", newline="") as f:
    for linha in csv.DictReader(f):
        dados[linha["algoritmo"]].append({
            "n": int(linha["n"]),
            "tempo": float(linha["tempo_medio_segundos"]),
            "comparacoes": float(linha["comparacoes_media"]),
        })

for campo, titulo, eixo_y, nome in [
    ("tempo", "Tempo médio de ordenação", "Tempo (segundos)", "tempos.png"),
    ("comparacoes", "Média de comparações entre elementos", "Comparações", "comparacoes.png"),
]:
    plt.figure(figsize=(9, 5.5))
    for algoritmo, linhas in dados.items():
        linhas = sorted(linhas, key=lambda x: x["n"])
        plt.plot([x["n"] for x in linhas], [x[campo] for x in linhas],
                 marker="o", label=algoritmo)
    plt.title(titulo)
    plt.xlabel("Tamanho da lista (n)")
    plt.ylabel(eixo_y)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PASTA / nome, dpi=160)
    plt.close()
print("Gráficos atualizados em graficos/")
