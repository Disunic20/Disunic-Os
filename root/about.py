from tkhtmlview import HTMLLabel
from tkinter import *

root = Tk()
root.geometry("400x400")
my_label = HTMLLabel(root, html="""
                <h1 style="color: red; text-align: center">Disunic OS</h1>
            """)
my_label.pack(pady=20, padx=20)
root.mainloop()