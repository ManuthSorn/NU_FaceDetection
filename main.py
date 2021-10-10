from tkinter import * 
import os

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def Data_window():
    #new_root = Tk()
    #new_root.title("New Tkinter Window")
    os.startfile("src\Read_Write.exe")
    #new_root.geometry("500x500")


def Scan_window():
    #new_root = Tk()
    #new_root.title("New Tkinter Window")
    os.startfile("Diagram_0.txt")
    #new_root.geometry("500x500")

Data_button = Button(root, text="Form Data Window", command=Data_window) 
sc_button = Button(root, text="Form Scan Window", command=Scan_window)
Data_button.pack() 
sc_button.pack()

root.mainloop()