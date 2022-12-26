from tkhtmlview import HTMLLabel
from tkinter import *
import root.downloader as Dm
import root.time as Bt
import root.calculator as Bc
import root.help as Bh
from root.DIOS_Colored import cl
banner = """
  _________________________________________________________________________________
 |    ____  _                 _         ___  ____    |01100101011000110001001110101|
 |   |  _ \(_)___ _   _ _ __ (_) ___   / _ \/ ___|   |10101111000101010111010001010|
 |   | | | | / __| | | | '_ \| |/ __| | | | \___ \   |       32bit And 64bit       |
 |   | |_| | \__ \ |_| | | | | | (__  | |_| |___) |  |          Supported          |
 |   |____/|_|___/\__,_|_| |_|_|\___|  \___/|____/   | https://disunic20.github.io |
 |___________________________________________________|_____________________________|
            | |                        | |_____|_______________|_____|
            | | By Disunic             | |      Version - 2.0.0      |
            |_|________________________|_|_____|_______________|_____|

    Type - help, to get help section .
"""
bannercl = cl("#0078d4")
inputcl = cl("#ffae07")
print(bannercl+banner)
def main():
    DisunicOs = input(inputcl+'DIOS : ',)

    if DisunicOs == "help":  # Help
        Bh.helpos()

    elif DisunicOs == "time":  # Time
        Bt.time()

    elif DisunicOs == "date":  # Dates
        Bt.dates()

    elif DisunicOs == "programs":  # Programes
        Bh.ProHelp()

    elif DisunicOs == "calculator":  # Calculator
        Bc.calculation()

    elif DisunicOs == "downloader": #Downloader
        print("Select mp3 or mp4")
        teos = input('Select : ')
        if teos == "mp3":
            Dm.mp3()
        elif teos == "mp4":
            Dm.mp4()
        else:
            print("Error")
            return (main())
    elif DisunicOs == "browser":  # Disunicx lite for DIOS
        import root.browser

    elif DisunicOs == "terminal":  # Disunicx
        pass

    elif DisunicOs == "about":  # About
        root = Tk()
        root.geometry("400x400")
        my_label = HTMLLabel(root, html="""
                        <h1 style="color: red; text-align: center">Disunic OS</h1>
                    """)
        my_label.pack(pady=20, padx=20)
        root.mainloop()
    elif DisunicOs == "exit":  # Exit
        print("Exiting Os 👾 ")
        exit()
    else:
        print("No command Found Type,-hh for advance help")
        Bh.helpos()
    return (main())
main()
