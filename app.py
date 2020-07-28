from tkinter import *
from tkinter import ttk as tk
from PIL import Image, ImageTk

root = Tk()
root.title("Image Chooser")

mainframe = tk.Frame(root, padding = 3)
mainframe.grid(column = 0, row = 0, sticky='nsew')

root.columnconfigure(0, weight=1, minsize = 600)
root.rowconfigure(0, weight=1, minsize=700)
mainframe.columnconfigure(0, weight=1, minsize = 600)
mainframe.rowconfigure(0, weight=1, minsize=500)

original_image = Image.open('test.jpg')

h = original_image.height
w = original_image.width

if h > w:
    r = 500/h
else:
    r = 600/w

resized = original_image.resize((round(w*r), round(h*r)), Image.ANTIALIAS)

image = ImageTk.PhotoImage(resized)

imframe = tk.Frame(mainframe, padding = 3)
imframe.grid(column = 0, row = 0, sticky='new')

imlabel = tk.Label(imframe, image=image, anchor='n')

imlabel.pack(side = "top", fill = "both", expand = "ye")

consframe = tk.Frame(mainframe, padding=2)
consframe.grid(column = 0, row = 1, sticky= 'nsew')

output = StringVar()
console = tk.Label(consframe, anchor='center', textvariable=output)
console.pack(fill='both', expand = 'yes')

output.set('test')

bframes = tk.Frame(mainframe, padding=3)
bframes.grid(column = 0, row = 2, sticky='ns')

for i in ['a', 'b', 'c']:
    button = tk.Button(bframes, text=i, command=lambda x: None)
    button.pack(side = 'left')

root.mainloop()