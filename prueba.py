from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from registro import RegistroApp
from bd import bd
import traceback
from info import Info
from existente import Existente
from confirmacion import VentanaConfirmacion

ctk.set_appearance_mode("light")  # pa que se vea blanco viejon

class Main_window(ctk.CTk):
    base = bd()
    data = base.Obtener_info_lista()
    base.Cerrar()

    tam = len(data)
    
    def confirmacion(self):
        app = Toplevel(ventana)
        confirn = VentanaConfirmacion(app)
        self.update()

    def abrir_registro(self):
        app = Toplevel(ventana)
        registro = RegistroApp(app)
        self.update()

    def obtener_info_completa(self):
        base = bd()
        data = base.obtener_info_derecha()
        base.Cerrar()
        return data

    def obtener_info_lista(self):
        base = bd()
        data = base.Obtener_info_lista()
        base.Cerrar()
        return data

    def updateOne(self):
        print("update entrando")
        self.lista_mascotas = self.obtener_info_lista()
        tam2 = len(self.lista_mascotas)
        if int(self.tam) < int(tam2):
            print("refrescando vista")
            new = self.lista_mascotas[-1]
            imagen3 = "imagenes/" + new[1]
            texto = new[2] + "\n" + new[3]
            image = Image.open(imagen3).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, texto, new[0])
            self.tam += 1
        else:
            print(self.tam, tam2)

    def update(self):
        for pet_id, img_icon, nombre, mascota in self.lista_mascotas:
            imagen3 = "imagenes/" + img_icon
            texto = "Dueño: " + nombre + "\n" + "Mascota: " + mascota
            image = Image.open(imagen3).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, texto, pet_id)

    def __init__(self):
        super().__init__()
        self.id = 0
        self.title("Selecciona tu Mascota")
        self.geometry("1080x720+400+60")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #boton de menu de hamburguesas*******************************************************************************
        self.menu_button = ctk.CTkButton(self, text="☰", command=self.toggle_menu, width=80, fg_color="lightgray", corner_radius=10)
        self.menu_button.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="nw")
        #**********************************************************************************************************
        
        #la barra azul de abajo
        self.footer_frame = ctk.CTkFrame(self, fg_color="lightblue")
        self.footer_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")
        self.footer_frame.grid_columnconfigure(0, weight=1)#pa centrar esto

        two_buttons_frame = ctk.CTkFrame(self.footer_frame, fg_color="lightblue")
        two_buttons_frame.grid(row=0, column=0, pady=10)

        self.register_button = ctk.CTkButton(
            two_buttons_frame, text="  Registrar ", 
            width=70, height=50, 
            fg_color="orange", 
            corner_radius=25, 
            command=lambda: self.abrir_registro()
        )
        self.register_button.grid(row=0, column=0, padx=5)

        self.boton_refresh = ctk.CTkButton(
            two_buttons_frame, 
            fg_color="orange", 
            text="Refrescar", 
            width=40, 
            height=50, 
            corner_radius=25, 
            command=lambda: self.updateOne()
        )
        self.boton_refresh.grid(row=0, column=1, padx=5)

        #todos los botones del menu de hamburgheas**************************************************************************************
        self.menu_frame = ctk.CTkFrame(self, fg_color="white")
        self.menu_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nw")
        self.menu_frame.grid_remove()
        
        self.about_button = ctk.CTkButton(self.menu_frame, text="Nota Medica", command=self.confirmacion, width=200)
        self.about_button.pack(pady=5)
        
        self.about_button = ctk.CTkButton(self.menu_frame, text="Agendar Cita", command=self.show_about, width=200)
        self.about_button.pack(pady=5)

        self.about_button = ctk.CTkButton(self.menu_frame, text="Sobre nosotros", command=self.show_about, width=200)
        self.about_button.pack(pady=5)

        self.help_button = ctk.CTkButton(self.menu_frame, text="Ayuda", command=self.show_help, width=200)
        self.help_button.pack(pady=5)
        
        self.logout_button = ctk.CTkButton(self.menu_frame, text="Cerrar sesión", command=self.popOut_cerrarsesion, width=200)
        self.logout_button.pack(pady=5)
        
        #********************************************************************************************************************************

        self.search_frame = ctk.CTkFrame(self, fg_color="white")
        self.search_frame.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Buscar Dueño", width=300)
        self.search_entry.pack(padx=10, pady=5)
        
        #*******************************todo el contenido de la lista de mascotas y barra desplazadora***********************************
        mascotas_frame_container = ctk.CTkFrame(self)
        mascotas_frame_container.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        
        self.mascotas_canvas = Canvas(mascotas_frame_container, bg="white", highlightthickness=0)
        self.mascotas_scrollbar = Scrollbar(mascotas_frame_container, orient="vertical", command=self.mascotas_canvas.yview)
        self.mascotas_dentro_frame = ctk.CTkFrame(self.mascotas_canvas, fg_color="white")

        self.mascotas_dentro_frame.bind("<Configure>", lambda e: self.mascotas_canvas.configure(scrollregion=self.mascotas_canvas.bbox("all")))
        self.mascotas_canvas.create_window(
            (0, 0), window=self.mascotas_dentro_frame, anchor="nw", tags="inner_frame", width=mascotas_frame_container.winfo_width()
        ) 
        self.mascotas_canvas.bind("<Configure>", lambda e: self.mascotas_canvas.itemconfig("inner_frame", width=e.width))
        self.mascotas_canvas.configure(yscrollcommand=self.mascotas_scrollbar.set)

        self.mascotas_canvas.pack(side="left", fill="both", expand=True)
        self.mascotas_scrollbar.pack(side="right", fill="y")

        self.lista_mascotas = self.obtener_info_lista()
        self.update()
        #********************************************************************************************************************************

        self.right_frame = ctk.CTkFrame(self, fg_color="#FFF8E1", width=300)
        self.right_frame.grid(row=1, column=2, padx=10, pady=0, sticky="nsew")
        self.right_frame.grid_propagate(False)

        self.content_frame = ctk.CTkFrame(self.right_frame, width=300, height=400)
        self.content_frame.pack_propagate(False)
        self.content_frame.pack(expand=True)

        initial_image = Image.open("imagenes/noseleccion.jpg").resize((300, 300))
        self.default_photo = ImageTk.PhotoImage(initial_image)

        self.text_label = ctk.CTkLabel(self.right_frame, text="Selecciona tu mascota", font=("Arial", 16))
        self.text_label.pack(pady=(0, 10))

        self.selected_image_label = ctk.CTkLabel(self.content_frame, image=self.default_photo, text="")
        self.selected_image_label.pack(pady=15)

        self.nombre_mascota = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 20), anchor='center')
        self.nombre_mascota.pack(pady=(0, 5))

        self.id_label = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 20), anchor='center')
        self.id_label.pack(pady=(0, 5))

        self.info_frame = ctk.CTkFrame(self.content_frame, fg_color="lightgray", corner_radius=10)
        self.info_frame.pack(pady=(10, 10), padx=10, fill="both", expand=True)

        self.owner_label = ctk.CTkLabel(self.info_frame, text="", font=("Arial", 16), anchor='w')
        self.owner_label.pack(pady=(5, 0))

        self.contact_label = ctk.CTkLabel(self.info_frame, text="", font=("Arial", 16), anchor='w')
        self.contact_label.pack(pady=(5, 10))

        self.full_info_button = ctk.CTkButton(self.content_frame, text="Ver información completa", command=lambda: self.show_full_info())
        self.full_info_button.pack(pady=(10, 10))

        self.lista_info_completa = self.obtener_info_completa()
        
    #crea la mascota y la pone en el frame de la lista
    def create_pet_item(self, image, text, pet_id):
        pet_frame = ctk.CTkFrame(self.mascotas_dentro_frame, fg_color=None)
        pet_frame.grid(row=self.mascotas_dentro_frame.grid_size()[1], column=0, padx=5, pady=15, sticky="ew")
        self.mascotas_dentro_frame.grid_columnconfigure(0, weight=1)

        pet_button = ctk.CTkButton(
            pet_frame, image=image, text="", width=100, height=100, fg_color=None, command=lambda img=image, txt=text, id=pet_id: self.display_pet_info(img, id)
        )
        pet_button.pack(side="left", padx=5)
        
        pet_label = ctk.CTkLabel(pet_frame, text=text, font=("Arial", 20), fg_color=None)
        pet_label.pack(side="left", padx=10, fill="x", expand=True)

        
    #muestra la info de la parte derecha
    def display_pet_info(self, image, pet_id):
        self.selected_image_label.configure(image=image)
        self.selected_image_label.image = image
        try:
            self.lista = self.obtener_info_completa()
            for tupla in self.lista:
                id, nombre, mascota, contacto = tupla
                self.id = id
                if id == pet_id:
                    self.nombre_mascota.configure(text=mascota)
                    self.id_label.configure(text=id)
                    self.owner_label.configure(text="Dueño: \n" + nombre + "\n")
                    self.contact_label.configure(text="Contacto: \n" + contacto)
                    break  # Terminar el bucle una vez se haya encontrado la mascota
        except Exception as e:
            print("Hubo un error: ", str(e))
            print(traceback.format_exc())

    def show_full_info(self):
        ven = Toplevel(ventana)
        app = Info(ven, self.id)
        
    def toggle_menu(self):
        """Alternar visibilidad del menú desplegable.""" 
        if self.menu_frame.winfo_ismapped():
            self.menu_frame.grid_remove()
            self.grid_columnconfigure(0, weight=0)
        else:
            self.menu_frame.grid()
            self.grid_columnconfigure(0, weight=0)
            
    #el pop out para cerrar la sessin, ya es funcional solo falta un poco mas de dise;o, 
    def popOut_cerrarsesion(self):
        self.popout = ctk.CTkToplevel()
        self.popout.geometry("300x150+700+300")
        self.popout.resizable(False, False)
        
        #con esto para que salga siempre enfrente
        self.popout.lift()
        self.popout.attributes("-topmost", True)
        
        #el label del pop out
        self.label_popOut = ctk.CTkLabel(self.popout, text="Estas seguro de que deseas cerrar sesion?", font=("Arial", 20), wraplength=250)
        self.label_popOut.pack(fill="both", pady = (10, 10), padx="10")
        
        #boton donde si damos 'si' se cierra la sesion, en teoria una vez se cierre te regresa a la pantalla de login
        self.cerrar = ctk.CTkButton(
            self.popout, 
            text="Si", 
            command=self.close_session, 
            fg_color="red", 
            corner_radius=10,
            width=150
        )
        self.cerrar.pack(fill="x" ,padx=(10,10) , side="left")
        
        #este es pa que no se cierre
        self.no_cerrar = ctk.CTkButton(   
            self.popout, 
            text="No", 
            command=self.no_close_session, 
            fg_color="green", 
            corner_radius=10, 
            width=150
        )
        self.no_cerrar.pack(fill="x" ,padx=(10,2) , side="left")

    def show_about(self):
        #--Mostrar información sobre la aplicacion.--# 
        ctk.CTkMessagebox.show_info("Sobre nosotros", "Este es un programa para gestionar mascotas.")

    #--Mostrar ayuda.--# 
    def show_help(self):
        ctk.CTkMessagebox.show_info("Ayuda", "Aquí puedes buscar y registrar mascotas.")

    #--Boton para cerrar secion--#
    def close_session(self):
        self.destroy()
        
    def no_close_session(self):
        self.popout.destroy()
        
ventana = Main_window()
ventana.mainloop()