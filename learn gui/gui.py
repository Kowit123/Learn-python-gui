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

#button
btn1 = Button(root,text="Open",bg="brown",font=30).pack()

#ขนาดหน้าจอ
root.geometry("500x400+700+250")

root.mainloop()