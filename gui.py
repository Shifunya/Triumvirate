import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def pixelization():
    print("pixelization func works")

def triangulation():
    print("triangulation func works")

def segmentation():
    print("segmentation func works")

def allEffects():
    print("allEffects func works")

pixelButton = tk.Button(frame, text="Пикселизация", command=pixelization)
pixelButton.pack(side=tk.LEFT)

triangButton = tk.Button(frame, text="Триангуляция", command=triangulation)
triangButton.pack(side=tk.LEFT)

segmButton = tk.Button(frame, text="Цветовая сегментация", command=segmentation)
segmButton.pack(side=tk.LEFT)

allButton = tk.Button(frame, text="Все эффекты", command=allEffects)
allButton.pack(side=tk.LEFT)

root.mainloop()