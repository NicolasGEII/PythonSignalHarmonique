import customtkinter
from funct import func_type

# class pricipale
class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        #### Window #####
        self.title("Harmonique")
        self.geometry("480x360")
        self.minsize(480, 360)
        self.maxsize(480, 360)
        self.grid_columnconfigure(0)
        self.grid_rowconfigure(0)
        
        theme, color_theme = "dark", "green"

        self.x: list
        self.y: list

        customtkinter.set_appearance_mode(theme)
        customtkinter.set_default_color_theme(color_theme)

        ##### widget #####
        # Harmonique Slider
        self.slide_frame = Harm_frame(self)
        self.slide_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nw")

        # bouton calcul
        self.button = customtkinter.CTkButton(self, text="Afficher", command=self.button_callbck)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="se")

        self.protocol("WM_DELETE_WINDOW", self.quit)

    def button_callbck(self) -> None:
        func_type(self.slide_frame.func_box.get(), self.slide_frame.nb_harm)


# frame pour les harmoniques
class Harm_frame(customtkinter.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        #### Var ####
        self.nb_harm: int = 0

        # label
        self.lb_harm = customtkinter.CTkLabel(self, text="Nombre(s) d'harmonique: 0")
        self.lb_harm.grid(row=0, column=0,padx=(20,0), pady=20, sticky="nw")

        # slider harmonique
        self.harm_slide = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        self.harm_slide.set(0)
        self.harm_slide.grid(row=1, column= 0, padx=20, pady=20)


        self.label = customtkinter.CTkLabel(self, text="Type de fonction: ")
        self.label.grid(row= 2, column=0, padx=(10, 0), pady=10, sticky="nw")
        
        # Combo Box
        self.func_box = customtkinter.CTkComboBox(self, values=["carré", "triangle", "scie"])
        self.func_box.grid(row=2, column=1, padx=(0, 10), pady=(10,10), sticky="nw")

    def slider_event(self, value) -> None:
        self.nb_harm = int(value)
        self.lb_harm.configure(text= f"Nombre(s) d'harmonique: {int(value)}")
