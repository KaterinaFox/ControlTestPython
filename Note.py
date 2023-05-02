import csv
import datetime
import os


file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = f"{file_dir}/note_book.csv"
if not os.path.exists(file_name):
    with open(file_name, 'w', newline='', encoding='utf8') as data:
        filewriter = csv.writer(data, delimiter=';')
headersCSV = ['ID', 'Title', 'Content', 'Date_Time']

def view_notes():
    with open(file_name, 'r', encoding='utf8') as data:
        notes =csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
        print(*headersCSV, sep = "\t")
        for line in notes:
            for v in line.values():
                print(f"{v}\t", end ="")
            print()
   
   

def add_notes():
    with open(file_name, "r", newline='', encoding="utf8") as data:
        old_notes = csv.DictReader(data, delimiter=';', fieldnames=['ID'])
        max_id = None
        for note in old_notes:
            if note['ID'] == '' or not note['ID'].isdigit():
                continue
            if max_id is None or int(note['ID']) > max_id:
                max_id = int(note['ID'])
        if max_id is None:
            max_id = 1
        else:
            max_id += 1
    with open(file_name, "a", newline='', encoding="utf8") as data:
        title = input('Введите название заметки: ')
        new_content = input('Введите текст заметки: ')
        dt = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        note_data = {'ID':max_id, 'Title': title, 'Content': new_content, 'Date_Time': dt}
        new_note = csv.DictWriter(data, delimiter=';', fieldnames=headersCSV)
        new_note.writerow(note_data)
        print('Заметка добавлена.')
    
              
def change_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    new_note = None
    is_change = False
    old_notes = []
    with open(file_name, "r", newline='', encoding="utf8") as data:
        notes = csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
        for note in notes:
            if  int(note['ID']) == note_id:
                is_change = True
                new_title = input('Введите новый заголовок заметки: ')
                new_content = input('Введите новый текст заметки: ')
                dt = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                new_note = {'ID':note_id, 'Title': new_title, 'Content': new_content, 'Date_Time': dt}
            else:
                old_notes.append(note)
    if is_change:
        if new_note is not None:
            old_notes.append(new_note)
            with open(file_name, "w", newline='', encoding="utf8") as data:
                writer = csv.DictWriter(data, delimiter=';', fieldnames=headersCSV)
                for note in old_notes:
                    writer.writerow(note)
                print('Заметка отредактирована.')
    else:
        print('Заметка с таким ID не найдена.')


def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    old_notes = []
    is_delete = False
    with open(file_name, "r", newline='', encoding="utf8") as data:
        notes = csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
        for note in notes:
            if  int(note['ID']) == note_id:
                is_delete = True
                continue
            else:
                old_notes.append(note)
    if is_delete:
        with open(file_name, "w", newline='', encoding="utf8") as data:
                writer = csv.DictWriter(data, delimiter=';', fieldnames=headersCSV)
                for note in old_notes:
                    writer.writerow(note)
                print('Заметка удалена.')
    else:
        print('Заметка с таким ID не найдена')
    
def find_note_id():
    note_id = int(input('Введите ID заметки: '))
    with open(file_name, "r", newline='', encoding="utf8") as data:
        notes = csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
        for note in notes:
            if  int(note['ID']) == note_id:
                print(*headersCSV, sep = "\t")
                for value in note.values():
                    print(f"{value} ", end="")
                break
        else:
            print("Заметка с таким ID не найдена")

def find_note_date():
    try:
        date_note = str(input('Введите дату заметки (дд-мм-гггг): '))
        date_note_obj = datetime.datetime.strptime(date_note, '%d-%m-%Y')
        date_note = date_note_obj.date()
        with open(file_name, "r", newline='', encoding="utf8") as data:
            notes = csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
            for note in notes:
                temp = str(note['Date_Time'])
                temp = datetime.datetime.strptime(temp, '%d-%m-%Y %H:%M:%S')
                temp = temp.date()
                if  temp == date_note:
                    for value in note.values():
                        print(f"{value} ", end="")
                    print()
                else:
                    print(f"Заметок от {date_note} не найдено")
                    break
    except ValueError as ex: 
        print("Неверно введена дата ", ex)
            
def main_menu():
    while True:
        num = int(input('\n \n Введите: 1 - просмотр блокнота; 2 - поиск заметки по ID;'
            ' 3 - поиск заметки по дате; 4 - добавить заметку; 5 - изменить заметку;'
            ' 6 - удалить заметку; 7 - выйти из программы: \n'))
        if num == 1:
            view_notes()
        elif num == 2: 
            find_note_id()
        elif num == 3: 
            find_note_date()
        elif num == 4: 
            add_notes()
        elif num == 5:
            change_note()
        elif num == 6:
            delete_note()
        elif num == 7: 
            print("До свидания!")   
            break
        else:
            print('Неизвестная команда.')
        
main_menu()