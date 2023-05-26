import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
import numpy as np
from datetime import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
n = 100
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('iccco.ico')

        # configure window
        self.title("Urfu Lens")
        self.geometry(f"{1200}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        x = '0.png'
        img = Image.open(x)
        img = img.resize((800, 600), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=0, column=1, padx=20)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_button_1 =  customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],                                                                      command=self.change_appearance_mode_event)
        self.sidebar_button_1.grid(row=1, column=1, padx=20, pady=30)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Настройки", command=self.createSitingWindow)
        self.sidebar_button_3.grid(row=2, column=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Выберите рабочий DataSet", state='disabled')
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self,text='Выбрать',command=self.getLocalFile, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Виды графиков", text_color=("gray10", "#DCE4EE"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='Круговая диаграмма', variable=self.radio_var,command=self.graf1, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="nsew")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='Ломанный график',variable=self.radio_var, command=self.graf2, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="nsew")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='Плитка',variable=self.radio_var,command=self.graf3, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="nsew")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def graf1(self):
        x = '1.png'
        img = Image.open(x)
        img = img.resize((800, 600), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=0, column=1, padx=20)

    def graf2(self):
        x = '2.png'
        img = Image.open(x)
        img = img.resize((800, 600), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=0, column=1, padx=20)

    def graf3(self):
        x = '3.png'
        img = Image.open(x)
        img = img.resize((800, 600), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=0, column=1, padx=20)

    def createSitingWindow(root):
        root = Tk()
        root.title("Настройки")
        root.geometry(f"{900}x{600}")
        root.configure(background='black')
        root.iconbitmap('iccco.ico')
        # create sidebar frame with widgets

        root.radiobutton_frame = customtkinter.CTkFrame(root)
        root.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        root.radio_var = tkinter.IntVar(value=0)
        root.label_radio_group = customtkinter.CTkLabel(master=root.radiobutton_frame, text="Rows on output",
                                                        text_color=("gray10", "#DCE4EE"))
        root.label_radio_group.grid(row=0, column=1, padx=10, pady=10, sticky="")
        global n
        root.entry = customtkinter.CTkEntry(master=root.radiobutton_frame, placeholder_text=n)
        root.entry.grid(row=0, column=2)
        n = root.placeholder_text
    def Simpletoggle(root):

        if root.toggle_button.config('text')[-1] == 'ON':
            root.toggle_button.config(text='OFF')
        else:
            root.toggle_button.config(text='ON')
    def createNewWindow(root):
        root = Tk()
        root.title("Обзор выбранного файла")
        root.geometry(f"{900}x{600}")
        root.configure(background='black')
        root.iconbitmap('iccco.ico')
        root.grid_columnconfigure(1, weight=1)
        my_game = ttk.Treeview(root)
        global columns
        my_game['columns'] = (columns[0])
        my_game.column("#0", width=0, stretch=NO)
        for i in columns[0]:
         my_game.column(i, anchor=CENTER,width=80)
        for i in columns[0]:
         my_game.heading(i, anchor=CENTER, text=i)
        global n
        for i in range(1,n,1):
            my_game.insert(parent='', index='end', text='',
                       values=(columns[i]))

        my_game.pack(expand=tk.YES, fill=tk.BOTH)
        root.mainloop()

    def getLocalFile(self):
        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        self.entry.configure(state="normal")
        self.entry = customtkinter.CTkEntry(self, placeholder_text=filePath)
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry.configure(state="disabled")
        print("Путь файла:", filePath)
        name = list((filePath.replace('/',' ').split()))
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text=name[-1],
                                                        command=self.createNewWindow,fg_color='grey')
        self.sidebar_button_4.grid(row=4, column=1,pady=20)
        global columns
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            columns = []
            for row in csv_reader:
                columns.append(row)
        df = pd.read_csv(filePath)
        df.head()
        df['rep_date'] = df['rep_date'].apply(
            lambda x: datetime.strptime(x, '%m/%d/%Y'))
        df["date_today"] = date.today()
        df['date_today'] = pd.to_datetime(df['date_today'], format='%Y/%m/%d')
        df["Recency"] = \
            (df["date_today"] - df["rep_date"]).dt.days
        df = df.sort_values(by='partner ', ascending=True)
        rfm = (df.pivot_table(index="partner ",
                              values=["monetary", "Recency"],
                              aggfunc={"Recency": np.min, "monetary": [np.sum, len]},
                              fill_value=0))
        rfm["Av_sum"] = rfm['monetary', 'sum'] / rfm['monetary', 'len']
        rfm.columns = ['recency', 'frequency', 'monetary', 'AVG_SUM']
        rfm['R'] = pd.qcut(rfm['recency'],
                           q=3,
                           labels=[3, 2, 1])
        rfm['F'] = pd.qcut(rfm['frequency'],
                           q=4,
                           labels=[1, 2, 3], duplicates='drop')
        rfm['M'] = pd.qcut(rfm['AVG_SUM'],
                           q=3,
                           labels=[1, 2, 3], duplicates='drop')
        rfm["RFM"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)
        p_rfm = pd.DataFrame()
        p_rfm['Частота'] = rfm['frequency']
        p_rfm['Средний_чек'] = rfm['AVG_SUM']
        p_rfm['Статус'] = ['Потерянный' if x == '111' or x == '112' or x == '113'
                           else 'Уходящие' if x == '121' or x == '122' or x == '123'
        else 'Уходящие лояльные' if x == '131' or x == '132' or x == '133'
        else 'Спящие' if x == '211' or x == '212' or x == '213' or x == '221' or x == '222' or x == '223'
        else 'Спящие лояльные' if x == '231' or x == '232' or x == '233'
        else 'Новички' if x == '311' or x == '312'
        else 'Лояльные новички' if x == '313' or x == '321' or x == '322'
        else 'Постоянные со средним чеком' if x == '323'
        else 'Постоянные лояльные с маленьким чеком' if x == '331'
        else 'Постоянные лояльные с средним чеком' if x == '332'
        else 'VIP' for x in rfm['RFM']]
        cat_totals = p_rfm.groupby("Статус").size()
        figure(figsize=(12, 8), dpi=100)
        cat_totals.plot(kind="pie", label="", labeldistance=1.05, autopct='%1.1f%%', radius=1, pctdistance=0.75,
                        shadow=1)
        plt.savefig('1.png', bbox_inches='tight')
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        x_data = []

        def lineplot(x_data, y_data, x_label="Месяц", y_label="Кол-во клиентов по месяцам",
                     title="Распределение клиентов по месяцам"):
            # Create the plot object
            _, ax = plt.subplots()

            # Plot the best fit line, set the linewidth (lw), color and
            # transparency (alpha) of the line
            ax.plot(x_data, y_data, marker='*', lw=2, color='#539caf', alpha=1)
            plt.locator_params(axis='both', integer=True, tight=True)

            # Label the axes and provide a title
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            plt.savefig('2.png', bbox_inches='tight')

        def data_po_month():
            df = pd.read_csv(filePath)
            df.head()
            df['rep_date'] = df['rep_date'].apply(
                lambda x: datetime.strptime(x, '%m/%d/%Y'))
            df['rep_date'] = pd.to_datetime(df['rep_date']).dt.month
            data_grp = df.groupby('rep_date').size()
            elements_count = len(data_grp)
            for i in range(elements_count):
                x_data.append(months[i])
            lineplot(x_data, data_grp)

        data_po_month()
        self.createNewWindow()
        return filePath

if __name__ == "__main__":

    app = App()
    app.mainloop()
