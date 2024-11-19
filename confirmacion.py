import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from existente import Existente

class VentanaConfirmacion():
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Ejemplo")
        self.root.geometry("800x400+550+200")
        self.root.configure(bg="white")

        # Barra azul en la parte superior
        self.top_bar = tk.Frame(self.root, bg="lightblue", height=30)
        self.top_bar.pack(fill="x")

        self.regresar_boton = tk.Button(self.top_bar, text="⬅️ Regresar", bg="orange", fg="white", borderwidth=0, font=("Arial", 18), command=self.back_window)
        self.regresar_boton.pack(side="left", padx=10, pady=5)

        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(expand=True, fill="both")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.image_width, self.image_height = 150, 150

        self.hamster_image = self.cargar_imagenes("imagenes/hamster_icon.jpg")
        self.cancel_image = self.cargar_imagenes("imagenes/cancel.png")

        self.create_buttons()
        
    def back_window(self):
        self.root.destroy()

    def cargar_imagenes(self, filepath):
        """Cargar y redimensionar una imagen"""
        img = Image.open(filepath)
        img = img.resize((self.image_width, self.image_height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def existente_window(self):
        app = Toplevel(self.root)
        nota = Existente(app)
        self.update()
        

    def desconocido_window(self):
        pass

    def create_buttons(self):
        """Crear los botones con las imágenes y los textos"""
        hamster_button = tk.Button(self.main_frame, image=self.hamster_image, bg="#b3e5fc", borderwidth=0, command=self.existente_window)
        hamster_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        existente_label = tk.Label(self.main_frame, text="Existente", font=("Arial", 14), bg="white")
        existente_label.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        cancel_button = tk.Button(self.main_frame, image=self.cancel_image, bg="#b3e5fc", borderwidth=0, command=self.desconocido_window)
        cancel_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        desconocido_label = tk.Label(self.main_frame, text="Desconocido", font=("Arial", 14), bg="white")
        desconocido_label.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaConfirmacion(root)
    root.mainloop()
