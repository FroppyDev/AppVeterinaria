from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from bd import bd

ctk.set_appearance_mode("light")  # pa que se vea blanco viejon

class Existente:
    def __init__(self, root):
        self.root = root
        root.geometry("900x600+500+100")
        
        # Crear la barra superior azul
        self.top_bar = ctk.CTkFrame(self.root, fg_color="lightblue")
        self.top_bar.grid(row=0, column=0, columnspan=3, sticky="ew")
        
        # boton pa regresar
        self.regresar_button = ctk.CTkButton(self.top_bar, text="⬅️ Regresar", command=self.back_window, width=80, fg_color="orange", corner_radius=10)
        self.regresar_button.pack(side="left", padx=(10,0), pady=10)
        
        # Etiqueta en la barra superior con el texto ese
        self.top_label = ctk.CTkLabel(self.top_bar, text="SELECCIONA LA MASCOTA", font=("Arial", 18), fg_color=None)
        self.top_label.pack(side="left",padx=(0,100),expand = True)
        
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(2, weight=1)
        
        self.search_entry = ctk.CTkEntry(root, placeholder_text="Buscar Dueño", width=500, height=40)
        self.search_entry.grid(row=1, column=1, pady = (20,0))
        
        # Frame con la barra desplazadora
        mascotas_frame_container = ctk.CTkFrame(self.root)
        mascotas_frame_container.grid(row=2, column=1, sticky="nsew", padx=20, pady=20, columnspan=2)

        self.mascotas_canvas = Canvas(mascotas_frame_container, bg="white", highlightthickness=0)
        self.mascotas_scrollbar = Scrollbar(mascotas_frame_container, orient="vertical", command=self.mascotas_canvas.yview)
        self.mascotas_dentro_frame = ctk.CTkFrame(self.mascotas_canvas, fg_color="white")
        self.mascotas_dentro_frame.grid(row=2, column=1)

        self.mascotas_dentro_frame.bind("<Configure>", lambda e: self.mascotas_canvas.configure(scrollregion=self.mascotas_canvas.bbox("all")))

        self.mascotas_canvas.create_window(
            (0, 0), window=self.mascotas_dentro_frame, anchor="nw", tags="inner_frame", width=mascotas_frame_container.winfo_width()
        )
        
        self.mascotas_canvas.bind("<Configure>", lambda e: self.mascotas_canvas.itemconfig("inner_frame", width=e.width))
        self.mascotas_canvas.configure(yscrollcommand=self.mascotas_scrollbar.set)

        self.mascotas_canvas.pack(side="left", fill="both", expand=True)
        self.mascotas_scrollbar.pack(side="right", fill="y")

        # Obtener lista de mascotas
        self.lista_mascotas = self.obtener_info_lista()
        self.update()
        
    def back_window(self):
        self.root.destroy()  # Cerrar ventana secundaria
        self.main_window.deiconify() 

    def next_window(self):
        pass

    def obtener_info_lista(self):
        base = bd()
        data = base.Obtener_info_lista()
        base.Cerrar()
        return data

    def update(self):
        for pet_id, img_icon, nombre, mascota in self.lista_mascotas:
            imagen3 = "imagenes/" + img_icon
            texto = "Dueño: " + nombre + "\n" + "Mascota: " + mascota
            image = Image.open(imagen3).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, texto, pet_id)
        
    def create_pet_item(self, image, text, pet_id):
        pet_frame = ctk.CTkFrame(self.mascotas_dentro_frame, fg_color=None)
        pet_frame.grid(row=self.mascotas_dentro_frame.grid_size()[1], column=0, padx=5, pady=15, sticky="ew")
        self.mascotas_dentro_frame.grid_columnconfigure(0, weight=1)

        # Boton con imagen de la mascota
        pet_button = ctk.CTkButton(
            pet_frame, image=image, text="", width=100, height=100, fg_color="#dab1bf", corner_radius=0, 
            command=lambda img=image, txt=text, id=pet_id: self.next_window(img, id)
        )
        pet_button.pack(side="left", padx=5)

        # Etiqueta con el texto de la mascota
        pet_label = ctk.CTkLabel(
            pet_frame, text=text, font=("Arial", 16), fg_color=None, anchor="w", width=300
        )
        pet_label.pack(side="left", padx=10, fill="x", expand=True)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Existente(root)
    root.mainloop()
