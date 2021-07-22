from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import cv2

a = 70
x = ""
q = 1
master = Tk()
master.title('Image Thresholder')
master.geometry('300x400')

def change(val):
    global a
    a = int(val)
def type_change(var):
    global q
    q = int(var)

def display():
    img = cv2.imread(x)
    if img is None:
        print('No image selected')
    else:
        if img.shape[1]>=600 or img.shape[0]>=600:
            scale_percent = 40
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        if q == 1:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)
            cv2.imshow("Image 1", thresh)
        if q == 2:
            _, thresh = cv2.threshold(img, a, 255, cv2.THRESH_BINARY)
            cv2.imshow("Image 2", thresh)
        if q == 3:
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            _, thresh = cv2.threshold(rgb, a, 255, cv2.THRESH_BINARY)
            cv2.imshow("Image 3", thresh)
        if q == 4:
            gray_inv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_inv, a, 255, cv2.THRESH_BINARY_INV)
            cv2.imshow("Image 4", thresh)
        if q == 5:
            inv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            _, thresh = cv2.threshold(inv, a, 255, cv2.THRESH_BINARY_INV)
            cv2.imshow("Image 5", thresh)
        if q == 6:
            _, thresh = cv2.threshold(img, a, 255, cv2.THRESH_BINARY_INV)
            cv2.imshow("Image 6", thresh)
        if q == 7:
            gray_trunc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_trunc, a, 255, cv2.THRESH_TOZERO)
            cv2.imshow("Image 7", thresh)
        if q == 8:
            trunc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            _, thresh = cv2.threshold(trunc, a, 255, cv2.THRESH_TOZERO)
            cv2.imshow("Image 8", thresh)
        if q == 9:
            _, thresh = cv2.threshold(img, a, 255, cv2.THRESH_TOZERO)
            cv2.imshow("Image 9", thresh)
    
def execute():
    global img
    global x
    master.filename = filedialog.askopenfilename(title="Image opener", filetypes=(("jpeg","*.jpg"), ("png","*.png")))
    label = Label(master, text=master.filename)
    label.pack()
    flag = label.winfo_exists()
    x = label['text']
    img = cv2.imread(x)
    if img.shape[1]>=600 or img.shape[0]>=600:
        scale_percent = 40
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Original Image", img)
    if flag == 1:
        label.after(1000, label.destroy())

btn = Button(master, text="Open your file", command=execute).pack(pady=30)
btn2 = Button(master, text="Display Result image", command=display).pack(pady=10)
scale = Scale(master, orient='horizontal', from_=0, to=255, label="Threshold scale:", command=change)
scale.pack(pady=30)
scale2 = Scale(master, orient='horizontal', from_=1, to=9, label="Image type:", command=type_change)
scale2.pack(pady=30)
master.mainloop()
