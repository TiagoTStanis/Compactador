import zipfile
import os
import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk, filedialog
from PIL import Image, ImageTk
import sys


if hasattr(sys, '_MEIPASS'):
    icon_path = os.path.join(sys._MEIPASS, 'iconCompact.ico')
else:
    icon_path = 'iconCompact.ico'
    
def compactar_arquivo(caminho_arquivo):
    try:
        caminho_saida = os.path.splitext(caminho_arquivo)[0] + ".zip"
        
        progress_bar['value'] = 0
        root.update_idletasks()
        log_text.insert(tk.END, f"Compactando '{caminho_arquivo}'...\n")

        with zipfile.ZipFile(caminho_saida, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
            zipf.write(caminho_arquivo, os.path.basename(caminho_arquivo))
        
        progress_bar['value'] = 100
        root.update_idletasks()
        log_text.insert(tk.END, f"Compactação concluída com sucesso: '{caminho_saida}'\n")
        messagebox.showinfo("Sucesso", f"Arquivo compactado com sucesso em: {caminho_saida}")

    except Exception as e:
        log_text.insert(tk.END, f"Erro ao compactar '{caminho_arquivo}': {e}\n")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        log_text.insert(tk.END, f"Arquivo selecionado: {caminho_arquivo}\n")
        compactar_arquivo(caminho_arquivo)

root = tk.Tk()
root.title("Compactador de Arquivos")
root.geometry("500x450")
root.configure(bg="#1c1c1c")

try:
    icon_path = "iconCompact.ico"
    icon_image = ImageTk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon_image) 
except:
    pass

try:
    icon = PhotoImage(file="iconCompact.ico")
    root.iconphoto(False, icon)
except:
    pass

label = tk.Label(
    root,
    text="Selecione o arquivo para compactar",
    font=("Helvetica", 14, "bold"),
    fg="#ffffff",
    bg="#1c1c1c",
    pady=20,
)
label.pack()

select_button = tk.Button(
    root,
    text="Selecionar Arquivo",
    font=("Helvetica", 12),
    command=selecionar_arquivo,
    bg="#4CAF50",
    fg="#ffffff",
    padx=20,
    pady=10
)
select_button.pack(pady=20)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

log_text = tk.Text(root, height=10, bg="#333333", fg="#ffffff", font=("Helvetica", 10))
log_text.pack(pady=10, padx=10)
log_text.insert(tk.END, "Log de atividades:\n")

root.mainloop()
