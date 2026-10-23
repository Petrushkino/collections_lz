import pandas as pd

class AddressBook:
    def __init__(self):
        self.columns = ["ФИО", "Адрес", "Телефон", "Дата рождения"]
        self.book = pd.DataFrame(columns = self.columns)
        
    def show_book(self):
        if self.book.empty:
            print("Адресная книга пока пуста.")
        else:
            print("Текущая адресная книга")
            print(self.book.to_string())
    
    def add_record(self):
        print("Добавление новой записи:")
        fio = input("Введите ФИО: ")
        address = input("Введите Адрес: ")
        phone = input("Введите Телефон: ")
        dob = input("Введите Дату рождения: ")
        
        new_row = pd.DataFrame([[fio, address, phone, dob]], columns = self.columns)
        self.book = pd.concat([self.book, new_row], ignore_index=True)
        print("Запись успешно добавлена!")
        
    def delete_record(self):
        self.show_book()
            
        index = int(input("Введите индекс записи для удаления: "))
        if index in self.book.index:
            self.book = self.book.drop(index).reset_index(drop=True)
            print("Запись удалена!")
        else:
            print("Ошибка. Запись с таким индексом не найдена.")
        
    def modify_record(self):
        self.show_book()
            
        index = int(input("Введите индекс записи для изменения: "))
        if index not in self.book.index:
            print("Ошибка. Запись с таким индексом не найдена.")
            return
                
        print("Доступные поля для изменения: ФИО, Адрес, Телефон, Дата рождения")
        field = input("Введите название поля, которое хотите изменить: ")
            
        if field in self.columns:
            new_value = input("Введите новое значение для поля ", field)
            self.book.at[index, field] = new_value
            print("Запись обновлена!")
        else:
            print("Ошибка. Такого поля не существует.")


def main():
    app = AddressBook()
    print("                 АДРЕСНАЯ КНИГА                  ")
        
    while True:
        print("Выберите действие:")
        print("1 - Показать адресную книгу")
        print("2 - Добавить запись")
        print("3 - Изменить запись")
        print("4 - Удалить запись")
        print("0 - Выход")
        
        choice = input("Ваш выбор: ")
        
        match choice:
            case '1':
                app.show_book()
            case '2':
                app.add_record()
            case '3':
                app.modify_record()
            case '4':
                app.delete_record()
            case '0':
                print("Завершение работы.")
                break 
            case _:
                print("Ошибка. Неизвестная команда. Выберите цифру из меню.")


main()