import tkinter as tk
from tkinter import messagebox

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.geometry("300x150")
        
        self.tempo = 1500
        self.rodando = False
        
        self.label = tk.Label(root, text="25:00", font=("Arial", 40))
        self.label.pack(pady=10)
        
        self.btn_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar)
        self.btn_iniciar.pack(side=tk.LEFT, padx=30)
        
        self.btn_parar = tk.Button(root, text="Parar", command=self.parar)
        self.btn_parar.pack(side=tk.RIGHT, padx=30)
        
        self.atualizar()

    def atualizar(self):
        if self.rodando and self.tempo > 0:
            self.tempo -= 1
            m, s = divmod(self.tempo, 60)
            self.label.config(text=f"{m:02d}:{s:02d}")
            self.root.after(1000, self.atualizar)
        elif self.tempo == 0:
            self.rodando = False
            messagebox.showinfo("Fim", "Tempo esgotado.")

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