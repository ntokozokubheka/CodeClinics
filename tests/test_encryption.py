import unittest
from unittest.mock import patch, MagicMock
from src.authentification.encryption import *
import src.authentification.encryption


class TestEncryptionFunctions(unittest.TestCase):

    @patch('builtins.open', create=True)
    def test_load_key_from_file(self, mock_open):

        mock_file = MagicMock()
        mock_file.read.return_value = b'some_key'
        mock_open.return_value.__enter__.return_value = mock_file

        key = load_key_from_file()

        self.assertEqual(key, b'some_key')

    @patch('builtins.open', create=True)
    def test_save_key_to_file(self, mock_open):

        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file

        save_key_to_file(b'some_key')

        mock_file.write.assert_called_once_with(b'some_key')

    def test_generate_key(self):

        key = generate_key()

        self.assertTrue(isinstance(key, bytes))

    def test_has_encrypt_value_function(self):

        self.assertTrue(
            hasattr(src.authentification.encryption, 'encrypt_value'))

    def test_has_decrypt_value_function(self):
        self.assertTrue(
            hasattr(src.authentification.encryption, 'decrypt_value'))


if __name__ == '__main__':
    unittest.main()