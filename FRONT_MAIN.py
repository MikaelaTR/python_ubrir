import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
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
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='График 1', variable=self.radio_var,command=self.graf1, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='График 2',variable=self.radio_var, command=self.graf2, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='График 3',variable=self.radio_var,command=self.graf3, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

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
        self.createNewWindow()
        return filePath

if __name__ == "__main__":

    app = App()
    app.mainloop()
