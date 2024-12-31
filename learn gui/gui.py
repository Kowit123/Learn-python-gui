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

#ขนาดหน้าจอ
root.geometry("500x400+700+250")

root.mainloop()