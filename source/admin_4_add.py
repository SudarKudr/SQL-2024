import sqlite3
import tkinter as tk
from tkinter import messagebox
import main    

def add_Zhanr_typeZapis_country(conn, categore, name):
    c = conn.cursor()
    if (name in ['', ' ']):
        messagebox.showerror("Error 444_type 😰 добавление", "Пустое название")
        return
    else:
        if categore == 'жанр':
            c.execute("SELECT COUNT(*) FROM жанр WHERE name_zhanr = ?", (name,))
            count = c.fetchone()[0]
            if count == 0:
                c.execute("INSERT INTO жанр (name_zhanr) VALUES (?)", (name,))
                messagebox.showinfo("Успех", "Добавлено!")
                conn.commit()
            else:
                print("Ignoring duplicate rowjhbhbhbhbhbhbu:")
                messagebox.showerror("Такой жанр уже есть", "Такой жанр уже есть")
                return
        elif categore == 'типЗаписи':
            c.execute("SELECT COUNT(*) FROM типЗаписи WHERE name_zapis = ?", (name,))
            count = c.fetchone()[0]
            if count == 0:
                c.execute("INSERT INTO типЗаписи (name_zapis) VALUES (?)", (name,))
                messagebox.showinfo("Успех", "Добавлено!")
                conn.commit()
            else:
                print("Ignoring duplicate rowjhbhbhbhbhbhbu:")
                messagebox.showerror("Такой типЗаписи уже есть", "Такой типЗаписи уже есть")
                return
        elif categore == 'страна':
            c.execute("SELECT COUNT(*) FROM страна WHERE name_country = ?", (name,))
            count = c.fetchone()[0]
            if count == 0:
                c.execute("INSERT INTO страна (name_country) VALUES (?)", (name,))
                messagebox.showinfo("Успех", "Добавлено!")
                conn.commit()
            else:
                print("Ignoring duplicate rowjhbhbhbhbhbhbu:")
                messagebox.showerror("Такая страна уже есть", "Такая страна уже есть")
                return
        

def add_musicant(conn, name, family, id_grr):
    c = conn.cursor()
    if (name in ['', ' ']) or (family in ['', ' ']): #or (id_gr in ['', ' ']):
        messagebox.showerror("Error 444_музыкант 😰 добавление", "Хотя бы одна строка пустая, так нельзя")
        return
    else:
        parts = id_grr.split()  # делим the string into a list of words
        id_gr = int(parts[0])  # extract the first element and convert it to an integer
        print(id_gr)  # output: int
        
        c.execute("SELECT COUNT(*) FROM музыкант WHERE name_au = ? AND family_au = ?", (name, family))
        count = c.fetchone()[0]
        if count == 0:
            c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES (?, ?, ?)", (name, family, id_gr))
            messagebox.showinfo("Успех", "Добавлено!")
            conn.commit()
        else:
            print("Ignoring duplicate rowjhbhbhbhbhbhbuмузыкантмузыкант:")
            messagebox.showerror("Такой автор уже есть", "Такой музыкант уже есть")
            return


def add_Group(conn, name, id_countr):
    c = conn.cursor()
    if (name in ['', ' ']):
        messagebox.showerror("Error 444 add_Group 😰 добавление", "строка пустая, так нельзя")
        return
    else:
        parts = id_countr.split()  # делим the string into a list of words
        id_coutr = int(parts[0])  # extract the first element and convert it to an integer
        print(id_coutr)  # output: int
        
        c.execute("SELECT COUNT(*) FROM группы WHERE name_group = ?", (name,))
        count = c.fetchone()[0]
        if count == 0:
            c.execute("INSERT INTO группы (name_group, id_country) VALUES (?, ?)", (name, id_coutr))
            messagebox.showinfo("Успех", "Добавлено!")
            conn.commit()
        else:
            print("Ignoring duplicate rowjhbhbhbhbhbhbuгруппы группы:")
            messagebox.showerror("Такая группа уже есть", "Такая группа уже есть")
            return
        

def add_music(conn, name, id_grr, id_zap, id_zhan_mus):
    c = conn.cursor()
    if (name in ['', ' ']):
        messagebox.showerror("Error 444 add_music 😰 добавление", "строка пустая, так нельзя")
        return
    else:
        parts = id_grr.split()  # делим the string into a list of words
        id_gr = int(parts[0])  # extract the first element and convert it to an integer
        #print(id_gr)  # output: int

        parts = id_zap.split()  # делим the string into a list of words
        id_zapis = int(parts[0])  # extract the first element and convert it to an integer
        #print(id_zapis)  # output: int

        parts = id_zhan_mus.split()  # делим the string into a list of words
        id_zh_mus = int(parts[0])  # extract the first element and convert it to an integer
        #print(id_zh)  # output: int
        c.execute("SELECT COUNT(*) FROM музыки WHERE name_music = ?", (name,))
        count = c.fetchone()[0]
        if count == 0:
            c.execute("INSERT INTO музыки (name_music, id_group, id_zapis, id_zhanr) VALUES (?, ?, ?, ?)", (name, id_gr, id_zapis, id_zh_mus))
            messagebox.showinfo("Успех", "Добавлено!")
            conn.commit()
        else:
            print("Ignoring duplicate rowjhbhbhbhbhbhbuгруппы музыки:")
            messagebox.showerror("Такая музыка уже есть", "Такая музыка уже есть")
            return
                    

def create_new_album(admin_window_2, conn, id_grr):
    admin_window_2.destroy()

    def add():
        if (entry_name.get() in ['', ' ']):
            messagebox.showerror("Error 55 create_new_album 😰 добавление", "имя пустое")
            return
        else:
            c.execute("SELECT COUNT(*) FROM альбом WHERE name_album = ?", (entry_name.get(),))
            count = c.fetchone()[0]
            if count == 0:
                parts = id_zap.get().split()
                id_zapis = int(parts[0])

                parts = id_mus.get().split()
                idmus = int(parts[0])

                c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES (?, ?, ?, ?)", (entry_name.get(), idmus, id_gr, id_zapis))
                messagebox.showinfo("Успех", "Добавлено!")
                conn.commit()
            else:
                print("Ignoring duplicate rowjhbhbhbhbhbhbuгруппы альбом:")
                messagebox.showerror("Такое название альбома уже есть", "Такое название альбома уже есть")
                return

    parts = id_grr.split()
    id_gr = int(parts[0])  
    
    c = conn.cursor()
    admin_window_4 = tk.Toplevel(main.root)
    admin_window_4.title("👷 Добавление НОВОГО альбома 👷")
    admin_window_4.geometry("500x300")
    for i in range(10):
        for j in range(7):
            smile = tk.Label(admin_window_4, text="👷", font=14)
            smile.place(x=i*100, y=j*100)
    
    label_name = tk.Label(admin_window_4, text="Введите название альбома")
    label_name.place(x=10, y=10)
    entry_name = tk.Entry(admin_window_4)
    entry_name.place(x=10, y=30)

    label_name = tk.Label(admin_window_4, text="выберите типЗаписи")
    label_name.place(x=30, y=60)
    c.execute("SELECT id_zapis, name_zapis FROM типЗаписи")
    results = c.fetchall()
    selectGroup = []
    for row in results:
        selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
    id_zap = tk.StringVar(admin_window_4)
    id_zap.set(selectGroup[0])  # Set default value
    action_dropdown = tk.OptionMenu(admin_window_4, id_zap, *selectGroup)
    action_dropdown.place(x=40, y=80)

    label_name = tk.Label(admin_window_4, text="выберите музыку которая есть у выбранной группы")
    label_name.place(x=60, y=110)
    c.execute("SELECT id_music, name_music FROM музыки WHERE id_group = ?", (id_gr,))
    results = c.fetchall()
    selectGroup = []
    for row in results:
        selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
    id_mus = tk.StringVar(admin_window_4)
    id_mus.set(selectGroup[0])  # Set default value
    action_dropdown = tk.OptionMenu(admin_window_4, id_mus, *selectGroup)
    action_dropdown.place(x=150, y=130)

    submit_AND_do = tk.Button(admin_window_4, text="✅ Добавить ✅", command=add) #(entry_name.get(), id_zap.get(), id_mus.get()))
    submit_AND_do.place(x=200, y=160)


def add_to_old_album(admin_window_2, conn, id_grr):
    admin_window_2.destroy()

    def yes():
        def yes_add():
            parts_mus = id_name_mus.get().split()
            id_mus = int(parts_mus[0])  
            
            c.execute("SELECT COUNT(*) FROM альбом WHERE name_album = ? AND id_music = ? AND id_group = ? AND id_zapis = ?", (nameAlb, id_mus, id_gr, id_zap))
            count = c.fetchone()[0]
            if count == 0:
                c.execute("INSERT INTO альбом (name_album, id_music, id_group, id_zapis) VALUES (?, ?, ?, ?)", (nameAlb, id_mus, id_gr, id_zap))
                messagebox.showinfo("Успех", "Добавлено!")
                conn.commit()
            else:
                print("Ignoring duplicate rowjhbhbhbhbhbhbuгруппы альбом:")
                messagebox.showerror("Такой альбом уже есть", "альбом с этой музыкой уже есть")
                return
            
        admin_window_4.destroy()

        admin_window_5 = tk.Toplevel(main.root)
        admin_window_5.title("👷 Добавление CУЩЕСТВУЮЩЕГО альбома - 2 👷")
        admin_window_5.geometry("500x300")
        for i in range(10):
            for j in range(7):
                smile = tk.Label(admin_window_5, text="👷", font=14)
                smile.place(x=i*100, y=j*100)
        
        #выводим id и название альбома, группы и тип записи
        # сначала присвоим имя и id альбома в stroka
        stroka = "| " + id_name_alb.get() + " | "

        parts = id_name_alb.get().split()
        id_alb = int(parts[0])

        c.execute("SELECT name_album FROM альбом WHERE id_album = ?", (id_alb,))
        nameAlb = c.fetchone()[0]

        c.execute("SELECT id_group, name_group FROM группы WHERE id_group = ?", (id_gr,))
        res = c.fetchone()
        stroka = stroka + str(res[0]) + "-" + str(res[1]) + " | "

        c.execute("SELECT id_zapis FROM альбом WHERE id_album = ?", (id_alb,))
        id_zap = c.fetchone()[0]
        c.execute("SELECT id_zapis, name_zapis FROM типЗаписи WHERE id_zapis = ?", (id_zap,))
        res = c.fetchone()
        stroka = stroka + str(res[0]) + "-" + str(res[1]) + " |"

        print("=============+++++++++++++++===========|  " + stroka)
        label_name = tk.Label(admin_window_5, text="Ваш выбор, осталось выбрать какую музыку добавить")
        label_name.place(x=10, y=20)
        label_name = tk.Label(admin_window_5, text=stroka)
        label_name.place(x=10, y=40)


        c.execute("SELECT id_music, name_music FROM музыки WHERE id_group = ?", (id_gr,))
        results = c.fetchall()
        selectGroup = []
        for row in results:
            selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
        id_name_mus = tk.StringVar(admin_window_5)
        id_name_mus.set(selectGroup[0])  # Set default value
        action_dropdown = tk.OptionMenu(admin_window_5, id_name_mus, *selectGroup)
        action_dropdown.place(x=10, y=70)

        submit_AND_do = tk.Button(admin_window_5, text="✅ Добавить ✅", command= yes_add)
        submit_AND_do.place(x=200, y=160)

#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////
    
    parts = id_grr.split()
    id_gr = int(parts[0])  
    
    c = conn.cursor()
    admin_window_4 = tk.Toplevel(main.root)
    admin_window_4.title("👷 Добавление CУЩЕСТВУЮЩЕГО альбома - 1 👷")
    admin_window_4.geometry("500x300")
    for i in range(10):
        for j in range(7):
            smile = tk.Label(admin_window_4, text="👷", font=14)
            smile.place(x=i*100, y=j*100)

    label_name = tk.Label(admin_window_4, text="выберите альбом")
    label_name.place(x=30, y=60)
    c.execute("SELECT id_album AS id_album, name_album FROM альбом WHERE id_group = ? ORDER BY name_album", (id_gr,))
    results = c.fetchall()
    selectGroup = []
    for row in results:
        selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
    id_name_alb = tk.StringVar(admin_window_4)
    id_name_alb.set(selectGroup[0])  # Set default value
    action_dropdown = tk.OptionMenu(admin_window_4, id_name_alb, *selectGroup)
    action_dropdown.place(x=40, y=80)
    

    submit_AND_do = tk.Button(admin_window_4, text="✅ Подтвердить ✅", command= yes)
    submit_AND_do.place(x=200, y=160)