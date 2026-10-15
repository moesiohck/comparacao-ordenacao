# Comparação de algoritmos de ordenação

Projeto da atividade de comparação entre **Insertion Sort**, **Merge Sort** e `sorted()` do Python.

## Arquivos

- `ordenacao.py`: implementa os dois algoritmos pedidos.
- `testes.py`: testa listas vazias, unitárias, aleatórias, ordenadas, invertidas, com duplicatas, valores negativos e listas maiores.
- `medir.py`: executa 10 medições para cada tamanho, calcula médias de tempo e comparações e grava `dados.csv`.
- `dados.csv`: resultados gerados pela execução de `medir.py`.
- `RELATORIO.md`: análise dos resultados e dos gráficos.
- `graficos/`: gráficos de tempo e de comparações.

## Como executar

Requer Python 3.9 ou superior. Os gráficos já estão incluídos no projeto. Para refazer os dados:

```bash
python testes.py
python medir.py
```

Para recriar os gráficos a partir do CSV, instale `matplotlib` e execute:

```bash
python gerar_graficos.py
```

Os tempos variam conforme o computador, a versão do Python e os processos em execução. Por isso, os valores do CSV são uma amostra experimental, não uma garantia para todas as máquinas.
