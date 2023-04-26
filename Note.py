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
    with open(file_name, 'r', newline='', encoding='utf8') as data:
        notes =csv.DictReader(data, delimiter=';', fieldnames=headersCSV)
        for line in notes:
            for v in line.values():
                print(f"{v};\t", end ="")
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
    
        
        
def save_notes(notes):
    with open(file_name, "w", encoding="utf8") as data:
        csv.dump(notes, data, indent=4)


def change_contact(word:str):
    buffer = ""
    with open(file_name, "r", encoding="utf8") as data1:
        lines = data1.readlines()
        for line in lines:
            line = line.strip()
            if word.upper() in line.upper():
                print (line)
                new_contact = str(input("Введите новый контакт:"))
                buffer += new_contact+'\n'
            else:
                buffer += line+'\n'
    with open(file_name, 'w', encoding="utf8") as data2:
        data2.write(buffer)

def delete_note(id:str):
    id = str(input("Введите ID удаляемой заметки:"))
    with open(file_name, "r", encoding="utf8") as data1:
        lines = data1.readlines()
        for line in lines:
            line = line.strip()
            
    with open(file_name, 'w', encoding="utf8") as data2:
        data2.write(buffer)
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
    data.close()

def main_menu():
    while True:
        num = int(input("\nВведите: 1 - просмотр блокнота;"
            ' 2 - поиск заметки; 3 - добавить заметку; 4 - изменить заметку;'
            ' 5 - удалить заметку; 6 - выйти из программы:\n'))
        if num == 1:
            view_notes()
        elif num == 2: 
            add_notes()
        elif num == 3:
            change_contact(str(input("Введите изменения:")))
        elif num == 4:
            delete_contact(str(input("Введите ID заметки:")))
        elif num == 5: 
            print("До свидания!")   
            break
        else:
            print('Неизвестная команда.')
        
main_menu()