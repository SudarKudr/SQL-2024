import sqlite3
import tkinter as tk
from tkinter import messagebox
import hashlib

import admin_1_Work

# Create or connect to a SQLite database
conn = sqlite3.connect('music_database.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS музыкант (
                id_author INTEGER PRIMARY KEY,
                name_au TEXT,
                family_au TEXT,
                id_group INTEGER
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS группы (
                id_group INTEGER PRIMARY KEY,
                name_group TEXT,
                id_country INTEGER
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS музыки (
                id_music INTEGER PRIMARY KEY,
                name_music TEXT,
                id_group INTEGER,
                id_zapis INTEGER,
                id_zhanr INTEGER
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS альбом (
                id_album INTEGER PRIMARY KEY,
                name_album TEXT,
                id_music INTEGER,
                id_group INTEGER,
                id_zapis INTEGER
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS жанр (
                id_zhanr INTEGER PRIMARY KEY,
                name_zhanr TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS типЗаписи (
                id_zapis INTEGER PRIMARY KEY,
                name_zapis TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS страна (
                id_country INTEGER PRIMARY KEY,
                name_country TEXT
             )''')


'''
# Insert sample data into the tables
c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Первый', 'музыкант', 1)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Второй', 'музыкант', 1)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Третий', 'музыкант', 2)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Четвертый_g3', 'гитарист', 3)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Пятный_g3', 'барабаник', 3)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('шестой_g3', 'рокер', 3)")
#c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES ('Седьмой', 'скрипач', 4)")

c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group1', 1)")
c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group2', 8)")
c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group3', 5)")
c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group4', 4)")
#c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group44', 4)")
#c.execute("INSERT INTO группы (name_group, id_country) VALUES ('Group444', 4)")

c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES ('Music 1', 1, 1, 3)")
c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES ('Music 2', 2, 2, 2)")
#c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES ('Music3_rock_p1', 3, 3, 1)")
#c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES ('Music3_rock_p2', 3, 2, 1)")
#c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES ('Music_44', 4, 3, 1)")

c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES ('Album 1', 1, 1, 1)")
#c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES ('Album 1.1', 1, 1, 2)")
#c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES ('Album 3_rocker_1', 3, 2, 3)")
#c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES ('Album 3_rocker_2', 4, 2, 3)")
#c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES ('Album 4', 5, 4, 3)")


c.execute("INSERT INTO жанр (name_zhanr) VALUES ('Рок_1')")
c.execute("INSERT INTO жанр (name_zhanr) VALUES ('Спокойно_2')")
c.execute("INSERT INTO жанр (name_zhanr) VALUES ('Любовь_3')")

c.execute("INSERT INTO типЗаписи (name_zapis) VALUES ('диск')")
c.execute("INSERT INTO типЗаписи (name_zapis) VALUES ('кассета')")
c.execute("INSERT INTO типЗаписи (name_zapis) VALUES ('любаяЗапись')")

c.execute("INSERT INTO страна (name_country) VALUES ('Rus Fed')")
c.execute("INSERT INTO страна (name_country) VALUES ('Ua')")
c.execute("INSERT INTO страна (name_country) VALUES ('Germany')")
c.execute("INSERT INTO страна (name_country) VALUES ('Un King')")
c.execute("INSERT INTO страна (name_country) VALUES ('Austria')")
c.execute("INSERT INTO страна (name_country) VALUES ('Belarus')")
c.execute("INSERT INTO страна (name_country) VALUES ('Belgium')")
c.execute("INSERT INTO страна (name_country) VALUES ('Bolivia')")
c.execute("INSERT INTO страна (name_country) VALUES ('Brazil L')")
c.execute("INSERT INTO страна (name_country) VALUES ('Egypt')")
c.execute("INSERT INTO страна (name_country) VALUES ('Estonia A')")
c.execute("INSERT INTO страна (name_country) VALUES ('Poland')")
c.execute("INSERT INTO страна (name_country) VALUES ('Turkey T')")
conn.commit()
'''

# Create Tkinter application
root = tk.Tk()
root.title("Music Search App")
root.geometry("570x340")

# Create button to switch to admin mode
admin_mode_button = tk.Button(root, text="👷Switch to Admin Mode👷", command=admin_1_Work.open_admin_window)
admin_mode_button.place(x=400, y=300)
########################################
#############👷👷👷👷👷##############
#############👷👷👷👷👷##############
########################################


label_group = tk.Label(root, text="Введите название/имя:")
label_group.place(x=10, y=0)
entry_group = tk.Entry(root)
entry_group.place(x=10, y=20)
label_family = tk.Label(root, text="Введите фамилию(при наличии)")
label_family.place(x=150, y=0)
entry_family = tk.Entry(root)
entry_family.place(x=150, y=20)

label_spisok1= tk.Label(root, text="Или выберите из списка")
label_spisok1.place(x=345, y=0)
actions = [" ", "Исполнители", "Музыка", "Альбом"]

# категория меняется если меняется другая категория, крч динамическая
def on_category_select(*args):
    selected_category = actions_var.get()
    if selected_category == 'Исполнители':
        c.execute("SELECT DISTINCT name_au, family_au FROM музыкант")
        album_items = c.fetchall()
        name_var.set('')
        action_dropdown['menu'].delete(0, 'end')  # очистка
        for album_item in album_items:
            action_dropdown['menu'].add_command(label=album_item[0]+" " +album_item[1], command=lambda name=album_item[0]+" " +album_item[1]: name_var.set(name))
    elif selected_category == 'Музыка':
        c.execute("SELECT DISTINCT name_music FROM музыки")
        album_items = c.fetchall()
        name_var.set('')
        action_dropdown['menu'].delete(0, 'end')  # очистка
        for album_item in album_items:
            action_dropdown['menu'].add_command(label=album_item[0], command=lambda name=album_item[0]: name_var.set(name))
    elif selected_category == 'Альбом':
        c.execute("SELECT DISTINCT name_album FROM альбом")
        album_items = c.fetchall()
        name_var.set('')
        action_dropdown['menu'].delete(0, 'end')  # очистка
        for album_item in album_items:
            action_dropdown['menu'].add_command(label=album_item[0], command=lambda name=album_item[0]: name_var.set(name))
    else:
        name_var.set('Выберите чуть выше')
        action_dropdown['menu'].delete(0, 'end')  # Clear current options

spisok = ["Выберите чуть выше"]
actions_var = tk.StringVar(root)
actions_var.set(actions[0])
category_dropdown = tk.OptionMenu(root, actions_var, *actions)
category_dropdown.place(x=345, y=20)

name_var = tk.StringVar(root)
name_var.set(spisok[0])
action_dropdown = tk.OptionMenu(root, name_var, *spisok)
action_dropdown.place(x=345, y=50)
actions_var.trace('w', on_category_select)


# Enter search type on the right
label_search_type = tk.Label(root, text="Что хотите найти?")
label_search_type.place(x=180, y=70)
categories = ["Альбом", "Песню"]
category_var11 = tk.StringVar(root)
category_var11.set(categories[0])  # Set default value
choose_category = tk.OptionMenu(root, category_var11, *categories)
choose_category.place(x=180, y=90)

label_search_type22 = tk.Label(root, text="Что вводите?")
label_search_type22.place(x=10, y=70)
categories22 = ["Имя исполнителя", "Название песни", "Название альбома"]
category_var22 = tk.StringVar(root)
category_var22.set(categories22[0])  # Set default value
choose_category22 = tk.OptionMenu(root, category_var22, *categories22)
choose_category22.place(x=10, y=90)









#  #entry_group.get - не только название ГРУППЫ но и название МУЗЫКИ и ИМЯ музыканта
def show_albums_or_music():
    if actions_var.get() in " " and entry_group.get() in " ":
        messagebox.showerror("Пустое", "выберите или напишите")
        return
    # Поиск через выпадающее окно
    elif actions_var.get() not in " ": #actions = [" ", "Исполнители", "Музыка", "Альбом"] 
        if actions_var.get() == "Исполнители":
            print("              через имя исполнителя " + name_var.get()) # нужно будет разделить на строки
            FIO = name_var.get().split()
            c.execute("SELECT id_group FROM музыкант WHERE name_au = ? AND family_au = ?", (FIO[0], FIO[1]))
            
        elif actions_var.get() == "Музыка":
            print("          через название музыки " + name_var.get())
            c.execute("SELECT id_group FROM музыки WHERE name_music = ?", (name_var.get(),))
        else:
            print("          через название альбома " + name_var.get())
            c.execute("SELECT id_group FROM альбом WHERE name_album = ?", (name_var.get(),))
            
        if category_var11.get() == "Альбом":
            print("Хочет найти альбом")
            ##### кусок для поиска и вывода ####выше это код для того чтобы узнать gr снизу
            gr = c.fetchall()
            name_alb = []
            for i in gr:
                c.execute("SELECT id_album FROM альбом WHERE id_group = ?", (i[0],))
                name_alb = c.fetchall()

            resultsFind = []
            for j in name_alb:
                print(j[0])
                c.execute("SELECT альбом.id_album, альбом.name_album, музыки.name_music, группы.name_group, типЗаписи.name_zapis, страна.name_country FROM альбом INNER JOIN музыки, группы, типЗаписи, страна ON альбом.id_music = музыки.id_music AND альбом.id_group = группы.id_group AND альбом.id_zapis = типЗаписи.id_zapis AND группы.id_country = страна.id_country AND альбом.id_album = ?", (j[0],))
                resultsFind.extend(c.fetchall())
        else:
            print("Хочет найти песню(музыку)")
            ##### кусок для поиска и вывода
            gr = c.fetchall()
            name_alb = []
            for i in gr:
                c.execute("SELECT id_music FROM музыки WHERE id_group = ?", (i[0],))
                name_alb = c.fetchall()

            resultsFind = []
            for j in name_alb:
                print(j[0])
                c.execute("SELECT музыки.id_music, музыки.name_music, группы.name_group, типЗаписи.name_zapis, жанр.name_zhanr, страна.name_country FROM музыки INNER JOIN группы, типЗаписи, жанр, страна ON музыки.id_group = группы.id_group AND музыки.id_zapis = типЗаписи.id_zapis AND музыки.id_zhanr = жанр.id_zhanr AND группы.id_country = страна.id_country AND музыки.id_music = ?", (j[0],))
                resultsFind.extend(c.fetchall())
        print("строка actions_var не готова")
    ######################### выше для кнопки
    # Поиск через строку ввода
    else:
    ######################### ниже для ручного ввода
        if category_var22.get() == "Имя исполнителя":
            print("              через имя исполнителя " + entry_group.get()) # нужно будет еще добавить фамилию
            if entry_family.get() in " ":
                messagebox.showerror("Пустое", "напишите фамилию")
                return
            c.execute("SELECT id_group FROM музыкант WHERE name_au = ? AND family_au = ?", (entry_group.get(), entry_family.get()))
                
        elif category_var22.get() == "Название песни":
            print("          через название музыки " + entry_group.get())
            c.execute("SELECT id_group FROM музыки WHERE name_music = ?", (entry_group.get(),))
        else:
            print("          через название альбома " + entry_group.get())
            c.execute("SELECT id_group FROM альбом WHERE name_album = ?", (entry_group.get(),))

        if category_var11.get() == "Альбом":
            print("Хочет найти альбом")
            ##### кусок для поиска и вывода ####выше это код для того чтобы узнать gr снизу
            gr = c.fetchall()
            name_alb = []
            for i in gr:
                c.execute("SELECT id_album FROM альбом WHERE id_group = ?", (i[0],))
                name_alb = c.fetchall()

            resultsFind = []
            for j in name_alb:
                print(j[0])
                c.execute("SELECT альбом.id_album, альбом.name_album, музыки.name_music, группы.name_group, типЗаписи.name_zapis, страна.name_country FROM альбом INNER JOIN музыки, группы, типЗаписи, страна ON альбом.id_music = музыки.id_music AND альбом.id_group = группы.id_group AND альбом.id_zapis = типЗаписи.id_zapis AND группы.id_country = страна.id_country AND альбом.id_album = ?", (j[0],))
                resultsFind.extend(c.fetchall())
        else:
            print("Хочет найти песню(музыку)")
            ##### кусок для поиска и вывода
            gr = c.fetchall()
            name_alb = []
            for i in gr:
                c.execute("SELECT id_music FROM музыки WHERE id_group = ?", (i[0],))
                name_alb = c.fetchall()

            resultsFind = []
            for j in name_alb:
                print(j[0])
                c.execute("SELECT музыки.id_music, музыки.name_music, группы.name_group, типЗаписи.name_zapis, жанр.name_zhanr, страна.name_country FROM музыки INNER JOIN группы, типЗаписи, жанр, страна ON музыки.id_group = группы.id_group AND музыки.id_zapis = типЗаписи.id_zapis AND музыки.id_zhanr = жанр.id_zhanr AND группы.id_country = страна.id_country AND музыки.id_music = ?", (j[0],))
                resultsFind.extend(c.fetchall())
        print("строка entry_group не готова")
    
    #resultsFind = c.fetchall()
    result_Find = tk.Toplevel(root)
    result_Find.title("Результат поиска ")
    columns = [desc[0] for desc in c.description]
    #tree = ttk.Treeview(resultsFind, columns=['ID', 'имя', 'фамилия', 'группа'], show='headings')
    #tree.pack()
    tree = ttk.Treeview(result_Find, columns=columns, show='headings', height=len(resultsFind))
    tree.pack()
    
    def sort_treeRes(column):
        data = [(tree.set(child, column), child) for child in tree.get_children('')]
        
        def try_int(x):
            try:
                return int(x)
            except ValueError:
                return x

        data.sort(key=lambda x: try_int(x[0]))
        
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: sort_treeRes(c))
    for row in resultsFind:
        tree.insert('', 'end', values=row)


submit_AND_search_button = tk.Button(root, text="✅ Поиск ✅", command=show_albums_or_music)
submit_AND_search_button.place(x=300, y=90)



from tkinter import ttk

def def_show_DataBase():
    if category_var_DataBase.get() == 'музыкант':
        c.execute("SELECT * FROM музыкант")
    elif category_var_DataBase.get() == 'группы':
        c.execute("SELECT * FROM группы")
    elif category_var_DataBase.get() == 'музыки':
        c.execute("SELECT * FROM музыки")
    elif category_var_DataBase.get() == 'альбом':
        c.execute("SELECT * FROM альбом")
    elif category_var_DataBase.get() == 'жанр':
        c.execute("SELECT * FROM жанр")
    elif category_var_DataBase.get() == 'типЗаписи':
        c.execute("SELECT * FROM типЗаписи")
    else: ## страна
        c.execute("SELECT * FROM страна")

    results = c.fetchall()
    result_window = tk.Toplevel(root)
    result_window.title("База Данных " + category_var_DataBase.get())
    columns = [desc[0] for desc in c.description]
    tree = ttk.Treeview(result_window, columns=columns, show='headings', height=len(results))
    tree.pack()
    
    def sort_tree(column):
        data = [(tree.set(child, column), child) for child in tree.get_children('')]
        
        def try_int(x):
            try:
                return int(x)
            except ValueError:
                return x

        data.sort(key=lambda x: try_int(x[0]))
        
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)


    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: sort_tree(c))
    for row in results:
        tree.insert('', 'end', values=row)



show_DataBase = tk.Label(root, text="Показать полный БД")
show_DataBase.place(x=180, y=180)
categories_show_DataBase = ["музыкант", "группы", "музыки", "альбом", "жанр", "типЗаписи", "страна"]
category_var_DataBase = tk.StringVar(root)
category_var_DataBase.set(categories_show_DataBase[0])  # Set default value
choose_category22 = tk.OptionMenu(root, category_var_DataBase, *categories_show_DataBase)
choose_category22.place(x=150, y=200)
submit_AND_show_button = tk.Button(root, text="Показать", command=def_show_DataBase)
submit_AND_show_button.place(x=280, y=200)


root.mainloop()
# Close the connection to the database
conn.close()
