import tkinter as tk

f = tk.Tk()

f.title('snake')

f.iconphoto(True, tk.PhotoImage(file='script_python/snake/snake.png'))
wl= f.winfo_reqwidth()
wh = f.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)


f.geometry("500x500+450+100")
f.resizable(0,0)


if  __name__ == '__main__' :
    f.mainloop()
