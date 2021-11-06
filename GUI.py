from tkinter import *
import os

root = Tk()
root.geometry("500x320")
root.title(" Sharepoint direct link generator ")
root.attributes('-topmost',True)
  
def Take_input():
    text_inp = tb_inp.get("1.0", "end-1c")
    text_inp = text_inp.replace("abc","aaa")
    tb_out.delete(END)
    tb_out.insert(END, text_inp)
    text_inp = 'echo ' + text_inp.strip() + "|clip"
    os.system(text_inp)

l_inp = Label(text = "Input: ", font = ('Helvetica', 12, 'bold')) 
tb_inp = Text(root, height = 5,
                width = 60,
                bg = "light yellow")

l_out = Label(text = "Output: ", font = ('Helvetica', 12, 'bold'))
tb_out = Text(root, height = 5, 
              width = 60, 
              bg = "light cyan")
  
b_Put = Button(root, height = 2,
                 width = 20, 
                 text ="Put to clipboard",
                 font = ('Helvetica', 12, 'bold'),
                 command = lambda:Take_input())

l_inp.place(x = 10, y = 10)
tb_inp.place(x = 10, y = 40)
l_out.place(x = 10, y = 130)
tb_out.place(x = 10, y = 160)
b_Put.place(x = 280, y = 260)
  
mainloop()