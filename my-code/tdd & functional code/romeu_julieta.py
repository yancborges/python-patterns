from unittest import TestCase, main
from app import romeu_julieta, romeus_julietas


class TesteRomeuEJulieta(TestCase):
    def teste_existe_romeu_e_julieta(self):
        romeu_julieta(0)

    def teste_rej_queijo(self):
        valores = [3, 6, 9]
        esperado = 'queijo'
        for valor in valores:
            with self.subTest(valor=valor):
                self.assertEqual(romeu_julieta(valor), esperado)

    def teste_rej_goiabada(self):
        valores = [5, 10, 20]
        esperado = 'goiabada'
        for valor in valores:
            with self.subTest(valor=valor):
                self.assertEqual(romeu_julieta(valor), esperado)

    def teste_rej_rej(self):
        valores = [15, 30, 45]
        esperado = 'romeu e julieta'
        for valor in valores:
            with self.subTest(valor=valor):
                self.assertEqual(romeu_julieta(valor), esperado)

    def teste_rej_lista(self):
        valores = [3, 5, 15]
        esperado = ['queijo', 'goiabada', 'romeu e julieta']
        self.assertEqual(romeus_julietas(valores), esperado)


main()