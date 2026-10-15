"""Testes automatizados dos algoritmos de ordenação."""
import unittest
from ordenacao import insertion_sort, merge_sort


class TestOrdenacao(unittest.TestCase):
    def verificar_algoritmos(self, valores):
        esperado = sorted(valores)

        entrada_insercao = valores[:]
        resultado_insercao = insertion_sort(entrada_insercao)
        self.assertEqual(resultado_insercao, esperado)
        # Insertion Sort ordena a própria lista (in-place).
        self.assertIs(resultado_insercao, entrada_insercao)

        entrada_merge = valores[:]
        resultado_merge = merge_sort(entrada_merge)
        self.assertEqual(resultado_merge, esperado)
        # Merge Sort devolve uma lista ordenada sem alterar a entrada.
        self.assertEqual(entrada_merge, valores)
        self.assertIsNot(resultado_merge, entrada_merge)

    def test_lista_vazia(self):
        self.verificar_algoritmos([])

    def test_elemento_unico(self):
        self.verificar_algoritmos([7])

    def test_dois_elementos(self):
        self.verificar_algoritmos([2, 1])
        self.verificar_algoritmos([1, 2])

    def test_lista_aleatoria(self):
        self.verificar_algoritmos([8, 3, 5, 1, 9, 2])

    def test_lista_ja_ordenada(self):
        self.verificar_algoritmos([1, 2, 3, 4, 5])

    def test_lista_invertida(self):
        self.verificar_algoritmos([5, 4, 3, 2, 1])

    def test_elementos_iguais(self):
        self.verificar_algoritmos([4, 4, 4, 4])

    def test_duplicatas_e_negativos(self):
        self.verificar_algoritmos([0, -2, 5, -2, 3, 0])

    def test_lista_grande(self):
        self.verificar_algoritmos(list(range(1000, 0, -1)))


if __name__ == "__main__":
    unittest.main()
