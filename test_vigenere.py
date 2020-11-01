import unittest
from vigenere import vigenere

class TestVigenere(unittest.TestCase):

    def test_vigenere(self):
        expected = [
                ('ce message', 'cle', True, 'fq pqxvmlh'),
                ('fq pqxvmlh', 'CLE', False, 'ce message'),
                ('une charogne', 'baudelaire', True, 'woz htbaglpf'),
                ("Rappelez-vous l'objet", 'Charles', True, "Uiqhqqxc-wggx o'ptvjm"),
                ('que nous vîmes', 'baudelaire', True, 'svz savb aînzw')
            ]
        for *args, result in expected:
            self.assertEqual(vigenere(*args), result)

if __name__ == '__main__':
    unittest.main()
