import tkinter as tk
import cv2
from tkinter import messagebox
from facerec import *



window = tk.Tk()
window.title("Face Recognition system")
l = tk.Label(window, text = 'Facial Recognition by helmi',font=("Algerian", 25))
l.place(x = 220,y = 10) 
b2=tk.Button(window,text="LOGIN",font=("Algerian",20),bg='green',fg='white',command=detect_face)
b2.place(x=300, y=100)
b=tk.Button(window,text="SIGN  UP",font=("Algerian",20),bg='green',fg='white',command=add)
b.place(x=430, y=100)


b3=tk.Button(window,text="EXIT",font=("Algerian",20),bg='black',fg='white',command=window.destroy)
b3.place(x=700, y=200)

window.geometry("800x300")
window.mainloop()
