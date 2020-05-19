import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def giveFile():
    filename=filedialog.askopenfilename(initialdir=".",title="Choose a picture",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    return filename

def pixelization():
    print("pixel button pressed")
    fileChosen = giveFile()
    print(fileChosen)

def triangulation():
    print("triangulation func works")
    fileChosen = giveFile()
    print(fileChosen)

def segmentation():
    print("segmentation func works")
    fileChosen = giveFile()
    print(fileChosen)

def allEffects():
    print("allEffects func works")
    fileChosen = giveFile()
    print(fileChosen)

pixelButton = tk.Button(frame, text="Пикселизация", command=pixelization)
pixelButton.pack(side=tk.LEFT)

triangButton = tk.Button(frame, text="Триангуляция", command=triangulation)
triangButton.pack(side=tk.LEFT)

segmButton = tk.Button(frame, text="Цветовая сегментация", command=segmentation)
segmButton.pack(side=tk.LEFT)

allButton = tk.Button(frame, text="Все эффекты", command=allEffects)
allButton.pack(side=tk.LEFT)

root.mainloop()