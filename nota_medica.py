from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import Image, ImageTk
from bd import bd
ctk.set_appearance_mode("light")  # pa que se vea blanco viejon

class NotaMedica():
    def __init__(self, root):
        self.root = root
        self.id = id
        self.root.title("Creacion de nota medica")
        self.root.geometry("1080x720+400+60")
        self.root.config(bg="white")

        self.font = "Verdana"
        self.fontWidht = 14
        self.fontStyle = "bold"
        self.color1 = "#4d86ff"
        self.color2 = "#ff6d4d"
        
        self.image = Image.open("imagenes/huella.png")
        self.image = self.image.resize((130, 130))
        self.photo1 = ImageTk.PhotoImage(self.image)

        self.nota()

    def nota(self):

        # configuracion de los frames principales
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.topFrame = Frame(self.root, bg="#4d86ff")
        self.topFrame.grid(column=0, columnspan=2, row=0, sticky="nsew")
        self.leftFrame = customtkinter.CTkFrame(self.root, corner_radius=0)
        self.leftFrame.grid(column=0, row=1, sticky="nsew")
        self.rightFrame = Frame(self.root, bg="white")
        self.rightFrame.grid(column=1, row=1, sticky="nsew", pady=50, padx=(50,50))

        #configuracion del topFrame**********************************************************************************
        self.topFrame.columnconfigure(0, weight=1)
        self.topFrame.columnconfigure(1, weight=1)
        self.topFrame.columnconfigure(2, weight=1)

        self.menu_button = ctk.CTkButton(self.topFrame, text="☰", width=60,height=50, fg_color=self.color2, corner_radius=10)
        self.menu_button.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="w")

        titleLabel = Label(self.topFrame, text="Nota medica", font=("Verdana",25, "bold"), bg=self.color1, foreground="white")
        titleLabel.grid(row=0, column=1, sticky="nsew", padx=(0, 65))

        #configuracion del topFrame**********************************************************************************

        #configuracion del leftFrame*********************************************************************************
        centerFrame = customtkinter.CTkFrame(self.leftFrame, corner_radius=10, fg_color="white")
        centerFrame.pack(expand=True)

        nameLabel = Label(centerFrame, text="Nombre del cuidador", font=(self.font, self.fontWidht))
        nameLabel.pack(pady=(15,0))
        nameEntry = customtkinter.CTkEntry(centerFrame, placeholder_text="Introduzca el nombre del cuidador", width=300, height=50)
        nameEntry.pack(pady=(30,30))

        petLabel = Label(centerFrame, text="Nombre de la mascota", font=(self.font, self.fontWidht))
        petLabel.pack()
        petEntry = customtkinter.CTkEntry(centerFrame, placeholder_text="Introduzca el nombre de la mascota", width=300, height=50)
        petEntry.pack(pady=(30,30))

        raceLabel = Label(centerFrame, text="Raza de la mascota", font=(self.font, self.fontWidht))
        raceLabel.pack()
        raceEntry = customtkinter.CTkEntry(centerFrame, placeholder_text="Introduzca la raza de la mascota", width=300, height=50)
        raceEntry.pack(pady=(30,30))

        contactLabel = Label(centerFrame, text="Contacto del cuidador", font=(self.font, self.fontWidht))
        contactLabel.pack()
        contactEntry = customtkinter.CTkEntry(centerFrame, placeholder_text="Introduzca un correo de contacto", width=300, height=50)
        contactEntry.pack(pady=(30,30), padx= 50)

        imageLabel = customtkinter.CTkLabel(self.root, image=self.photo1)
        imageLabel.place(x=500, y=500)

        #configuracion del leftFrame*********************************************************************************

        #configuracion del rightFrame********************************************************************************

        self.rightFrame.columnconfigure(0, weight=1)
        self.rightFrame.columnconfigure(1, weight=1)
        self.rightFrame.rowconfigure(0, weight=1)
        self.rightFrame.rowconfigure(1, weight=1)
        self.rightFrame.rowconfigure(2, weight=1)
        self.rightFrame.rowconfigure(3, weight=1)
        self.rightFrame.rowconfigure(4, weight=1)

        dateLabel = Label(self.rightFrame, text="Fecha de consulta", font=(self.font, self.fontWidht))
        dateLabel.grid(column=0, row=0)
        dateEntry = customtkinter.CTkEntry(self.rightFrame, placeholder_text="dd/mm/aa", width=190, height=50)
        dateEntry.grid(column=0, row=1)

        timeLabel = Label(self.rightFrame, text="Hora de consulta", font=(self.font, self.fontWidht))
        timeLabel.grid(column=1, row=0)
        timeEntry = customtkinter.CTkEntry(self.rightFrame, placeholder_text="Introduzca la hora", width=190, height=50)
        timeEntry.grid(column=1, row=1)

        reasonLabel = Label(self.rightFrame, text="Motivo de la visita", font=(self.font, self.fontWidht))
        reasonLabel.grid(column=0, columnspan=2, row=2)
        reasonText = customtkinter.CTkTextbox(self.rightFrame, width=500, border_width=2)
        reasonText.grid(column=0, columnspan=2, row=3)

        btnSend = Button(self.rightFrame, text="Enviar", width=15, height=3, background=self.color2, font=(self.font, self.fontWidht, "bold"), foreground="white")
        btnSend.grid(column=0, row=4)

        btnPrint = Button(self.rightFrame, text="Imprimir", width=15, height=3, background=self.color2, font=(self.font, self.fontWidht, "bold"), foreground="white")
        btnPrint.grid(column=1, row=4)

if __name__ == "__main__":
    root = Tk()
    app = NotaMedica(root)
    root.mainloop()
