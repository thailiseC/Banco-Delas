import unittest
from banco_delas import Banco_Delas
from banco_delas import Conta_corrente

class TestClass(unittest.TestCase):
    def test_buscar_conta(self):
        conta = Conta_corrente(10001)
        conta2 = Conta_corrente(1234)
        novo_banco = Banco_Delas()
        novo_banco.contas_abertas.append(conta)
        novo_banco.contas_abertas.append(conta2)
        print(novo_banco.contas_abertas)
        self.assertEqual(novo_banco.contas_abertas[1], novo_banco.buscar_conta(1234), 'o teste deu ruim')
        print('O teste deu bom!')
        print(novo_banco.contas_abertas[1])

if __name__ == "__main__":
    unittest.main()