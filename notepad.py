import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os

r = tk.Tk()
r.title("Untitled - Notepad")

photo = PhotoImage(file = "notepad1.png")
r.iconphoto(False, photo)

file = None

def Widgets():
	global textArea
	textArea = Text(r)
	textArea.grid(sticky = N+E+S+W)
	menuBar = Menu(r)
	r.config(menu=menuBar)
	fileMenu = Menu(menuBar, tearoff=0)
	fileMenu.add_command(label="New", command=newfile)
	fileMenu.add_command(label="Open", command=openfile)
	fileMenu.add_command(label="Save", command=save)
	fileMenu.add_separator()
	fileMenu.add_command(label="Exit", command=close)
	menuBar.add_cascade(label="File", menu=fileMenu)

	editMenu = Menu(menuBar, tearoff=0)
	editMenu.add_command(label="Cut", command=cut)
	editMenu.add_command(label="Copy", command=copy)
	editMenu.add_command(label="Paste", command=paste)
	menuBar.add_cascade(label="Edit",menu=editMenu)

	helpMenu = Menu(menuBar,tearoff=0)
	helpMenu.add_command(label="About Notepad", command=help_m)
	menuBar.add_cascade(label="Help", menu=helpMenu)


def newfile():
	global textArea
	file = None
	r.title("Untitled - Notepad")
	textArea.delete(1.0, END)

def openfile():
	global textArea
	file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Document","*.txt")])
	file = file.name

	if file == "":
		file = None
	else:
		r.title(os.path.basename(file) + " - Notepad")
		textArea.delete(1.0, END)
		file = open(file, "rb")
		textArea.insert(1.0, file.read())
		file.close()
def save():
	global textArea, file
	if file == None:
		file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Document","*.txt")])

		if file == None:
			file = None
		else:
			file = open(file, "w")
			file.write(textArea.get(1.0, END))
			file.close()
			file = file.name
			r.title(os.path.basename(file) + " - Notepad")
	else:
		file = open(file, "w")
		file.write(textArea.get(1.0, END))
		file.close()

def close():
    title='close tab'
    text='Do you want to close this tab ?'
    replay = messagebox.askquestion(title,text)
    if replay == 'yes' :
        a=r.destroy()
        return a
    else:
        return None


def cut():
	global textArea
	textArea.event_generate("<<Cut>>")

def copy():
	global textArea
	textArea.event_generate("<<Copy>>")

def paste():
	global textArea
	textArea.event_generate("<<Paste>>")


def help_m():
	messagebox.showinfo("Notepad","This is a Notepad developed by Shabari.\nUsing Python Tkinter.")

Widgets()




r.mainloop()