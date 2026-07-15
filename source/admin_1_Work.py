import sqlite3
import tkinter as tk
from tkinter import messagebox
import random
import hashlib

import shutil
import datetime



import main
import admin_2_redakt
import admin_3_delete
import admin_4_add

conn = sqlite3.connect('music_database.db')
c = conn.cursor()


hashed_password = hashlib.sha256("password123".encode()).hexdigest()
print(hashed_password)

########################################
#############👷👷👷👷👷##############
#############👷👷👷👷👷##############
########################################
# Function to create hashed password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to open admin window
def open_admin_window():
    admin_login_window = tk.Toplevel(main.root)
    admin_login_window.title("Admin Login")
    label_username = tk.Label(admin_login_window, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(admin_login_window)
    entry_username.pack()
    label_password = tk.Label(admin_login_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(admin_login_window, show="*")
    entry_password.pack()
    login_button = tk.Button(admin_login_window, text="Login", command=lambda: admin_login(entry_username.get(), entry_password.get(), admin_login_window))
    login_button.pack()

# Function for admin login
def admin_login(username, password, window):
    if username == 'admin' and hash_password(password) == 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f':
        window.destroy()
        admin_mode()
    elif username == '':
        window.destroy()
        admin_mode()
    else:
        messagebox.showerror("Fatal Error", "Incorrect username or password")

# Function for admin mode
def admin_mode():
    admin_window = tk.Toplevel(main.root)
    admin_window.title("👷Admin Mode👷")
    admin_window.geometry("500x300")

    def create_backup():
        database_name = 'music_database.db'
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_filename = f'backup_{timestamp}.db'
        shutil.copyfile(database_name, backup_filename)
        print(f'Backup created as {backup_filename}')
        messagebox.showerror("Успешно", f'Резервная копия сделана в файле {backup_filename}')
        return

    button = tk.Button(admin_window, text="сделать резервную копию", command=create_backup)
    button.place(x=150, y=150)



    categories = ["музыкант", "группы", "музыки", "альбом", "жанр", "типЗаписи", "страна"]
    
    for i in range(10):
        for j in range(10):
            smile = tk.Label(admin_window, text="👷", font=14)
            smile.place(x=i*100, y=j*100)
    
    category_label = tk.Label(admin_window, text="Выберите БД:")
    category_label.pack()
    category_var = tk.StringVar(admin_window)
    category_var.set(categories[0])  # Set default value
    category_dropdown = tk.OptionMenu(admin_window, category_var, *categories)
    category_dropdown.pack()

    actions = ["Добавить", "Изменить", "Удалить"]
    action_label = tk.Label(admin_window, text="Дейстиве?")
    action_label.pack()
    action_var = tk.StringVar(admin_window)
    action_var.set(actions[0])  # Set default value
    action_dropdown = tk.OptionMenu(admin_window, action_var, *actions)
    action_dropdown.pack()

    def confirm_selection():
        selected_category = category_var.get()
        print("ADMIN Selected category:", selected_category)
        a_selected_category = action_var.get()
        print("ADMIN Selected actions:", a_selected_category)

        admin_window_2 = tk.Toplevel(main.root)
        admin_window_2.title("👷 " + action_var.get() + " 👷")
        admin_window_2.geometry("500x300")
        for i in range(10):
            for j in range(7):
                if action_var.get() == 'Удалить':
                    smile = tk.Label(admin_window_2, text="🗑️❌", font=14)
                else:
                    smile = tk.Label(admin_window_2, text="👷", font=14)
                smile.place(x=i*100, y=j*100)


        ##выбор действии
        if action_var.get() == 'Добавить' and category_var.get() == 'альбом':
                def have_it_or_no(): 
                    parts = entry_id_grr.get().split()
                    id_gr = int(parts[0])

                    c.execute("SELECT COUNT(*) FROM альбом WHERE id_group = ?", (id_gr,))
                    count = c.fetchone()[0]
                    if count == 0:
                        print("NONONONO group")
                        messagebox.showerror("Альбома нет", "Альбома с этой группой нет в БД")
                        return
                    else:
                        print("yes group")
                        admin_4_add.add_to_old_album(admin_window_2, conn, entry_id_grr.get())

                def have_it_or_no_NEW_alb(): 
                    parts = entry_id_grr.get().split()
                    id_gr = int(parts[0])

                    c.execute("SELECT COUNT(*) FROM музыки WHERE id_group = ?", (id_gr,))
                    count = c.fetchone()[0]
                    if count == 0:
                        print("NONONONO музыки")
                        messagebox.showerror("Музыки нет", "в БД музыки нет такой группы")
                        return
                    else:
                        print("yes музыки")
                        admin_4_add.create_new_album(admin_window_2, conn, entry_id_grr.get())


                label_name = tk.Label(admin_window_2, text="Сначала выберите id группы")
                label_name.place(x=10, y=10)
                c.execute("SELECT id_group, name_group FROM группы")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                entry_id_grr = tk.StringVar(admin_window_2)
                entry_id_grr.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, entry_id_grr, *selectGroup)
                action_dropdown.place(x=10, y=30)

                submit_AND_doIt = tk.Button(admin_window_2, text="Создать новый", command= have_it_or_no_NEW_alb)
                #проверяем что такая музыка есть в группе, если нету, то сначала добавить музыку потом альбом
                submit_AND_doIt.place(x=100, y=60)

                submit_AND_doIt = tk.Button(admin_window_2, text="Добавить существующий", command= have_it_or_no)
                #проверяем что Альбома с этой группой ЕСТЬ в БД
                submit_AND_doIt.place(x=100, y=150)

        elif action_var.get() == 'Добавить':
            label_name = tk.Label(admin_window_2, text="Введите название/имя")
            label_name.place(x=10, y=60)
            entry_name = tk.Entry(admin_window_2)
            entry_name.place(x=10, y=80)

            if category_var.get() == 'жанр' or category_var.get() == 'типЗаписи' or category_var.get() == 'страна':
                submit_AND_do = tk.Button(admin_window_2, text="✅ Добавить ✅", command=lambda: admin_4_add.add_Zhanr_typeZapis_country(conn, category_var.get(), entry_name.get()))
                submit_AND_do.place(x=200, y=160)
            if category_var.get() == 'музыкант':
                label_name = tk.Label(admin_window_2, text="Введите фамилию музыканта")
                label_name.place(x=10, y=120)
                entry_famil_muss = tk.Entry(admin_window_2)
                entry_famil_muss.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Выберите id группы музыканта")
                label_name.place(x=10, y=180)
                # entry_id_grr = tk.Entry(admin_window_2)
                # entry_id_grr.place(x=10, y=200)

                c.execute("SELECT id_group, name_group FROM группы")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                selectGroup_var = tk.StringVar(admin_window_2)
                selectGroup_var.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, selectGroup_var, *selectGroup)
                action_dropdown.place(x=10, y=200)
                # action_dropdown.pack()

                submit_AND_do = tk.Button(admin_window_2, text="✅ Добавить ✅", command=lambda: admin_4_add.add_musicant(conn, entry_name.get(), entry_famil_muss.get(), selectGroup_var.get()))
                submit_AND_do.place(x=200, y=160)
            elif category_var.get() == 'группы':
                label_name = tk.Label(admin_window_2, text="Выберите id страны группы")
                label_name.place(x=10, y=120)
                # entry_id_countr = tk.Entry(admin_window_2)
                # entry_id_countr.place(x=10, y=140)

                c.execute("SELECT id_country, name_country FROM страна")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                entry_id_countr = tk.StringVar(admin_window_2)
                entry_id_countr.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, entry_id_countr, *selectGroup)
                action_dropdown.place(x=10, y=140)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Добавить ✅", command=lambda: admin_4_add.add_Group(conn, entry_name.get(), entry_id_countr.get()))
                submit_AND_do.place(x=200, y=160)
            elif category_var.get() == 'музыки':
                label_name = tk.Label(admin_window_2, text="Выберите id группы")
                label_name.place(x=10, y=120)
                # entry_id_grr = tk.Entry(admin_window_2)
                # entry_id_grr.place(x=10, y=140)
                c.execute("SELECT id_group, name_group FROM группы")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                entry_id_grr = tk.StringVar(admin_window_2)
                entry_id_grr.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, entry_id_grr, *selectGroup)
                action_dropdown.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Выберите типЗаписи музыки")
                label_name.place(x=10, y=180)
                # entry_id_zap = tk.Entry(admin_window_2)
                # entry_id_zap.place(x=10, y=200)
                c.execute("SELECT id_zapis, name_zapis FROM типЗаписи")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                entry_id_zap = tk.StringVar(admin_window_2)
                entry_id_zap.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, entry_id_zap, *selectGroup)
                action_dropdown.place(x=10, y=200)

                label_name = tk.Label(admin_window_2, text="Выберите id жанра музыки")
                label_name.place(x=10, y=240)
                # entry_id_zhanr = tk.Entry(admin_window_2)
                # entry_id_zhanr.place(x=10, y=260)
                c.execute("SELECT id_zhanr, name_zhanr FROM жанр")
                results = c.fetchall()
                selectGroup = []
                for row in results:
                    selectGroup.append(f"{row[0]} - {row[1]}")  # Combine the two columns into a single string
                entry_id_zhanr = tk.StringVar(admin_window_2)
                entry_id_zhanr.set(selectGroup[0])  # Set default value
                action_dropdown = tk.OptionMenu(admin_window_2, entry_id_zhanr, *selectGroup)
                action_dropdown.place(x=10, y=260)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Добавить ✅", command=lambda: admin_4_add.add_music(conn, entry_name.get(), entry_id_grr.get(), entry_id_zap.get(), entry_id_zhanr.get()))
                submit_AND_do.place(x=200, y=160)

           
        elif action_var.get() == 'Изменить':
            if category_var.get() == 'музыкант':
                label_id = tk.Label(admin_window_2, text="   Введите id музыканта")
                label_id.place(x=10, y=0)
                entry_id_mus = tk.Entry(admin_window_2)
                entry_id_mus.place(x=10, y=20)

                label_name = tk.Label(admin_window_2, text=" Введите имя музыканта")
                label_name.place(x=10, y=60)
                entry_name_mus = tk.Entry(admin_window_2)
                entry_name_mus.place(x=10, y=80)

                label_name = tk.Label(admin_window_2, text=" Введите фамилию музыканта")
                label_name.place(x=10, y=120)
                entry_famil_mus = tk.Entry(admin_window_2)
                entry_famil_mus.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Введите id группы музыканта")
                label_name.place(x=10, y=180)
                entry_id_gr = tk.Entry(admin_window_2)
                entry_id_gr.place(x=10, y=200)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Изменить ✅", command=lambda: admin_2_redakt.redaktirovanie_musicant(conn, entry_id_mus.get(), entry_name_mus.get(), entry_famil_mus.get(), entry_id_gr.get()))
                submit_AND_do.place(x=200, y=160)
            elif category_var.get() == 'жанр' or category_var.get() == 'типЗаписи' or category_var.get() == 'страна':
                label_id = tk.Label(admin_window_2, text="   Введите id: " + category_var.get())
                label_id.place(x=10, y=0)
                entry_id_r = tk.Entry(admin_window_2)
                entry_id_r.place(x=10, y=20)

                label_name = tk.Label(admin_window_2, text=" Введите название: " + category_var.get())
                label_name.place(x=10, y=60)
                entry_name_r = tk.Entry(admin_window_2)
                entry_name_r.place(x=10, y=80)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Изменить ✅", command=lambda: admin_2_redakt.redaktirovanie_Zhanr_typeZapis_country(conn, category_var.get(), entry_id_r.get(), entry_name_r.get()))
                submit_AND_do.place(x=200, y=160)
            elif category_var.get() == 'группы':
                label_id = tk.Label(admin_window_2, text="   Введите id группы")
                label_id.place(x=10, y=0)
                entry_id_g = tk.Entry(admin_window_2)
                entry_id_g.place(x=10, y=20)

                label_name = tk.Label(admin_window_2, text=" Введите название группы")
                label_name.place(x=10, y=60)
                entry_name_g = tk.Entry(admin_window_2)
                entry_name_g.place(x=10, y=80)

                label_name = tk.Label(admin_window_2, text=" Введите id страны")
                label_name.place(x=10, y=120)
                entry_id_country = tk.Entry(admin_window_2)
                entry_id_country.place(x=10, y=140)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Изменить ✅", command=lambda: admin_2_redakt.redaktirovanie_Group(conn, entry_id_g.get(), entry_name_g.get(), entry_id_country.get(), 'notDel'))
                submit_AND_do.place(x=200, y=160)
            else: ## 'музыки'  'альбом'
                label_id = tk.Label(admin_window_2, text="   Введите id " + category_var.get())
                label_id.place(x=10, y=0)
                entry_id_a = tk.Entry(admin_window_2)
                entry_id_a.place(x=10, y=20)

                label_name = tk.Label(admin_window_2, text=" Введите название " + category_var.get())
                label_name.place(x=10, y=60)
                entry_name_a= tk.Entry(admin_window_2)
                entry_name_a.place(x=10, y=80)

                label_name = tk.Label(admin_window_2, text=" Введите id группы " + category_var.get())
                label_name.place(x=10, y=120)
                entry_id_grp = tk.Entry(admin_window_2)
                entry_id_grp.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Введите id записи")
                label_name.place(x=10, y=180)
                entry_id_zapis = tk.Entry(admin_window_2)
                entry_id_zapis.place(x=10, y=200)


                if category_var.get() == 'музыки':
                    pr = " жанра музыки"
                else:
                    pr = " музыки в альбоме"

                label_name = tk.Label(admin_window_2, text="Введите id " + pr)
                label_name.place(x=10, y=240)
                entry_id_zhanr_music = tk.Entry(admin_window_2)
                entry_id_zhanr_music.place(x=10, y=260)

                submit_AND_do = tk.Button(admin_window_2, text="✅ Изменить ✅", command=lambda: admin_2_redakt.redaktirovanie(conn, category_var.get(), entry_id_a.get(), entry_name_a.get(), entry_id_grp.get(), entry_id_zapis.get(), entry_id_zhanr_music.get()))
                submit_AND_do.place(x=200, y=160)
        else: ##Удалить
            ##узнать переменные
            c.execute("SELECT * FROM {}".format(category_var.get()))
            num_fields = len(c.description) 
            field_names = [i[0] for i in c.description] ##
            ##print("+++ ", field_names, " ------ ", field_names[0], "   ", field_names[1]) ##

            label_id = tk.Label(admin_window_2, text="Введите id "+category_var.get())
            label_id.place(x=10, y=0)
            entry_id = tk.Entry(admin_window_2)
            entry_id.place(x=10, y=20)

            label_name = tk.Label(admin_window_2, text="Введите название/имя")
            label_name.place(x=10, y=60)
            entry_name = tk.Entry(admin_window_2)
            entry_name.place(x=10, y=80)

            if category_var.get() == 'музыкант':
                label_name2 = tk.Label(admin_window_2, text="Музыкант удаляется только через ID")
                label_name2.place(x=230, y=120)
                label_name2 = tk.Label(admin_window_2, text="либо через другие данные по одному-две")
                label_name2.place(x=230, y=140)
                label_name2 = tk.Label(admin_window_2, text="АККУРАТНО если работаете с одним")
                label_name2.place(x=230, y=160)
                label_name2 = tk.Label(admin_window_2, text="данным - может удалить несколько сразу!")
                label_name2.place(x=230, y=180)

                label_name = tk.Label(admin_window_2, text="Введите фамилию музыканта")
                label_name.place(x=10, y=120)
                entry_famil_muss = tk.Entry(admin_window_2)
                entry_famil_muss.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Введите id группы музыканта")
                label_name.place(x=10, y=180)
                entry_id_grr = tk.Entry(admin_window_2)
                entry_id_grr.place(x=10, y=200)
            #elif category_var.get() == 'группы':
                #label_name = tk.Label(admin_window_2, text="Введите id страны группы")
                #label_name.place(x=10, y=120)
                #entry_id_countr = tk.Entry(admin_window_2)
                #entry_id_countr.place(x=10, y=140)
            elif category_var.get() == 'музыки':
                label_name = tk.Label(admin_window_2, text="Введите id группы")
                label_name.place(x=10, y=120)
                entry_id_grr = tk.Entry(admin_window_2)
                entry_id_grr.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Введите id записи музыки")
                label_name.place(x=10, y=180)
                entry_id_zap = tk.Entry(admin_window_2)
                entry_id_zap.place(x=10, y=200)

                label_name = tk.Label(admin_window_2, text="Введите id жанра музыки")
                label_name.place(x=10, y=240)
                entry_id_zhanr = tk.Entry(admin_window_2)
                entry_id_zhanr.place(x=10, y=260)
            elif category_var.get() == 'альбом':
                label_name2 = tk.Label(admin_window_2, text="Альбом удаляется только через ID")
                label_name2.place(x=200, y=120)
                label_name2 = tk.Label(admin_window_2, text="либо через другие данные по одному-две")
                label_name2.place(x=200, y=140)
                label_name2 = tk.Label(admin_window_2, text="АККУРАТНО если работаете с одним")
                label_name2.place(x=200, y=160)
                label_name2 = tk.Label(admin_window_2, text="данным - может удалить несколько альбомов!")
                label_name2.place(x=200, y=180)

                label_name = tk.Label(admin_window_2, text="Введите id группы")
                label_name.place(x=10, y=120)
                entry_id_grr = tk.Entry(admin_window_2)
                entry_id_grr.place(x=10, y=140)

                label_name = tk.Label(admin_window_2, text="Введите id записи альбома")
                label_name.place(x=10, y=180)
                entry_id_zap = tk.Entry(admin_window_2)
                entry_id_zap.place(x=10, y=200)

                label_name = tk.Label(admin_window_2, text="Введите id музыки альбома")
                label_name.place(x=10, y=240)
                entry_id_muz = tk.Entry(admin_window_2)
                entry_id_muz.place(x=10, y=260)


            def delete_it_now():
                if category_var.get() == 'страна' or category_var.get() == 'жанр' or category_var.get() == 'типЗаписи':
                    if (entry_id.get() in ['', ' ']) and (entry_name.get() in ['', ' ']):
                        messagebox.showerror("Error 333 😰", "Пустая строка при удалении")
                        return
                    elif (entry_id.get() not in ['', ' ']) and (entry_name.get() not in ['', ' ']): ## проверка что обе строки не пустые
                        ##c.execute("DELETE FROM {} WHERE ? = ?".format(category_var.get()), (field_names[0],))
                        ##conn.commit()
                        
                        ##удалять из категории(страна/жанр/типЗаписи) где ID = ? AND имя = ?
                        SQL_Command = " FROM " + category_var.get() + " WHERE " + field_names[0] + " = ? AND " + field_names[1] + " = ?"
                        ##выбрать id страна/жанр/типЗаписи из БД страна/жанр/типЗаписи
                        c.execute("SELECT "+ field_names[0] +SQL_Command, (entry_id.get(), entry_name.get()))
                        row = c.fetchone()
                        c.execute("DELETE" + SQL_Command, (entry_id.get(), entry_name.get()))
                        print("DELETE________________________________T ", SQL_Command)
                        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
                            messagebox.showerror("Удаление через оба", "Data not found in the database")
                        else:
                            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
                            conn.commit()
                            messagebox.showinfo("Удаление через оба", "Удалено успешно")
                            if category_var.get() == 'страна':
                                c.execute("SELECT id_group FROM группы WHERE id_country = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie_Group(conn, i[0], '', 0, 'Del') ## меняем id на нулевой у группы, так как страна связяна с группой
                            elif category_var.get() == 'жанр':
                                c.execute("SELECT id_music FROM музыки WHERE id_zhanr = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '', '', 0)
                                    ## меняем id на нулевой у музыки, так как жанр связяна с музыкой
                            elif category_var.get() == 'типЗаписи':
                                c.execute("SELECT id_music FROM музыки WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '',  0, '')
                            ## меняем id на нулевой у муз, так как типЗаписи связяна с муз и альб
                                    ## внизу меняем у альбома
                                c.execute("SELECT id_album FROM альбом WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'альбом', i[0], '', '', 0, '')
                            ## меняем id на нулевой у альб, так как типЗаписи связяна с муз и альб
                                return
                    elif (entry_id.get() in ['', ' ']) and (entry_name.get() not in ['', ' ']): ## удаление через имя
                        ##удалять из категории(страна/жанр/типЗаписи) где имя = ?
                        SQL_Command = " FROM " + category_var.get() + " WHERE " + field_names[1] + " = ?"
                         ##выбрать id страна/жанр/типЗаписи из БД страна/жанр/типЗаписи
                        c.execute("SELECT "+ field_names[0] +SQL_Command, (entry_name.get(),))
                        row = c.fetchone()
                        c.execute("DELETE" + SQL_Command, (entry_name.get(),))
                        print("DELETE________________________________T ", SQL_Command)
                        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
                            messagebox.showerror("Удаление через имя", "Data not found in the database")
                        else:
                            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
                            conn.commit()
                            messagebox.showinfo("Удаление через оба", "Удалено успешно")
                            if category_var.get() == 'страна':
                                c.execute("SELECT id_group FROM группы WHERE id_country = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie_Group(conn, i[0], '', 0, 'Del') ## меняем id на нулевой у группы, так как страна связяна с группой
                            elif category_var.get() == 'жанр':
                                c.execute("SELECT id_music FROM музыки WHERE id_zhanr = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '', '', 0)
                                    ## меняем id на нулевой у музыки, так как жанр связяна с музыкой
                            elif category_var.get() == 'типЗаписи':
                                c.execute("SELECT id_music FROM музыки WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '',  0, '')
                            ## меняем id на нулевой у муз, так как типЗаписи связяна с муз и альб
                                    ## внизу меняем у альбома
                                c.execute("SELECT id_album FROM альбом WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'альбом', i[0], '', '', 0, '')
                            ## меняем id на нулевой у альб, так как типЗаписи связяна с муз и альб
                                return
                    else:
                        ##удалять из категории(страна/жанр/типЗаписи) где ID = ?
                        SQL_Command = " FROM " + category_var.get() + " WHERE " + field_names[0] + " = ?"
                        ##выбрать id страна/жанр/типЗаписи из БД страна/жанр/типЗаписи
                        c.execute("SELECT "+ field_names[0] +SQL_Command, (entry_id.get(),))
                        row = c.fetchone()
                        c.execute("DELETE" + SQL_Command, (entry_id.get(),))
                        print("DELETE________________________________T ", SQL_Command)
                        conn.commit()
                        
                        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
                            messagebox.showerror("Удаление через id", "Data not found in the database")
                        else:
                            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
                            conn.commit()
                            messagebox.showinfo("Удаление через оба", "Удалено успешно")
                            if category_var.get() == 'страна':
                                c.execute("SELECT id_group FROM группы WHERE id_country = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie_Group(conn, i[0], '', 0, 'Del') ## меняем id на нулевой у группы, так как страна связяна с группой
                            elif category_var.get() == 'жанр':
                                c.execute("SELECT id_music FROM музыки WHERE id_zhanr = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '', '', 0)
                                    ## меняем id на нулевой у музыки, так как жанр связяна с музыкой
                            elif category_var.get() == 'типЗаписи':
                                c.execute("SELECT id_music FROM музыки WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', '',  0, '')
                            ## меняем id на нулевой у муз, так как типЗаписи связяна с муз и альб
                                    ## внизу меняем у альбома
                                c.execute("SELECT id_album FROM альбом WHERE id_zapis = ? ", (row[0],))
                                gr = c.fetchall()
                                for i in gr:
                                    ##print("----hhhhhhhh ", i[0])
                                    admin_2_redakt.redaktirovanie(conn, 'альбом', i[0], '', '', 0, '')
                            ## меняем id на нулевой у альб, так как типЗаписи связяна с муз и альб
                                return
#############################################################################################################################################################
#############################################################################################################################################################
####################################################################################################################################################################################################################
                elif category_var.get() == 'группы':
                    admin_3_delete.delet_droup(conn, entry_id, entry_name) #, entry_id_countr) думаю не надо через страну удалять? это бред
                elif category_var.get() == 'альбом':
                    admin_3_delete.delet_album(conn, entry_id, entry_name, entry_id_muz, entry_id_grr, entry_id_zap)
                elif category_var.get() == 'музыкант':
                    admin_3_delete.delet_musicant(conn, entry_id, entry_name, entry_famil_muss, entry_id_grr)
                    
                            
            submit_AND_do = tk.Button(admin_window_2, text="✅ Удалить ✅", command=delete_it_now)
            submit_AND_do.place(x=180, y=0)

    # Add your logic here to handle the selected category (add/edit/delete)
    submit_button = tk.Button(admin_window, text="Подтвердить", command=confirm_selection)
    submit_button.pack()
    
########################################
#############👷👷👷👷👷##############
#############👷👷👷👷👷##############
########################################

name_au = 'Первый'
family_au = 'музыкант'
id_group = 1

c.execute("SELECT COUNT(*) FROM музыкант WHERE name_au = ? AND family_au = ? AND id_group = ?", (name_au, family_au, id_group))
count = c.fetchone()[0]
if count == 0:
    c.execute("INSERT INTO музыкант (name_au, family_au, id_group) VALUES (?, ?, ?)", (name_au, family_au, id_group))
else:
    print("Ignoring duplicate rowjhbhbhbhbhbhbu:")
    

# Commit changes to the database
conn.commit()