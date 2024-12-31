from tkinter import *

root = Tk()
root.title("GUI")

#label, fg = color font, font = font size, bg = background color
myLabel = Label(root,text="Hello",fg="red",font=20,bg="yellow").pack()
#จัดตำแหน่ง Label โดยใช้ place
# myLabel = Label(root,text="Hello",bg="yellow").place(x=0,y=0)
#จัดตำแหน่ง Label โดยใช้ grid ps. grid ใช้ร่วมกับวิธีอื่นไม่ได้
# myLabel = Label(text="Hello",font=20).grid(row=0,column=0)

def showmsg():
    msg = txt.get()
    Label(text=msg,bg="black",fg="white").pack()
    Label(text="KK!\n").pack()
#button
btn1 = Button(root,text="Open",fg="white",bg="black",font=30,command=showmsg).pack()

#textbox
txt = StringVar()
mytxt = Entry(root,textvariable=txt,bg="black",fg="white").pack()


#ขนาดหน้าจอ&ตำแหน่ง
root.geometry("500x400+700+250")

root.mainloop()
