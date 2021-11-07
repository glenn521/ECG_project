from subprocess import Popen
import tkinter as tk
from PIL import Image,ImageTk
import PyPDF2
root= tk.Tk()
from tkinter.filedialog import askopenfile

canvas = tk.Canvas(root,width=600,height=100)
canvas.grid  (columnspan=3)

#logo
'''logo=Image.open('forza.png')     #input image in logo variable
logo=ImageTk.PhotoImage(logo)   #Convert image in logo to tkinter format
logo_label=tk.Label(image=logo) #making a lable out of the image
logo_label.image = logo
logo_label.grid(column=1,row=0)
'''
instructions = tk.Label(root, text = "Select the required ECG signal to be displayed", font="Raleway")
instructions.grid(columnspan=3, column=0, row=0)

ht=2
wd=15
ft="Raleway"
bgcolor="#0059b3"
fgcolor="white"
option1 = tk.StringVar()
option1_btn = tk.Button(root, textvariable=option1,command=lambda:Popen('python Normal_Sinus.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option1.set("Normal Sinus")
option1_btn.grid(column=0,row=1)

option2 = tk.StringVar()
option2_btn = tk.Button(root, textvariable=option2,command=lambda:Popen('python Sinus_Bradycardia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option2.set("Sinus Bradycardia")
option2_btn.grid(column=0,row=2)


option3 = tk.StringVar()
option3_btn = tk.Button(root, textvariable=option3,command=lambda:Popen('python Sinus_Tachycardia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option3.set("Sinus Tachycardia")
option3_btn.grid(column=0,row=3)

option4 = tk.StringVar()
option4_btn = tk.Button(root, textvariable=option4,command=lambda:Popen('python Sinus_Pause_or_Arrest.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option4.set("Sinus Pause")
option4_btn.grid(column=0,row=4)

option5 = tk.StringVar()
option5_btn = tk.Button(root, textvariable=option5,command=lambda:Popen('python Supraventricular_Tachycardia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option5.set("Supraventricular \nTachycardia")
option5_btn.grid(column=0,row=5)

option6 = tk.StringVar()
option6_btn = tk.Button(root, textvariable=option6,command=lambda:Popen('python Idioventricular_Rhythm.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option6.set("Idioventricular \nRhythm")
option6_btn.grid(column=0,row=6)

option7 = tk.StringVar()
option7_btn = tk.Button(root, textvariable=option7,command=lambda:Popen('python Accelerated_Idioventricular_rhythm.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option7.set("Accelerated \nIdioventricular \nRhythm")
option7_btn.grid(column=1,row=1)

option8 = tk.StringVar()
option8_btn = tk.Button(root, textvariable=option8,command=lambda:Popen('python Agonal_Rhythm.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option8.set("Agonal Rhythm")
option8_btn.grid(column=1,row=2)

option9 = tk.StringVar()
option9_btn = tk.Button(root, textvariable=option9,command=lambda:Popen('python Premature_Atrial_Contractions.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option9.set("Premature \natrial \ncontractions")
option9_btn.grid(column=1,row=3)

option10 = tk.StringVar()
option10_btn = tk.Button(root, textvariable=option10,command=lambda:Popen('python Premature_Junctional_Complexes.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option10.set("Premature \nJunctional \nComplexes")
option10_btn.grid(column=1,row=4)

option11 = tk.StringVar()
option11_btn = tk.Button(root, textvariable=option11,command=lambda:Popen('python Atrial_Flutter.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option11.set("Atrial Flutter")
option11_btn.grid(column=1,row=5)

option12 = tk.StringVar()
option12_btn = tk.Button(root, textvariable=option12,command=lambda:Popen('python Ventricular_Tachycardia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option12.set("Ventricular \nTachycardia")
option12_btn.grid(column=1,row=6)

option13 = tk.StringVar()
option13_btn = tk.Button(root, textvariable=option13,command=lambda:Popen('python Atrial_Fibrilation.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option13.set("Atrial Fibrilation")
option13_btn.grid(column=2,row=1)

option14 = tk.StringVar()
option14_btn = tk.Button(root, textvariable=option14,command=lambda:Popen('python Ventricular_Fibrilation.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option14.set("Ventricular \nFibrilation")
option14_btn.grid(column=2,row=2)

option15 = tk.StringVar()
option15_btn = tk.Button(root, textvariable=option15,command=lambda:Popen('python Accelerated_Junctional_Rhythm.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option15.set("Accelerated \nJunctional \nRhythm")
option15_btn.grid(column=2,row=3)

option16 = tk.StringVar()
option16_btn = tk.Button(root, textvariable=option16,command=lambda:Popen('python Junctional_Tachycardia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option16.set("Junctional \nTachycardia")
option16_btn.grid(column=2,row=4)

option17 = tk.StringVar()
option17_btn = tk.Button(root, textvariable=option17,command=lambda:Popen('python Premature_Ventricular_Complexes.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option17.set("Premature \nVentricular \ncomplexes")
option17_btn.grid(column=2,row=5)

option18 = tk.StringVar()
option18_btn = tk.Button(root, textvariable=option18,command=lambda:Popen('python Sinus_Arrhythmia.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option18.set("Sinus arrhythmia")
option18_btn.grid(column=2,row=6)

option19 = tk.StringVar()
option19_btn = tk.Button(root, textvariable=option19,command=lambda:Popen('python Junctional_Escape_Rhythm.py'), font=ft, bg=bgcolor, fg=fgcolor, height=ht, width=wd)
option19.set("Junctional \nescape rhythm")
option19_btn.grid(column=0,row=7)



#canvas = tk.Canvas(root, width=600, height=250)
#canvas.grid(columnspan=3, column =0, row=1)

root.mainloop()
