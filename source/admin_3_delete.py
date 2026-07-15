import sqlite3
import tkinter as tk
from tkinter import messagebox

import admin_2_redakt

def delet_droup(conn, entry_id, entry_name):
    c = conn.cursor()
    if (entry_id.get() in ['', ' ']) and (entry_name.get() in ['', ' ']): 
        messagebox.showerror("Error 333 😰", "Пустая строка при удалении _droup")
        return
    ## проверка все строки не пустые
    elif (entry_id.get() not in ['', ' ']) and (entry_name.get() not in ['', ' ']):  ## проверка все строки не пустые (удаление через все)
       
        ##удалять из категории(группы) где ID = ? AND имя = ?
        SQL_Command = " FROM группы WHERE id_group = ? AND name_group = ?"
        c.execute("SELECT id_group" +SQL_Command, (entry_id.get(), entry_name.get()))
        row = c.fetchone()
        c.execute("DELETE" + SQL_Command, (entry_id.get(), entry_name.get()))
        print("DELETE___________group_______________T ", SQL_Command)
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через все", "Data not found in the database")
        else:
            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
            messagebox.showinfo("Удаление через все", "Удалено успешно")

            ''' не нужно так как это редактирвоание а нам нужно удаление так как
            у группы есть права на них, если ужалить группу то и остальные ее права удаляются автоматически
            c.execute("SELECT id_music FROM музыки WHERE id_group = ? ", (row[0],))
            mus = c.fetchall()
            c.execute("SELECT id_album FROM альбом WHERE id_group = ? ", (row[0],))
            alb = c.fetchall()

            ## меняем id на нулевой у музыки и альбома, так как группа связяна с ним
            for i in mus:
                ##print("----hhhhhhhh ", i[0])                    
                admin_2_redakt.redaktirovanie(conn, 'музыки', i[0], '', 0, '', '')
            for i in alb:
                ##print("----hhhhhhhh ", i[0])                    
                admin_2_redakt.redaktirovanie(conn, 'альбом', i[0], '', 0, '', '')
            return
            '''

            c.execute("DELETE FROM музыки WHERE id_group = ?", (row[0],))
            print("удалено у музыки ")
            c.execute("DELETE FROM альбом WHERE id_group = ?", (row[0],))
            print("удалено у альбома ")

            conn.commit()

    elif (entry_id.get() not in ['', ' ']) and (entry_name.get() in ['', ' ']): ## удаление через ID
        ##удалять из категории(группы) где ID = ?
        SQL_Command = " FROM группы WHERE id_group = ?"
        c.execute("SELECT id_group" +SQL_Command, (entry_id.get(),))
        row = c.fetchone()
        c.execute("DELETE" + SQL_Command, (entry_id.get(),))
        print("DELETE___________group_______________T ", SQL_Command)
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через ID", "Data not found in the database")
        else:
            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
            messagebox.showinfo("Удаление через ID", "Удалено успешно")

            c.execute("DELETE FROM музыки WHERE id_group = ?", (row[0],))
            print("удалено у музыки ")
            c.execute("DELETE FROM альбом WHERE id_group = ?", (row[0],))
            print("удалено у альбома ")

            conn.commit()
    elif (entry_id.get() in ['', ' ']) and (entry_name.get() not in ['', ' ']): ## удаление через имя
        ##удалять из категории(группы) где имя = ?
        SQL_Command = " FROM группы WHERE name_group = ?"
        c.execute("SELECT id_group" +SQL_Command, (entry_name.get(),))
        row = c.fetchone()
        c.execute("DELETE" + SQL_Command, (entry_name.get(),))
        print("DELETE___________group_______________T ", SQL_Command)
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через имя", "Data not found in the database")
        else:
            print("✅DELETE____________ID______________T ", entry_id.get(), "  row = ", row[0])
            messagebox.showinfo("Удаление через имя", "Удалено успешно")

            c.execute("DELETE FROM музыки WHERE id_group = ?", (row[0],))
            print("удалено у музыки ")
            c.execute("DELETE FROM альбом WHERE id_group = ?", (row[0],))
            print("удалено у альбома ")

            conn.commit()
    else:
       print("ого не понятная ошибка жесть37829н428934")
       return
    

def delet_album(conn, entry_id, entry_name, id_music, id_group, id_zapis):
    c = conn.cursor()
    kol = 0
    SqlText =[]
    entText =[]
    if (entry_id.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_album = ')
        entText.append(entry_id.get())
    if (entry_name.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('name_album = ')
        entText.append(entry_name.get())
    if (id_music.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_music = ')
        entText.append(id_music.get())
    if (id_group.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_group = ')
        entText.append(id_group.get())
    if (id_zapis.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_zapis = ')
        entText.append(id_zapis.get())

    ## да, я знаю что можно проверить размер через массив, но не хочу
    ## Альбом удаляется только через ID либо через другие данные по одному-две
    if kol == 0:
        messagebox.showerror("Error kol = 0 😰", "Пустая строка при удалении _album")
        return
    ## проверка все строки не пустые
    elif kol > 2:
        messagebox.showerror("Error kol > 2 😰", "Много строк _album")
        return
    ## проверка все строки не пустые
    elif kol == 1:
        c.execute("DELETE FROM альбом WHERE " + SqlText[0] + "?", (entText[0],))
        print("DELETE___________альбом_______________T ", SqlText[0])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через один", "Data not found in the database")
        else:
            print("✅DELETE____________ID______________T " + SqlText[0] + "?")
            messagebox.showinfo("Удаление через один ", "Удалено успешно")
            conn.commit()

    elif kol == 2: 
        c.execute("DELETE FROM альбом WHERE " + SqlText[0] + "? AND " + SqlText[1] + "?", (entText[0], entText[1]))
        print("DELETE___________альбом_______________T " + SqlText[0] + " AND " + SqlText[1])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через два", "Data not found in the database")
        else:
            print("✅DELETE____________ID______________T " + SqlText[0] + " AND " + SqlText[1])
            messagebox.showinfo("Удаление через два", "Удалено успешно")
            conn.commit()
    else:
       print("ого не понятная ошибка жесть37829н428934")
       return
    
def delet_musicant(conn, id_author, name_au, family_au, id_group):
    c = conn.cursor()
    kol = 0
    SqlText =[]
    entText =[]
    if (id_author.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_author = ')
        entText.append(id_author.get())
    if (name_au.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('name_au = ')
        entText.append(name_au.get())
    if (family_au.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('family_au = ')
        entText.append(family_au.get())
    if (id_group.get() not in ['', ' ']): 
        kol = kol + 1
        SqlText.append('id_group = ')
        entText.append(id_group.get())

    ## да, я знаю что можно проверить размер через массив, но не хочу
    ## музыкант удаляется только через ID либо через другие данные по одному-две
    if kol == 0:
        messagebox.showerror("Error kol = 0 😰", "Пустая строка при удалении _музыкант")
        return
    elif kol == 1:
        c.execute("DELETE FROM музыкант WHERE " + SqlText[0] + "?", (entText[0],))
        print("DELETE___________музыкант_______________T ", SqlText[0])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через все", "Data not found in the database")
        else:
            print("✅DELETE___________музыкант_______________T " + SqlText[0] + "?")
            messagebox.showinfo("Удаление через один ", "Удалено успешно")
            conn.commit()
    elif kol == 2: 
        c.execute("DELETE FROM музыкант WHERE " + SqlText[0] + "? AND " + SqlText[1] + "?", (entText[0], entText[1]))
        print("DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через два", "Data not found in the database")
        else:
            print("✅DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
            messagebox.showinfo("Удаление через два", "Удалено успешно")
            conn.commit()
    elif kol == 3: 
        c.execute("DELETE FROM музыкант WHERE " + SqlText[0] + "? AND " + SqlText[1] + "? AND " + SqlText[2] + "?", (entText[0], entText[1], entText[2]))
        print("DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через три", "Data not found in the database")
        else:
            print("✅DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
            messagebox.showinfo("Удаление через три", "Удалено успешно")
            conn.commit()
    elif kol == 4: 
        c.execute("DELETE FROM музыкант WHERE " + SqlText[0] + "? AND " + SqlText[1] + "? AND " + SqlText[2] + "? AND " + SqlText[3] + "?", (entText[0], entText[1], entText[2], entText[3]))
        print("DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
        if c.rowcount == 0:  # Проверим не повлияла ли операция удаления на какие-либо строки
            messagebox.showerror("Удаление через все", "Data not found in the database")
        else:
            print("✅DELETE___________музыкант_______________T " + SqlText[0] + " AND " + SqlText[1])
            messagebox.showinfo("Удаление через все", "Удалено успешно")
            conn.commit()
    else:
       print("ого не понятная ошибка жесть37829н428934")
       return