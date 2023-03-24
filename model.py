



notes_list = []

path = 'notes_list.txt'


def get_notes_list():
    global notes_list
    return notes_list

def get_notes(text: str):
    global notes_list
    result = []
    for i, notes in enumerate(notes_list):
        for field in notes:
            if text in field:
                result.append((notes, i))
    if len(result) >1: 
        return False
    else:
        return result

def open_file():
    global notes_list
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for notes in file:
        notes_list.append(notes.strip().split(';'))
    print(notes_list)


def save_file():
    global notes_list
    global path
    nl_str = []
    for notes in notes_list:
        nl_str.append(';'.join(notes))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(nl_str))



def add_new_notes(new_notes: list):
    global notes_list
    notes_list.append(new_notes)

def search_notes(find: str):
    global notes_list
    result = []
    for notes in notes_list:
        for field in notes:
            if find in field:
                result.append(notes)
                break
    return result


def delete_notes(notes: list):
    global notes_list
    notes_list.remove(notes)

def change_notes(index: int, new: list):
    global notes_list
    notes_list[index][0] = new[0] if new[0] != '' else notes_list[index][0]
    notes_list[index][1] = new[1] if new[1] != '' else notes_list[index][1]
    notes_list[index][2] = new[2] if new[2] != '' else notes_list[index][2]