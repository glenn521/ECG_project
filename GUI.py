from subprocess import Popen
import tkinter as tk
from PIL import Image,ImageTk
root= tk.Tk()
from tkinter.filedialog import askopenfile

canvas = tk.Canvas(root,width=600,height=100,background='#ccd7eb',bd=0, highlightthickness=0, relief='ridge')
canvas.grid  (columnspan=3)

#logo
'''logo=Image.open('forza.png')     #input image in logo variable
logo=ImageTk.PhotoImage(logo)   #Convert image in logo to tkinter format
logo_label=tk.Label(image=logo) #making a lable out of the image
logo_label.image = logo
logo_label.grid(column=1,row=0)
'''
instructions = tk.Label(root, text = "Select the required ECG signal to be displayed", font="Arial", fg='#000', background='#ccd7eb')
instructions.grid(columnspan=3, column=0, row=0)
root.configure(background='#ccd7eb')

ht=4
wd=43
ft="Arial"
bgcolor="#0059b3"
fgcolor="white"
option1 = tk.StringVar()
option1_btn = tk.Button(root, textvariable=option1,command=lambda:Popen('python Normal_Sinus.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option1.set("Normal Sinus")
option1_btn.grid(column=0,row=1)

option2 = tk.StringVar()
option2_btn = tk.Button(root, textvariable=option2,command=lambda:Popen('python Sinus_Bradycardia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option2.set("Sinus Bradycardia")
option2_btn.grid(column=0,row=2)


option3 = tk.StringVar()
option3_btn = tk.Button(root, textvariable=option3,command=lambda:Popen('python Sinus_Tachycardia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option3.set("Sinus Tachycardia")
option3_btn.grid(column=0,row=3)

option4 = tk.StringVar()
option4_btn = tk.Button(root, textvariable=option4,command=lambda:Popen('python Sinus_Pause_or_Arrest.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option4.set("Sinus Pause")
option4_btn.grid(column=0,row=4)

option5 = tk.StringVar()
option5_btn = tk.Button(root, textvariable=option5,command=lambda:Popen('python Supraventricular_Tachycardia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option5.set("Supraventricular \nTachycardia")
option5_btn.grid(column=0,row=5)

option6 = tk.StringVar()
option6_btn = tk.Button(root, textvariable=option6,command=lambda:Popen('python Idioventricular_Rhythm.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd, borderwidth=3)
option6.set("Idioventricular \nRhythm")
option6_btn.grid(column=0,row=6)

option7 = tk.StringVar()
option7_btn = tk.Button(root, textvariable=option7,command=lambda:Popen('python Accelerated_Idioventricular_rhythm.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option7.set("Accelerated \nIdioventricular \nRhythm")
option7_btn.grid(column=1,row=1)

option8 = tk.StringVar()
option8_btn = tk.Button(root, textvariable=option8,command=lambda:Popen('python Agonal_Rhythm.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd, borderwidth=3)
option8.set("Agonal Rhythm")
option8_btn.grid(column=1,row=2)

option9 = tk.StringVar()
option9_btn = tk.Button(root, textvariable=option9,command=lambda:Popen('python Premature_Atrial_Contractions.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option9.set("Premature \natrial \ncontractions")
option9_btn.grid(column=1,row=3)

option10 = tk.StringVar()
option10_btn = tk.Button(root, textvariable=option10,command=lambda:Popen('python Premature_Junctional_Complexes.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option10.set("Premature \nJunctional \nComplexes")
option10_btn.grid(column=1,row=4)

option11 = tk.StringVar()
option11_btn = tk.Button(root, textvariable=option11,command=lambda:Popen('python Atrial_Flutter.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option11.set("Atrial Flutter")
option11_btn.grid(column=1,row=5)

option12 = tk.StringVar()
option12_btn = tk.Button(root, textvariable=option12,command=lambda:Popen('python Ventricular_Tachycardia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option12.set("Ventricular \nTachycardia")
option12_btn.grid(column=1,row=6)

option13 = tk.StringVar()
option13_btn = tk.Button(root, textvariable=option13,command=lambda:Popen('python Atrial_Fibrilation.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option13.set("Atrial Fibrilation")
option13_btn.grid(column=2,row=1)

option14 = tk.StringVar()
option14_btn = tk.Button(root, textvariable=option14,command=lambda:Popen('python Ventricular_Fibrilation.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option14.set("Ventricular \nFibrilation")
option14_btn.grid(column=2,row=2)

option15 = tk.StringVar()
option15_btn = tk.Button(root, textvariable=option15,command=lambda:Popen('python Accelerated_Junctional_Rhythm.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option15.set("Accelerated \nJunctional \nRhythm")
option15_btn.grid(column=2,row=3)

option16 = tk.StringVar()
option16_btn = tk.Button(root, textvariable=option16,command=lambda:Popen('python Junctional_Tachycardia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option16.set("Junctional \nTachycardia")
option16_btn.grid(column=2,row=4)

option17 = tk.StringVar()
option17_btn = tk.Button(root, textvariable=option17,command=lambda:Popen('python Premature_Ventricular_Complexes.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option17.set("Premature \nVentricular \ncomplexes")
option17_btn.grid(column=2,row=5)

option18 = tk.StringVar()
option18_btn = tk.Button(root, textvariable=option18,command=lambda:Popen('python Sinus_Arrhythmia.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option18.set("Sinus arrhythmia")
option18_btn.grid(column=2,row=6)

option19 = tk.StringVar()
option19_btn = tk.Button(root, textvariable=option19,command=lambda:Popen('python Junctional_Escape_Rhythm.py',shell=True), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd,borderwidth=3)
option19.set("Junctional \nescape rhythm")
option19_btn.grid(column=1,row=7)

option20 = tk.StringVar()
option20_btn = tk.Button(root, text="Exit", command=root.destroy, font=ft, bg='red', fg=fgcolor, height=ht, width=wd,borderwidth=3)
option20_btn.grid(column=2,row=7)

root.mainloop()
