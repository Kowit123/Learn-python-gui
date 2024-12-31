from tkinter import *

root = Tk()
root.title("GUI")

#label
myLabel = Label(text="Hello").pack()
#fg = color font
myLabel = Label(text="Hello",fg="red").pack()
#font = font size
myLabel = Label(text="Hello",font=20).pack()
#bg = background color
myLabel = Label(text="Hello",bg="yellow").pack()
#จัดตำแหน่ง Label โดยใช้ place
myLabel = Label(text="Hello",bg="yellow").place(x=0,y=0)

#จัดตำแหน่ง Label โดยใช้ grid ps. grid ใช้ร่วมกับวิธีอื่นไม่ได้
# myLabel = Label(text="Hello",font=20).grid(row=0,column=0)

def showmsg():
    Label(text="KK!\n").pack()
#button
btn1 = Button(root,text="Open",fg="white",bg="black",font=30,command=showmsg).pack()


def showmsg():
    print("KK!\n")

#ขนาดหน้าจอ&ตำแหน่ง
root.geometry("500x400+700+250")

root.mainloop()