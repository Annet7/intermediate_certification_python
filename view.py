
commands = ['Открыть файл', 
            'Сохранить файл', 
            'Показать все заметки', 
            'Создать заметку', 
            'Удалить заметку', 
            'Изменить заметку', 
            'Найти заметку', 
            'Выход из программы']


def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(F'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('Введите число от 1 до 8')
        except ValueError:
            print('Введите число от 1 до 8')

def show_notes(notes_list: list):
    if len(notes_list) <1:
        print('Заметки пусты или не открыты')
    else:
        for i, notes in enumerate(notes_list, 1):
            print(f'\t{i}. {notes[0]:10} {notes[1]:50} {notes[2]:300}')



def input_error():
    print('Некорректный ввод. Введите корректный пункт меню. ')

def empry_request():
    print('Заметка не найдена.')

def many_request():
    print('Введите более точные данные. Найдено более одной заметки.')



def create_new_note():
    id = input('Введите идентификатор: ')
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    return id, head, body

def find_notes():
    find = input('Введите искомый эллемент: ')
    return find

def select_notes(notes: str):
    notes = input(notes)
    return notes

def change_notes():
    print('Введите новые данные. Если изменения не требуются, нажмите Enter')
    id = input('Введите идентификатор: ')
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    return id, head, body


def delete_confirm(note: str):
    result =input(f'Вы действительно хотите удалить заметку {note}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False