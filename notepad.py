from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk
from datetime import datetime
import webbrowser

# Initialize current_file
current_file = None

# ======================================================================================
#  ========================== File Code Starts Here  ============================
# ======================================================================================

# =================================== New Code  ======================================
def new():
    global current_file
    text.delete('1.0', 'end')
    current_file = None
# ===================================== End =========================================

# ========================= New Window Code  ================================
def new_window():
    new_root = tk.Tk()
    new_root.geometry('500x500')

    menubar = Menu(new_root)

    file = Menu(menubar, tearoff=0)
    file.add_command(label="New", command=new)
    file.add_command(label="New window", command=new_window)
    file.add_command(label="Open", command=Open)
    file.add_command(label="Save", command=save)
    file.add_command(label="Save as", command=save_as)
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))

    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: new_text.edit_undo())
    edit.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: new_text.edit_redo())
    edit.add_separator()
    edit.add_command(label="Cut", command=lambda: new_text.event_generate("<<Cut>>"))
    edit.add_command(label="Copy", command=lambda: new_text.event_generate("<<Copy>>"))
    edit.add_command(label="Paste", command=lambda: new_text.event_generate("<<Paste>>"))
    edit.add_command(label="Delete", command=lambda: new_text.delete('1.0', 'end'))
    edit.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: new_text.tag_add('sel', '1.0', 'end'))
    edit.add_command(label="Time/Date", accelerator="F5", command=lambda: new_text.insert('end', datetime.now()))
    menubar.add_cascade(label="Edit", menu=edit)

    Format = Menu(menubar, tearoff=0)
    Format.add_command(label="Word Wrap")
    Format.add_command(label="Font...", command=fonts)
    menubar.add_cascade(label="Format", menu=Format)

    Help = Menu(menubar, tearoff=0)
    Help.add_command(label="View Help", command=view_help)
    Help.add_command(label="Send FeedBack", command=send_feedback)
    Help.add_command(label="About Notepad")
    menubar.add_cascade(label="Help", menu=Help)

    new_root.config(menu=menubar)

    new_text = ScrolledText(new_root, width=1000, height=1000, undo=True)
    new_text.place(x=0, y=0)

    new_root.mainloop()

# =========================== End ==============================================        

# ===================== Open File Code ========================================
def Open():
    global current_file
    current_file = filedialog.askopenfilename(
        initialdir='/',
        title="Select file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if current_file:
        with open(current_file, 'r') as file:
            text.delete('1.0', 'end')
            text.insert('end', file.read())
# ================================= End ==========================================

# ================================ Save File Code ====================================
def save():
    global current_file
    if not current_file:
        save_as()
    else:
        with open(current_file, 'w') as file:
            file.write(text.get('1.0', END))

# ================================ End =======================================

# =============================== save as File code ==============================
def save_as():
    global current_file
    file = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    if file:
        current_file = file.name
        file.write(text.get('1.0', END))
        file.close()
# ================================ End ============================================

# ================================ Exit Code =====================================
def exit():
    message = messagebox.askquestion('Notepad', "Do you want to save changes")
    if message == "yes":
        save_as()
    else:
        root.destroy()
# ==================================== end =========================================

# ======================================================================================
# ======================= Edit Code Starts Here  ============================
# ======================================================================================

# =========================== Cut code =============================
def cut():
    text.event_generate("<<Cut>>")

# =========================== End code =====================================

# =========================== Copy code =============================
def copy():
    text.event_generate("<<Copy>>")

# =========================== End code =====================================

# =========================== Paste code =============================
def paste():
    text.event_generate("<<Paste>>")

# =========================== End code =====================================

# =========================== Delete all code =============================
def delete():
    message = messagebox.askquestion('Notepad', "Do you want to Delete all")
    if message == "yes":
        text.delete('1.0', 'end')

# =========================== End code =====================================

# =========================== Select all code =============================
def select_all():
    text.tag_add('sel', '1.0', 'end')
    return 'break'
# =========================== End code =============================

# =========================== Time/Date code =============================
def time():
    d = datetime.now()
    text.insert('end', d)

# =========================== End code =============================

# ======================================================================================
# ======================= Format Code Starts Here  ============================
# ======================================================================================

def fonts():
    font_root = tk.Tk()
    font_root.geometry('400x400')
    font_root.title('Font')

    l1 = Label(font_root, text="Font:")
    l1.place(x=10, y=10)
    f = tk.StringVar()
    fonts = ttk.Combobox(font_root, width=15, textvariable=f, state='readonly', font=('verdana', 10, 'bold'))
    fonts['values'] = font.families()
    fonts.place(x=10, y=30)
    fonts.current(0)

    l2 = Label(font_root, text="Font Style:")
    l2.place(x=180, y=10)
    st = tk.StringVar()
    style = ttk.Combobox(font_root, width=15, textvariable=st, state='readonly', font=('verdana', 10, 'bold'))
    style['values'] = ('bold', 'bold italic', 'italic')
    style.place(x=180, y=30)
    style.current(0)

    l3 = Label(font_root, text="Size:")
    l3.place(x=350, y=10)
    sz = tk.StringVar()
    size = ttk.Combobox(font_root, width=2, textvariable=sz, state='readonly', font=('verdana', 10, 'bold'))
    size['values'] = (8, 9, 10, 12, 15, 20, 23, 25, 27, 30, 35, 40, 43, 47, 50, 55, 65, 76, 80, 90, 100, 150, 200, 255, 300)
    size.place(x=350, y=30)
    size.current(0)

    sample = LabelFrame(font_root, text="Sample", height=100, width=200)
    sample['font'] = (fonts.get(), size.get(), style.get())
    sample.place(x=180, y=220)

    l4 = Label(sample, text="This is sample")
    l4.place(x=20, y=30)

    def OK():
        text['font'] = (fonts.get(), size.get(), style.get())
        font_root.destroy()

    ok = Button(font_root, text="OK", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=OK)
    ok.place(x=137, y=350)

    def Apl():
        l4['font'] = (fonts.get(), size.get(), style.get())

    Apply = Button(font_root, text="Apply", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=Apl)
    Apply.place(x=210, y=350)

    def Cnl():
        font_root.destroy()

    cancel = Button(font_root, text="Cancel", relief=RIDGE, borderwidth=2, padx=20, command=Cnl)
    cancel.place(x=295, y=350)
    font_root.mainloop()

# ======================================================================================
# ======================= Format Code Ends Here  ============================
# ======================================================================================

# ======================================================================================
# ======================= Help Code Ends Here  ============================
# ======================================================================================

# ======================   View Help ===================================
def view_help():
    webbrowser.open('#')

# ============================= End =======================================

# ======================   Send Feedback ===================================
def send_feedback():
    webbrowser.open('#')

# ============================= End =======================================

# ======================================================================================
# ======================= Help Code Ends Here  ============================
# ======================================================================================

# ============================= Main Window =============================

root = tk.Tk()
root.geometry('600x300')
root.minsize(200, 100)
root.title('Notepad')
root.iconbitmap('C:\\Users\\aarju\\OneDrive\\Desktop\\Python\\Notepad\\notepad.ico')

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
file.add_command(label="New", command=new)
file.add_command(label="New window", command=new_window)
file.add_command(label="Open", command=Open)
file.add_command(label="Save", command=save)
file.add_command(label="Save as", command=save_as)
file.add_separator()
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))

edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: text.edit_undo())
edit.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: text.edit_redo())
edit.add_separator()
edit.add_command(label="Cut", command=cut)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
edit.add_command(label="Delete", command=delete)
edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
edit.add_command(label="Time/Date", accelerator="F5", command=time)
menubar.add_cascade(label="Edit", menu=edit)

Format = Menu(menubar, tearoff=0)
Format.add_command(label="Word Wrap")
Format.add_command(label="Font...", command=fonts)
menubar.add_cascade(label="Format", menu=Format)

Help = Menu(menubar, tearoff=0)
Help.add_command(label="View Help", command=view_help)
Help.add_command(label="Send FeedBack", command=send_feedback)
Help.add_command(label="About Notepad")
menubar.add_cascade(label="Help", menu=Help)

root.config(menu=menubar)

text = ScrolledText(root, width=1000, height=1000, undo=True)
text.place(x=0, y=0)

root.mainloop()
