import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import main

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
        selected_image = Image.open(file_selected)
        out = main.get_output_img(selected_image)
        out.show("\"enhanced\" image")
        out.save("output.png")
    else:
        tkinter.messagebox.showerror("Error!", "Please fill out the fields, idiot.")

# Finish building display
submit = tkinter.Button(root, text="Launch program", command=launch)
submit.pack()

bottomtext = tkinter.Label(root, text="Find us on GitHub: https://github.com/NinjadenMu/python_image_enchancement")
bottomtext.pack()

root.mainloop() # required for Tkinter