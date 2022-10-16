import requests


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def find_name():
    '''Функция поиска имени по номеру документа'''
    number_ = input('Введите номер документа: ')
    result = 'Документ с таким номером не существует.'
    for doc in documents:
        if doc['number'] == number_:
            result = doc['name']
            break
    return result

def _get_input():
    '''В эту функцию вынесены все инпуты для функции add_file'''
    a = input("Введите тип документа: ")
    b = input("Введите номер документа: ")
    c = input("Введите имя: ")
    d = input("Введите номер полки: ")
    return [a, b, c, d]

def add_file(int_datas):
    '''Функция добавляющая новый файл'''
    type_doc = int_datas[0]
    num_doc = int_datas[1]
    name = int_datas[2]
    shelf = int_datas[3]
    if shelf in directories.keys():
        documents.append({"type": type_doc, "number": num_doc, "name": name})
        shelf_content = directories.get(shelf)
        shelf_content.append(num_doc)
    else:
        print('Указана несуществующая полка')
    return documents

def delete_file():
    '''Функция удаления файла'''
    num_doc = input('Введите номер документа: ').strip()
    count = 0
    for file in documents:
        if num_doc in file.values():
            documents.remove(file)
        else:
            count += 1
    for shelf in directories:
        if num_doc in directories.get(shelf):
            directories.get(shelf).remove(num_doc)
    return documents


with open("YANDEX_TOKEN.txt") as file_tok:
    ya_token = file_tok.read()


class YaDisk:
    def __init__(self):
        self.token = ya_token
        self.headers = {'Authorization': self.token}

    def create_folder(self, folder_name):
        """Создаём папку на Яндекс диск"""
        response = requests.get('https://yandex.ru/dev/disk/poligon')
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name}
        requests.put(url, headers=self.headers, params=params)
        return response.status_code

    def is_folder_in_directory(self, folder_name):
        '''Функция проверяющая наличие папки на Яндекс.Диске'''
        params = {'path': folder_name}
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        result = requests.get(url, headers=self.headers, params=params)
        if result.status_code == 200:
            return True
        else:
            return False



if __name__ == '__main__':

    print('Доступные команды:\np - поиск имени\na - добавить новый документ\nd - удалить документ из каталога')
    request = input('\nВыберите команду: ').strip()
    if request == 'p':
        find_name()
    elif request == 'a':
        input_datas = _get_input()
        add_file(input_datas)
    elif request == 'd':
        delete_file()
    else:
        print('Введена несуществующая команда')

    yadisk = YaDisk()
    yadisk.create_folder('Моя милая папочка')
    yadisk.is_folder_in_directory('Моя милая папочка')
