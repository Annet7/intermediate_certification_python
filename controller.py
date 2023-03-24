import model
import view


def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_notes(model.get_notes_list())
            case 4:
                new_notes = list(view.create_new_note())
                model.add_new_notes(new_notes)
            case 5:
                del_name = view.select_notes('Введите удаляемую заметку: ')
                notes = model.get_notes(del_name)
                if notes:
                    confirm = view.delete_confirm(notes[0][0][0])
                    if confirm:
                        model.delete_notes(notes[0][0])
                elif notes ==[]:
                    view.empry_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_notes('Введите изменяемую заметку: ')
                notes = model.get_notes(name)
                if notes:
                    changed_notes = view.change_notes()
                    model.change_notes(notes[0][1], list(changed_notes))
                elif notes ==[]:
                    view.empry_request()
                else:
                    view.many_request()
            case 7:
                find = view.find_notes()
                result = model.search_notes(find)
                view.show_notes(result)
            case _:
                view.input_error()
        
        