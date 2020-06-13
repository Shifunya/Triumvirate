import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2 
import matplotlib
import pkg_resources.py2_warn


root = tk.Tk()
root.title('Triumvirate')
frame = tk.Frame(root)
frame.pack()

def giveFile():
    filename = filedialog.askopenfilename(initialdir=".",title="Choose a picture",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    return filename

def saveFile(outputImg):
    fileToSave = filedialog.asksaveasfilename(initialdir=".",title="Save as",defaultextension="*.*",filetypes=(("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")))
    cv2.imwrite(fileToSave, outputImg)

def rect_contains(rect, point):
    if point[0] < rect[0]:
        return False
    elif point[1] < rect[1]:
        return False
    elif point[0] > rect[2]:
        return False
    elif point[1] > rect[3]:
        return False
    return True

def draw_delaunay(img, subdiv, delaunay_color):
    triangleList = subdiv.getTriangleList();
    height, width = img.shape[:2]
    r = (0, 0, width, height)

    for t in triangleList:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        
        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3):
            cv2.line(img, pt1, pt2, delaunay_color, 1)
            cv2.line(img, pt2, pt3, delaunay_color, 1)
            cv2.line(img, pt3, pt1, delaunay_color, 1)

def draw_all(inputImg, outputImg, subdiv):
    triangleList = subdiv.getTriangleList();
    height, width = inputImg.shape[:2]
    r = (0, 0, width, height)

    for t in triangleList:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        poly = np.array( [pt1,pt2,pt3] )

        M = cv2.moments(poly)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        resultRed = int(inputImg[cY, cX][0])
        resultGreen = int(inputImg[cY, cX][1])
        resultBlue = int(inputImg[cY, cX][2])
        
        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3):
            cv2.fillPoly(outputImg, np.int32([poly]), (resultRed, resultGreen, resultBlue))

def pixelization():
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
    fileChosen = giveFile()

    inputImg = cv2.imread(fileChosen)
    height, width = inputImg.shape[:2]

    outputImg = cv2.imread(fileChosen)

    edges = cv2.Canny(inputImg, 100, 200)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    points = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        for point in approx:
            points.append((point[0][0],point[0][1]))

    rect = (0, 0, width, height)
    print(rect)

    subdiv = cv2.Subdiv2D(rect);

    for p in points:
        subdiv.insert(p)

    draw_delaunay(outputImg, subdiv, (0, 255, 0))

    cv2.imshow('Output', outputImg)

    saveFile(outputImg)

    cv2.waitKey(0)

def segmentation():
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
    fileChosen = giveFile()
    inputImg = cv2.imread(fileChosen)
    height, width = inputImg.shape[:2]

    outputImg = np.zeros((height,width,3), dtype=np.uint8)
    outputImg.fill(255)

    edges = cv2.Canny(inputImg, 100, 200)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    points = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        for point in approx:
            points.append((point[0][0],point[0][1]))

    rect = (0, 0, width, height)

    subdiv = cv2.Subdiv2D(rect);

    print(f"Height: {height}")
    print(f"Width: {width}")

    for p in points:
        subdiv.insert(p)

    draw_all(inputImg, outputImg, subdiv)

    cv2.imshow('output', outputImg)

    saveFile(outputImg)    

    cv2.waitKey(0)

pixelButton = tk.Button(frame, text="Pixelization", command=pixelization)
pixelButton.pack(side=tk.LEFT)

triangButton = tk.Button(frame, text="Triangulation", command=triangulation)
triangButton.pack(side=tk.LEFT)

segmButton = tk.Button(frame, text="Color segmentation", command=segmentation)
segmButton.pack(side=tk.LEFT)

allButton = tk.Button(frame, text="All effects", command=allEffects)
allButton.pack(side=tk.LEFT)

root.mainloop()