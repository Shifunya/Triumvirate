import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2 
import matplotlib

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def giveFile():
    filename = filedialog.askopenfilename(initialdir=".",title="Choose a picture",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    return filename

def saveFile(outputImg):
    fileToSave = filedialog.asksaveasfilename(initialdir=".",title="Save as",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    cv2.imwrite(fileToSave, outputImg)

def pixelization():
    print("pixel button pressed")
    fileChosen = giveFile()

    inputImg = cv2.imread(fileChosen)
    height, width = inputImg.shape[:2]
    w, h = (16, 16)
    temp = cv2.resize(inputImg, (w, h), interpolation=cv2.INTER_LINEAR)
    outputImg = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('Output', outputImg)

    saveFile(outputImg)    

    cv2.waitKey(0)

def triangulation():
    print("triangulation func works")
    fileChosen = giveFile()
    print(fileChosen)

def segmentation():
    print("segmentation func works")
    fileChosen = giveFile()

    inputImg = cv2.imread(fileChosen, cv2.IMREAD_COLOR)
    inputImg_gray = cv2.cvtColor(inputImg, cv2.COLOR_BGR2GRAY)
    
    filt = cv2.medianBlur(inputImg_gray, 9)
    filt = cv2.blur(filt, (3,3))
    
    edges = cv2.Canny(filt, 10, 50)
    cv2.imshow('output', edges)

    saveFile(edges)    

    cv2.waitKey(0)

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