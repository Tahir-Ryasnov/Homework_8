import unittest
from unittest.mock import patch
from main import find_name, add_file, delete_file, documents, YaDisk
from test_tools import tests_documents, tests_datas


yadisk = YaDisk()


class TestFunctions(unittest.TestCase):
    """Тест поиска имени по номеру документа"""
    @patch('builtins.input', return_value='11-2')
    def test_find_name(self, n):
        result = find_name()
        self.assertEqual(result, 'Геннадий Покемонов')

    '''Тест добавления новой папки'''
    def test_add_file(self):
        result = add_file(tests_datas)
        self.assertEqual(result, tests_documents)

    '''Тест удаления папки'''
    @patch('builtins.input', return_value='2')
    def test_delete_file(self, n):
        result = delete_file()
        self.assertEqual(result, documents)

    '''Тест создания папки на ЯндексДиске'''
    def test_create_folder_1(self):
        result = yadisk.create_folder('Моя милая папочка')
        self.assertEqual(result, 200)

    """Тест с ошибкой №1"""
    def test_create_folder_2(self):
        result = yadisk.create_folder('Моя милая папочка')
        self.assertEqual(result, 400)

    '''Тест с ошибкой №2'''
    def test_get_folder_info(self):
        result = yadisk.is_folder_in_directory('Моя милая папочка')
        self.assertFalse(result)
