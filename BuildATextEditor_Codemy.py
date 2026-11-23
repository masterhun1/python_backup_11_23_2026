

"""

Tkinter 
Youtube
@Codemycom
"Build A Text Editor - Python Tkinter GUI Tutorial #104"

"""

import tkinter
from tkinter import filedialog 
from tkinter import font 

root = tkinter.Tk()
root.title("Codemy.com - Textpad")
# root.iconbitpam('c://gui/codemy.ico')
root.geometry("800x500")

# Create main frame 
my_frame = tkinter.Frame(root)
my_frame.pack(pady=5)

# Create out Scrollbar for the Text Box 
text_scroll = tkinter.Scrollbar(my_frame)
text_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Create Text Box 
my_text = tkinter.Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our Scrollbar 
text_scroll.config(command=my_text.yview)

# Create Menu 
my_menu = tkinter.Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar to the bottom
status_bar = tkinter.Label(root, text="Ready ", anchor=tkinter.E)
status_bar.pack(fill=tkinter.X, side=tkinter.BOTTOM, ipady=5)





root.mainloop()

