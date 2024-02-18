import csv
import os
import datetime

NOTES_FILE = 'notes.csv'

def create_note(note_id, title, body):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'id': note_id, 'title': title, 'body': body, 'timestamp': timestamp}

def save_notes(notes):
    with open(NOTES_FILE, 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for note in notes:
            writer.writerow(note)

def load_notes():
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                notes.append(row)
    return notes

def add_note(notes, title, body):
    if notes:
        last_id = int(notes[-1]['id'])
    else:
        last_id = 0
    new_note = create_note(last_id + 1, title, body)
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def edit_note(notes, note_id, title, body):
    for note in notes:
        if int(note['id']) == note_id:
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным идентификатором не найдена.")

def delete_note(notes, note_id):
    for note in notes:
        if int(note['id']) == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным идентификатором не найдена.")

def print_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}, Дата/время: {note['timestamp']}")

def main():
    notes = load_notes()
    while True:
        print("\nМеню:")
        print("1. Показать все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать существующую заметку")
        print("4. Удалить существующую заметку")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == '1':
            print_notes(notes)
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(notes, title, body)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            edit_note(notes, note_id, title, body)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(notes, note_id)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()
