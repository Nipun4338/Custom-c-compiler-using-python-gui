import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from tkinter.font import Font
from tkinter.messagebox import *
import time
from subprocess import Popen, PIPE
import tkinter.scrolledtext as scrolledtext


image1=''
main = Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
os.chdir(dir_path)
main.bold_font = Font(family="Helvetica", size=14, weight="bold")
main.title("Compiler")
main.minsize(1300, 670)
main.maxsize(1300, 670)
main.labelFrame = Label(main, text = "Welcome to Notebook", font=('Impact', -20), bg='#000', fg='#000')
main.labelFrame.place(relx = 0.5,
                   rely = 0.2,
                   anchor = 'center')
main.configure(background='#dfdddd')
main.labelFrame.configure(background='#dfdddd')

def executeme():
    yourfile=filedialog.askopenfilenames(title = "Select your file")
    for i in yourfile:
        commands = f'''cd {dir_path}
        set Path=C:\\MinGW\\bin;%PATH%
        gcc -o 180104042.exe 180104042.c
        "{dir_path}\\180104042.exe" 2 "{i}"
        ''' #you can use " " for 1 line of commands or '''  ''' for several lines
        #Single quotation marks won't do in that case. You have to add quotation marks around each path and also enclose the whole command in quotation marks:
    process = Popen("cmd.exe", shell=False, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    out, err = process.communicate(commands)
    f = open(f"filtered.txt", "r")
    Label(main, text = str(f.read()), font=('Impact', -15),borderwidth=1, relief="raised", fg='#000').grid(column= 0, row = 1)
    f.close()


#get text for inserting note
def get_text(*values):
    if len(values[0])>0 and len(values[1])>0:
        #print(str(values[1])+"' '"+str(values[0]))
        f = open(f"{values[1]}", "w")
        f.write(f"{values[0]}")
        f.close()
        commands = f'''cd {dir_path}
        set Path=C:\\MinGW\\bin;%PATH%
        gcc -o 180104042.exe 180104042.c
        "{dir_path}\\180104042.exe" 2 "{values[1]}"
        ''' #you can use " " for 1 line of commands or '''  ''' for several lines
            #Single quotation marks won't do in that case. You have to add quotation marks around each path and also enclose the whole command in quotation marks:
        process = Popen("cmd.exe", shell=False, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        out, err = process.communicate(commands)
        f = open(f"filtered.txt", "r")
        alert=Tk()
        alert.title('Output')
        alert.minsize(1300, 700)
        alert.maxsize(1300, 700)
        alert.configure(background='#456')
        Label(alert, text = str(f.read()),font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')
        f.close()

    else:
        alert=Tk()
        alert.title('Alert')
        alert.minsize(400, 50)
        alert.maxsize(400, 50)
        alert.configure(background='#fff')
        Label(alert, text = "Nothing to add due to empty!",bg="#fff",font=('Impact', -20),fg="#df4759").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')


def compileme():
    add=Tk()
    add.title('Add a new note')
    sub = Entry(add,font = ('courier', 15, 'bold'), width=50,foreground = 'green',borderwidth=15, relief=tk.SUNKEN)
    sub.insert(0, "")
    sub.pack(side=TOP, anchor=NW,expand=True, fill='both')

    txt = scrolledtext.ScrolledText(add, undo=True)
    txt['font'] = ('consolas', '12')
    txt.pack(expand=True, fill='both')
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=5, relief="sunken")
    add.showoriginal = tk.Button(add,width=15, text="Insert",font=('Impact', -20),fg='#fff', command= lambda:[get_text(txt.get('1.0', 'end-1c'),str(sub.get()))])
    add.showoriginal.configure(background='#5cb85c')
    add.showoriginal.pack()
    add.showoriginal1 = tk.Button(add,width=15, text="Add Images",font=('Impact', -20),fg='#fff', command= lambda:[add_images(values[0])])
    add.showoriginal1.configure(background='#0275d8')
    add.showoriginal1.pack()



def execute():
        main.showoriginal = Button(main, text = "Select",command = executeme)
        main.showoriginal.configure(background='#df4759',font=('Impact', -20),fg='#fff')
        main.showoriginal.place(relx = 0.37,
                           rely = 0.5,
                           anchor = 'center')

def compile():
        main.showoriginal = Button(main, text = "Compile",command = compileme)
        main.showoriginal.configure(background='#42ba96',font=('Impact', -20),fg='#fff')
        main.showoriginal.place(relx = 0.63,
                           rely = 0.5,
                           anchor = 'center')

execute()
compile()
main.mainloop()
