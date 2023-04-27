import csv
import datetime
import os

count = 1

def get_id():
    global count
    count += 1

def create_note(notes):
    """Создание заметки"""
    global count
    for note in notes:
        if int(note[0]) == count:
            get_id()
        else:
            break

    note_id = count
    count = 1

    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.datetime.now()
    return [note_id, title, body, date, date]

def save_notes(notes):
    """Сохранение заметок в CSV-файл"""
    with open("notes.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(notes)

def load_notes(filter_date=None):
    """Загрузка заметок из CSV-файла"""
    if not os.path.exists("notes.csv"):
        return []
    with open("notes.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        return list(reader)

def display_notes(notes):
    """Отображение заметок"""
    if not notes:
        print("Заметок пока нет")
        return
    
    sorted_notes = sorted(notes, key=lambda x: x[4], reverse=True)
    print("{:<10} {:<30} {:<30} {:<30} {:<30}".format("ID", "Заголовок", "Текст", "Дата создания", "Дата изменения"))
    
    for note in sorted_notes:
        note_id, title, body, created_at, updated_at = note
        print("{:<10} {:<30} {:<30} {:<30} {:<30}".format(note_id, title, body, created_at, updated_at))

def find_note_by_id(notes, note_id):
    """Поиск заметки по ID"""
    for note in notes:
        if int(note[0]) == note_id:
            return note
    return None

def add_note():
    """Добавление заметки"""
    notes = load_notes()
    note = create_note(load_notes())
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена")

def delete_note():
    notes = load_notes()
    id = int(input('Введите идентификатор заметки: '))
    try:
        del notes[id - 1]
        save_notes(notes)
        print(f'Заметка с идентификатором {id} удалена.')
    except:
        print(f"Заметки с индентификатором {id} не найдена")

def edit_note():
    """Редактирование заметки"""
    notes = load_notes()
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    note = find_note_by_id(notes, note_id)
    if note is None:
        print("Заметка с ID {} не найдена".format(note_id))
        return
    title = input("Введите новый заголовок заметки (старый заголовок: {}): ".format(note[1]))
    body = input("Введите новый текст заметки (старый текст: {}): ".format(note[2]))
    updated_note = [note_id, title or note[1], body or note[2], note[3], datetime.datetime.now()]
    notes[notes.index(note)] = updated_note
    save_notes(notes)