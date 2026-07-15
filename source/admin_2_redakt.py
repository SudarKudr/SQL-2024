import sqlite3
import tkinter as tk
from tkinter import messagebox

import main
import admin_1_Work

##редактирование через ID потому что оно уникальнее!
## у😰😰😰 музыканта😰😰😰 другое реадкиторание
##                  id   для всех
##                name   для всех
##
## id_group_OR_country   для всех (группа только id_страна, музыка и альбом - id_group)
##
##           id_zapisi   для музыка и альбом
##     id_mus_or_zhanr   для музыка(zhanr ) и альбом(mus)
'''
UPDATE table_name SET столбец1=value,
столбец2=значение ГДЕ условие;
'''
def redaktirovanie(conn, category, id, name, id_grp, id_zapis, id_mus_or_zhanr):
    c = conn.cursor()
    if (id in ['', ' ']):
        messagebox.showerror("Error 444 😰 редактирование", "Пустая ID😰😰😰")
        return
    else: ## если группа, то остальные переменные поставь "" (пустые)
        if (name in ['', ' ']) and (id_grp in ['', ' ']) and (id_zapis in ['', ' ']) and (id_mus_or_zhanr in ['', ' ']):
            messagebox.showerror("Error 555 😰", "Пустая строка при редактирвоании")
            return
        elif category == 'альбом': ## 🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗
            print("SSSSSelect было = ", id, name, id_grp, id_zapis, id_mus_or_zhanr)
            if (name  in ['', ' ']):
                c.execute("SELECT name_album FROM альбом WHERE id_album = ?", (id,))
                name = c.fetchone()[0]
                print("Select альбом, name = ", name)
            if (id_mus_or_zhanr in ['', ' ']):
                c.execute("SELECT id_music FROM альбом WHERE id_album = ?", (id,))
                id_mus_or_zhanr = c.fetchone()[0]
                print("Select альбом, id_music = ", id_mus_or_zhanr)
            if (id_grp in ['', ' ']):
                c.execute("SELECT id_group FROM альбом WHERE id_album = ?", (id,))
                id_grp = c.fetchone()[0]
                print("Select альбом, id_group = ", id_grp)
            if (id_zapis in ['', ' ']):
                c.execute("SELECT id_zapis FROM альбом WHERE id_album = ?", (id,))
                id_zapis = c.fetchone()[0]
                print("Select альбом, id_zapis = ", id_zapis)
            print("SSSSSelect итог = ", id, name, id_grp, id_zapis, id_mus_or_zhanr)
            
            c.execute("SELECT COUNT(*) FROM альбом WHERE name_album = ? AND id_group = ? AND id_zapis = ? AND id_music = ? ", (name, id_grp, id_zapis, id_mus_or_zhanr))
            count = c.fetchone()[0]
            if count == 0:
                SQL_Command = "UPDATE альбом SET name_album = ?, id_group = ?, id_zapis = ?, id_music = ? WHERE id_album = ?"
                c.execute(SQL_Command, (name, id_grp, id_zapis, id_mus_or_zhanr, id))
                messagebox.showinfo("Успех", "Редактирование успешно")
                if c.rowcount > 0:
                    conn.commit()
                    print("Table successfully updated")
                    print("____альбом________РЕДАКТИРОВАНО_____________ ", SQL_Command)
                else:
                    print("Table update failed 'альбом' ")
            else:
                messagebox.showerror("Повтор", "Повтор при редактировании")
                print("Повтор при редактировании")

        elif category == 'музыки':
            print("SSSSSelect было = ", id, name, id_grp, id_zapis, id_mus_or_zhanr)
            if (name  in ['', ' ']):
                c.execute("SELECT name_music FROM музыки WHERE id_music = ?", (id,))
                name = c.fetchone()[0]
                print("Select музыки, name = ", name)
            if (id_grp in ['', ' ']):
                c.execute("SELECT id_group FROM музыки WHERE id_music = ?", (id,))
                id_grp = c.fetchone()[0]
                print("Select музыки, id_group = ", id_grp)
            if (id_zapis in ['', ' ']):
                c.execute("SELECT id_zapis FROM музыки WHERE id_music = ?", (id,))
                id_zapis = c.fetchone()[0]
                print("Select музыки, id_zapis = ", id_zapis)
            if (id_mus_or_zhanr in ['', ' ']):
                c.execute("SELECT id_zhanr FROM музыки WHERE id_music = ?", (id,))
                id_mus_or_zhanr = c.fetchone()[0]
                print("Select музыки, id_zhanr = ", id_mus_or_zhanr)
            print("SSSSSelect итог = ", id, name, id_grp, id_zapis, id_mus_or_zhanr)
            
            c.execute("SELECT COUNT(*) FROM музыки WHERE name_music = ? AND id_group = ? AND id_zapis = ? AND id_zhanr = ? ", (name, id_grp, id_zapis, id_mus_or_zhanr))
            count = c.fetchone()[0]
            if count == 0:
                SQL_Command = "UPDATE музыки SET name_music = ?, id_group = ?, id_zapis = ?, id_zhanr = ? WHERE id_music = ?"
                c.execute(SQL_Command, (name, id_grp, id_zapis, id_mus_or_zhanr, id))
                messagebox.showinfo("Успех", "Редактирование успешно")
                if c.rowcount > 0:
                    conn.commit()
                    print("Table successfully updated")
                    print("____музыки________РЕДАКТИРОВАНО_____________ ", SQL_Command)
                else:
                    print("Table update failed 'музыки' ")
            else:
                messagebox.showerror("Повтор", "Повтор при редактировании")
                print("Повтор при редактировании")
        else: 
            print("ого Не понятная ошибка")
    conn.commit()



def redaktirovanie_musicant(conn, id, name, family, id_gr): ##🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸
    c = conn.cursor()
    if (id in ['', ' ']):
        messagebox.showerror("Error 444_mus 😰 редактирование", "Пустая ID😰😰😰")
        return
    else:
        if (name in ['', ' ']) and (family in ['', ' ']) and (id_gr in ['', ' ']):
            messagebox.showerror("Error 555_mus 😰", "Пустая строка при редактирвоании")
            return
        else: ##                              🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸
            print("🎸 Select было = ", id, name, family, id_gr)
            if (name  in ['', ' ']):
                c.execute("SELECT name_au FROM музыкант WHERE id_author = ?", (id,))
                name = c.fetchone()[0]
                print("Select музыкант, name = ", name)
            if (family in ['', ' ']):
                c.execute("SELECT family_au FROM музыкант WHERE id_author = ?", (id,))
                family = c.fetchone()[0]
                print("Select музыкант, family = ", family)
            if (id_gr in ['', ' ']):
                c.execute("SELECT id_group FROM музыкант WHERE id_author = ?", (id,))
                id_gr = c.fetchone()[0]
                print("Select музыкант, id_group = ", id_gr)
            print("🎸 Select итог = ", id, name, family, id_gr)
            
            c.execute("SELECT COUNT(*) FROM музыкант WHERE name_au = ? AND family_au = ? AND id_group = ?", (name, family, id_gr))
            count = c.fetchone()[0]
            if count == 0:
                SQL_Command = "UPDATE музыкант SET name_au = ?, family_au = ?, id_group = ? WHERE id_author = ?"
                c.execute(SQL_Command, (name, family, id_gr, id))
                messagebox.showinfo("Успех", "Редактирование успешно")
                if c.rowcount > 0:
                    conn.commit()
                    print("Table successfully updated")
                    print("____музыкант________РЕДАКТИРОВАНО_____________ ", SQL_Command)
                else:
                    print("Table update failed redaktirovanie_musicant")
            else:
                messagebox.showerror("Повтор", "Повтор при редактировании")
                print("Повтор при редактировании")
    conn.commit()

def redaktirovanie_Zhanr_typeZapis_country(conn, categore, id, name): ##🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
    c = conn.cursor()
    if (id in ['', ' ']):
        messagebox.showerror("Error 444_type 😰 редактирование", "Пустая ID😰😰😰")
        return
    else:
        if (name in ['', ' ']):
            messagebox.showerror("Error 555_type 😰", "Пустая строка при редактирвоании")
            return
        else: ##                              🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
            c.execute("SELECT * FROM {}".format(categore))
            field_names = [i[0] for i in c.description]

            SQL_Commande = "SELECT COUNT(*) FROM " + categore + " WHERE " + field_names[1] + " = ?"
            c.execute(SQL_Commande, (name,))
            count = c.fetchone()[0]
            if count == 0:
                SQL_Commande = "UPDATE " + categore + " SET " + field_names[1] + " = ? WHERE " + field_names[0] + " = ?"
                c.execute(SQL_Commande, (name, id))
                messagebox.showinfo("Успех", "Редактирование успешно")
                if c.rowcount > 0:
                    conn.commit()
                    print("Table successfully updated")
                    print("____типЗаписи Жанр Страна________РЕДАКТИРОВАНО_____________ ", SQL_Commande)
                else:
                    print("Table update failed redaktirovanie_Zhanr_typeZapis_country")
            else:
                messagebox.showerror("Повтор", "Повтор при редактировании")
                print("Повтор при редактировании")
    conn.commit()   
                
def redaktirovanie_Group(conn, id_g, name_g, id_country, delet): ##ГРУППА ГРУППА ГРУППА ГРУППА ГРУППА
    c = conn.cursor()
    if (id_g in ['', ' ']):
        messagebox.showerror("Error 444_g 😰 редактирование", "Пустая ID😰😰😰")
        return
    else:
        if (name_g in ['', ' ']) and (id_country in ['', ' ']):
            messagebox.showerror("Error 555_g 😰", "Пустая строка при редактирвоании")
            return
        else: ##                              ГРУППА ГРУППА ГРУППА ГРУППА ГРУППА
            print("Select было = ", id_g, name_g, id_country)
            if (name_g in ['', ' ']):
                c.execute("SELECT name_group FROM группы WHERE id_group = ?", (id_g,))
                name_g = c.fetchone()[0]
                print("Select имя группы, name_group = ", name_g)
            if (id_country in ['', ' ']):
                c.execute("SELECT id_country FROM группы WHERE id_group = ?", (id_g,))
                id_country = c.fetchone()[0]
                print("Select группы, id_country = ", id_country)
            print("Select итог = ", id_g, name_g, id_country)
            
            c.execute("SELECT COUNT(*) FROM группы WHERE name_group = ?", (name_g,))
            count = c.fetchone()[0]
            if count == 0 or delet == 'Del':
                SQL_Command = "UPDATE группы SET name_group = ?, id_country = ? WHERE id_group = ?"
                c.execute(SQL_Command, (name_g, id_country, id_g))
                messagebox.showinfo("Успех", "Редактирование успешно")
                if c.rowcount > 0:
                    conn.commit()
                    print("Table successfully updated")
                    print("____группы________РЕДАКТИРОВАНО_____________ ", SQL_Command)
                else:
                    print("Table update failed redaktirovanie_Group")
            else:
                messagebox.showerror("Повтор", "Повтор при редактировании, нельзя две одинаковой группы")
                print("Повтор при редактировании")
    conn.commit()
# Commit changes to the database