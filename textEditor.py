import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def changeColor():
    color = colorchooser.askcolor(title="Pick a color or else ;)")
    textArea.config(fg=color[1])


def changeFont(*args):
    textArea.config(font=(fontName.get(), sizeBox.get()))


def newFile():
    window.title("Untitled")
    textArea.delete(1.0, END)


def openFile():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        textArea.delete(1.0, END)

        file = open(file, "r")
        textArea.insert(1.0, file.read())
    except Exception:
        print("Couldn't read file")
    finally:
        file.close()


def saveFile():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All  Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(textArea.get(1.0, END))

        except Exception:
            print("Couldn't save the file")

        finally:
            file.close()


def cut():
    textArea.event_generate("<<Cut>>")


def paste():
    textArea.event_generate("<<Paste>>")


def copy():
    textArea.event_generate("<<Copy>>")


def about():
    showinfo("About this program", "This is a program written by Adrian Garza, and stolen off the internet")


def quit():
    window.destroy()


window = Tk()
window.title("Text editor program")
file = None
windowWidth = 500
windowHeight = 500
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth / 2) - (windowWidth / 2))
y = int((screenHeight / 2) - (windowHeight / 2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

fontName = StringVar(window)
fontName.set("Arial")

fontSize = StringVar(window)
fontSize.set("25")

textArea = Text(window, font=(fontName.get(), fontSize.get()))

scrollBar = Scrollbar(textArea)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
textArea.grid(sticky=N + E + S + W)
scrollBar.pack(side=RIGHT, fill=Y)
textArea.config(yscrollcommand=scrollBar.set)

frame = Frame(window)
frame.grid()


def fontBox():
    fB = OptionMenu(fontName, *font.families(), command=changeFont)
    fontBox.grid(row=0, column=1)

#colorButton = Button(frame, text="color", command=changeColor)
#colorButton.grid(row=0, column=0)

fontBox = OptionMenu(frame, fontName, *font.families(), command=changeFont)
fontBox.grid(row=0, column=1)

sizeBox = Spinbox(frame, from_=1, to=100, textvariable=fontSize, command=changeFont)
sizeBox.grid(row=0, column=2)

menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

textMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Text", menu=textMenu)
textMenu.add_command(label="color", command=changeColor)
textMenu.add_command(label="font", command= fontBox)
# textMenu.add_command(label="font",  *font.families(), command=changeFont)

window.mainloop()
