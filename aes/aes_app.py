from tkinter import filedialog, messagebox
from main import AES
import tkinter as tk
import os


class AESApp:
    def __init__(self, master):
        self.master = master
        master.title("AES File Encryptor")

        self.label = tk.Label(master, text="Selecione o arquivo para criptografar ou descriptografar:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Selecionar Arquivo", command=self.select_file)
        self.select_button.pack()

        self.filename_label = tk.Label(master, text="")
        self.filename_label.pack(pady=5)

        self.save_label = tk.Label(master, text="Nome do arquivo de saída (com extensão):")
        self.save_label.pack(pady=5)

        self.output_name = tk.Entry(master)
        self.output_name.pack()

        self.key_label = tk.Label(master, text="Chave de 16 bytes (separados por vírgula):")
        self.key_label.pack(pady=5)

        self.key_entry = tk.Entry(master, width=50)
        self.key_entry.pack()

        self.encrypt_button = tk.Button(master, text="Criptografar e Salvar", command=lambda: self.process_file("encrypt"))
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(master, text="Descriptografar e Salvar", command=lambda: self.process_file("decrypt"))
        self.decrypt_button.pack(pady=2)

        self.file_path = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Selecione o arquivo",
            filetypes=[('Todos os Arquivos', '*.*')]
        )
        self.filename_label.config(text=os.path.basename(self.file_path))

    def process_file(self, mode):
        # self.encrypt_data(b'DESENVOLVIMENTO!', '65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80')
        if not self.file_path:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado!")
            return

        output_filename = self.output_name.get()
        if not output_filename:
            messagebox.showerror("Erro", "Digite um nome para o arquivo de saída!")
            return

        key_text = self.key_entry.get()
        if not key_text:
            messagebox.showerror("Erro", "Digite a chave!")
            return

        output_path = filedialog.asksaveasfilename(
            title="Salvar arquivo",
            defaultextension=".enc" if mode == "encrypt" else ".dec",
            filetypes=[('Todos os Arquivos', '*.*')],
            initialfile=output_filename
        )

        if not output_path:
            return

        try:
            with open(self.file_path, 'rb') as f_in:
                content = f_in.read()

            if mode == "encrypt":
                processed_content = self.encrypt_data(content, key_text)
            else:
                processed_content = self.decrypt_data(content, key_text)

            with open(output_path, 'wb') as f_out:
                f_out.write(processed_content)

            messagebox.showinfo("Sucesso", f"Arquivo {mode}ado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def encrypt_data(self, data, key):
        aes = AES(key)  # Instancia a classe AES com a chave fornecida
        return aes.encrypt(data)

    def decrypt_data(self, data, key):
        aes = AES(key)  # Instancia a classe AES com a chave fornecida
        return aes.decrypt(data)


if __name__ == "__main__":
    root = tk.Tk()
    app = AESApp(root)
    root.geometry("400x300")
    root.mainloop()
