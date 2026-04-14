import tkinter as tk

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.geometry("350x250")
        self.root.configure(bg="#202124")
        self.root.resizable(False, False)
        
        self.tempo_foco = 1500
        self.tempo_pausa = 300
        self.tempo = self.tempo_foco
        self.rodando = False
        self.modo = "Foco"
        
        self.cor_foco = "#f28b82"
        self.cor_pausa = "#81c995"
        self.cor_bg = "#202124"
        self.cor_fg = "#e8eaed"
        self.cor_btn = "#303134"
        self.fonte_principal = ("Segoe UI", 56)
        self.fonte_secundaria = ("Segoe UI", 14)
        
        self.frame = tk.Frame(root, bg=self.cor_bg)
        self.frame.pack(expand=True)
        
        self.lbl_modo = tk.Label(self.frame, text=self.modo, font=self.fonte_secundaria, bg=self.cor_bg, fg=self.cor_foco)
        self.lbl_modo.pack(pady=(0, 5))
        
        self.label = tk.Label(self.frame, text="25:00", font=self.fonte_principal, bg=self.cor_bg, fg=self.cor_fg)
        self.label.pack(pady=5)
        
        self.frame_botoes = tk.Frame(self.frame, bg=self.cor_bg)
        self.frame_botoes.pack(pady=15)
        
        self.btn_iniciar = tk.Button(self.frame_botoes, text="Iniciar", font=self.fonte_secundaria, bg=self.cor_btn, fg=self.cor_fg, activebackground="#3c4043", activeforeground=self.cor_fg, relief="flat", width=10, cursor="hand2", command=self.iniciar)
        self.btn_iniciar.pack(side=tk.LEFT, padx=10)
        
        self.btn_parar = tk.Button(self.frame_botoes, text="Parar", font=self.fonte_secundaria, bg=self.cor_btn, fg=self.cor_fg, activebackground="#3c4043", activeforeground=self.cor_fg, relief="flat", width=10, cursor="hand2", command=self.parar)
        self.btn_parar.pack(side=tk.RIGHT, padx=10)
        
        self.atualizar_interface()

    def atualizar(self):
        if self.rodando and self.tempo > 0:
            self.tempo -= 1
            self.atualizar_interface()
            self.root.after(1000, self.atualizar)
        elif self.tempo == 0:
            self.alternar_modo()

    def alternar_modo(self):
        if self.modo == "Foco":
            self.modo = "Pausa"
            self.tempo = self.tempo_pausa
            self.lbl_modo.config(fg=self.cor_pausa)
        else:
            self.modo = "Foco"
            self.tempo = self.tempo_foco
            self.lbl_modo.config(fg=self.cor_foco)
            
        self.lbl_modo.config(text=self.modo)
        self.atualizar_interface()
        self.root.after(1000, self.atualizar)

    def atualizar_interface(self):
        m, s = divmod(self.tempo, 60)
        self.label.config(text=f"{m:02d}:{s:02d}")

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar()

    def parar(self):
        self.rodando = False

if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro(root)
    root.mainloop()
