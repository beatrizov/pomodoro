import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Configuração global do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PomodoroPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pomodoro Pro")
        self.geometry("400x480")
        self.resizable(False, False)

        # Variáveis de controle
        self.tempo_foco = 25 * 60
        self.tempo_pausa = 5 * 60
        self.tempo_restante = self.tempo_foco
        self.rodando = False
        self.modo = "Foco"
        self.ciclos_concluidos = 0
        self.sempre_no_topo = False

        self.setup_ui()

    def setup_ui(self):
        # Frame Principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=20)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Botão Pin (Sempre no Topo)
        self.btn_pin = ctk.CTkButton(self.main_frame, text="📌", width=35, height=35, 
                                     fg_color="transparent", hover_color="#333333",
                                     command=self.toggle_pin)
        self.btn_pin.place(x=10, y=10)

        # Label do Modo
        self.lbl_modo = ctk.CTkLabel(self.main_frame, text=self.modo.upper(), 
                                     font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
                                     text_color="#f28b82")
        self.lbl_modo.pack(pady=(40, 0))

        # Timer (Display Principal)
        self.lbl_timer = ctk.CTkLabel(self.main_frame, text="25:00", 
                                      font=ctk.CTkFont(family="Segoe UI", size=80, weight="bold"))
        self.lbl_timer.pack(pady=5)

        # Barra de Progresso
        self.progresso = ctk.CTkProgressBar(self.main_frame, width=300, height=10,
                                           progress_color="#f28b82")
        self.progresso.set(1.0)
        self.progresso.pack(pady=15)

        # Contador de Ciclos
        self.lbl_ciclos = ctk.CTkLabel(self.main_frame, text=f"Sessões concluídas: {self.ciclos_concluidos}", 
                                       font=ctk.CTkFont(family="Segoe UI", size=14))
        self.lbl_ciclos.pack(pady=5)

        # Botões de Controle
        self.btn_start = ctk.CTkButton(self.main_frame, text="INICIAR", 
                                       font=ctk.CTkFont(size=16, weight="bold"),
                                       fg_color="#303134", hover_color="#3c4043",
                                       height=45, corner_radius=10, command=self.controlar_timer)
        self.btn_start.pack(pady=20)

        self.btn_reset = ctk.CTkButton(self.main_frame, text="Resetar", 
                                       font=ctk.CTkFont(size=13),
                                       fg_color="transparent", border_width=1,
                                       hover_color="#333333",
                                       corner_radius=10, command=self.resetar_timer)
        self.btn_reset.pack(pady=0)

    def controlar_timer(self):
        if not self.rodando:
            self.rodando = True
            self.btn_start.configure(text="PAUSAR", fg_color="#f28b82", text_color="black")
            self.atualizar_contagem()
        else:
            self.rodando = False
            self.btn_start.configure(text="RETOMAR", fg_color="#303134", text_color="white")

    def atualizar_contagem(self):
        if self.rodando and self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.atualizar_interface()
            self.after(1000, self.atualizar_contagem)
        elif self.tempo_restante == 0:
            self.finalizar_ciclo()

    def atualizar_interface(self):
        minutos, segundos = divmod(self.tempo_restante, 60)
        self.lbl_timer.configure(text=f"{minutos:02d}:{segundos:02d}")
        
        # Atualiza o preenchimento da barra de progresso
        total = self.tempo_foco if self.modo == "Foco" else self.tempo_pausa
        self.progresso.set(self.tempo_restante / total)

    def finalizar_ciclo(self):
        self.rodando = False
        self.bell() # Emite um sinal sonoro do sistema
        
        if self.modo == "Foco":
            self.ciclos_concluidos += 1
            self.lbl_ciclos.configure(text=f"Sessões concluídas: {self.ciclos_concluidos}")
            self.modo = "Pausa"
            self.tempo_restante = self.tempo_pausa
            self.lbl_modo.configure(text="PAUSA", text_color="#81c995")
            self.progresso.configure(progress_color="#81c995")
        else:
            self.modo = "Foco"
            self.tempo_restante = self.tempo_foco
            self.lbl_modo.configure(text="FOCO", text_color="#f28b82")
            self.progresso.configure(progress_color="#f28b82")
            
        self.atualizar_interface()
        self.btn_start.configure(text="INICIAR PRÓXIMO", fg_color="#303134", text_color="white")
        messagebox.showinfo("Pomodoro Pro", f"Ciclo finalizado! Próximo: {self.modo}")

    def resetar_timer(self):
        self.rodando = False
        self.tempo_restante = self.tempo_foco if self.modo == "Foco" else self.tempo_pausa
        self.atualizar_interface()
        self.btn_start.configure(text="INICIAR", fg_color="#303134", text_color="white")

    def toggle_pin(self):
        self.sempre_no_topo = not self.sempre_no_topo
        self.attributes("-topmost", self.sempre_no_topo)
        # Feedback visual no botão de pin
        self.btn_pin.configure(fg_color="#f28b82" if self.sempre_no_topo else "transparent",
                               text_color="black" if self.sempre_no_topo else "white")

if __name__ == "__main__":
    app = PomodoroPro()
    app.mainloop()