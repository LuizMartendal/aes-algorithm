import tkinter as tk

from aes_app import AESApp

if __name__ == "__main__":
    root = tk.Tk()
    app = AESApp(root)
    root.geometry("400x300")
    root.mainloop()