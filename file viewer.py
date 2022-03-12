from tkinter import *
import tkinter.ttk as ttk
import os

root = Tk()
root.config(bg='white')
root.geometry('500x300')

style = ttk.Style()

def fixed_map(option):
    # Returns the style map for 'option' with any styles starting with
    # ("!disabled", "!selected", ...) filtered out

    # style.map() returns an empty list for missing options, so this should
    # be future-safe
    return [elm for elm in style.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]

style.map("Treeview",
          foreground=fixed_map("foreground"),
          background=fixed_map("background"))

path = 'C:\\'

def selectItem(a):
    global path
    curItem = file_window.focus()
    to_extend = file_window.item(curItem)['values'][0]
    if os.path.isdir(path+'\\'+to_extend):
        try:
            current = os.listdir(path+'\\'+to_extend)
            path = path+'\\'+to_extend
            file_window.delete(*file_window.get_children())
            for x in current:
                a = file_window.insert('', END, values=(x, 0))
        except:
            pass

def dirback():
    global path
    path = path.split('\\')
    if len(path) > 2:
        path.pop()
        path.pop()
    path = '\\'.join(path)+'\\'
    current = os.listdir(path)
    file_window.delete(*file_window.get_children())
    for x in current:
        a = file_window.insert('', END, values=(x, 0))

style.configure("Treeview", highlightthickness=0, highlightcolor='red', bd=0, font=('Bahnschrift', 11)) # Modify the font of the body
style.configure("Treeview.Heading", font=('Bahnschrift', 20,'bold')) # Modify the font of the headings
style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


column_names = ("title")
file_window = ttk.Treeview(root, column=column_names, style="Treeview")
file_window.pack()
current = [f for f in os.listdir(path) if not f.startswith('.')]

file_window['show'] = 'headings'
file_window.heading("title", text="FILE LIST")
file_window.column("title", width=500, minwidth=500, stretch=NO)
file_window.tag_configure('odd', background='#E8E8E8')
for x in current:
    a = file_window.insert('', END, values=(x, 0), tags=('odd',))

file_window.bind('<Double-Button-1>', selectItem)

frame = Frame(bg='black', padx=2, pady=2)
backbutton = Button(frame, text='back', command=dirback, borderwidth=0, padx=49, pady=5, font=('Bahnschrift', 15), bg='white')
frame.pack(anchor='center')
backbutton.pack(anchor='center')


root.mainloop()
