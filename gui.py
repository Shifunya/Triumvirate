import tkinter as tk
from tkinter import filedialog
import cv2

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def giveFile():
    filename = filedialog.askopenfilename(initialdir=".",title="Choose a picture",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    
    inputImg = cv2.imread(filename)
    height, width = inputImg.shape[:2]
    w, h = (16, 16)
    temp = cv2.resize(inputImg, (w, h), interpolation=cv2.INTER_LINEAR)
    outputImg = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('Output', outputImg)

    fileToSave = filedialog.asksaveasfilename(initialdir=".",title="Save as",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    cv2.imwrite(fileToSave, outputImg)

    cv2.waitKey(0)
    
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