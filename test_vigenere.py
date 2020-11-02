import unittest
from vigenere import vigenere
from testing_utils import BaseTestCase


class TestVigenere(BaseTestCase):

    def test_vigenere(self):
        test_cases = [
            ('ce message', 'cle', True, 'fq pqxvmlh'),
            ('fq pqxvmlh', 'CLE', False, 'ce message'),
            ('une charogne', 'baudelaire', True, 'woz htbaglpf'),
            ("Rappelez-vous l'objet", 'Charles', True, "Uiqhqqxc-wggx o'ptvjm"),
            ('que nous vîmes', 'baudelaire', True, 'svz savb aînzw')
        ]
        self.run_tests(test_cases, vigenere)

    def ok_message(self, args, expected):
        decode_encode = "encoding" if args[2] else "decoding"
        print(
            f"OK    : {decode_encode} \"{args[0]}\" with key \"{args[1]}\", "
            f"result is \"{expected}\"")

    def error_message(self, args, expected, result):
        decode_encode = "encoding" if args[2] else "decoding"
        print(
            f"ERROR : {decode_encode} \"{args[0]}\" with key \"{args[1]}\", "
            f"result should be \"{expected}\" but was \"{result}\"")


if __name__ == '__main__':
    unittest.main()
