import tkinter as tk
from tkinter import filedialog
from face.face_detect import Face_Detect
from face.face_skin_color import Face_Skin_Color
from utils.convert import distancia_eucliana


def ler_arquivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        F = Face_Detect(file_path)
        path = F.detect()
        skin_color = Face_Skin_Color(path)
        tom = skin_color.mean_color()
        cor = distancia_eucliana(tom)
        processar_conteudo(cor)
   


def processar_conteudo(conteudo):
    resultado = "Resultado das funções:\n" + conteudo[0] 

    texto_resultado.configure(state='normal')
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado)
    texto_resultado.configure(state='disabled')


# Restante do código ...


window = tk.Tk()
window.title("Leitor de Arquivos")

botao_selecionar = tk.Button(window, text="Selecionar Arquivo", command=ler_arquivo)
botao_selecionar.pack(pady=10)

texto_resultado = tk.Text(window, height=10, width=50)
texto_resultado.configure(state='disabled')
texto_resultado.pack()

window.mainloop()
