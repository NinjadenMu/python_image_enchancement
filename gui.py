import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image, ImageTk
import main
import webbrowser
from functools import partial
import os
import copy

# Initiate Tkinter
root = tkinter.Tk()
root.title("python_image_enhancement")

# Function for file upload handling
selected_label = tkinter.Label(root, text="File selected: none")
file_selected = ""
def UploadAction(event=None):
    global file_selected
    global selected_label
    filename = tkinter.filedialog.askopenfilename()
    selected_label.config(text="File selected: " + filename)
    file_selected = filename

# Build display
fileselect = tkinter.Button(root, text="Select file", command=UploadAction)
fileselect.pack()
selected_label.pack() # display label after button

# main
def launch():
    global file_selected
    if file_selected != "":
        try:
            selected_image = Image.open(file_selected)
        except:
            tkinter.messagebox.showerror("Error!", "Your image file is corrupted, loser")
            return
        out = main.get_output_img(selected_image)
        newroot = tkinter.Tk()
        newroot.title("\"Enhanced\" Image")
        out_thumb = copy.deepcopy(out)
        out_thumb.thumbnail((500, 500))
        out_tk = ImageTk.PhotoImage(out_thumb, master=newroot, height=900)
        panel = tkinter.Label(newroot, image=out_tk)
        panel.image = out_tk
        panel.pack()
        def file_save(data):
            f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
            if f:
                abs_path = os.path.abspath(f.name)
                data.save(abs_path)
        savebutton = tkinter.Button(newroot, text="save as...", command=partial(file_save, out))
        savebutton.pack()
        newroot.mainloop()
    else:
        tkinter.messagebox.showerror("Error!", "Please fill out the fields, idiot.")

# Finish building display
submit = tkinter.Button(root, text="Launch program", command=launch)
submit.pack()

# Open in github button
def openGithubPage():
    webbrowser.open("https://github.com/NinjadenMu/python_image_enhancement")
bottomtext = tkinter.Button(root, text="Fork me on GitHub", command=openGithubPage)
bottomtext.pack()

root.mainloop() # required for Tkinter