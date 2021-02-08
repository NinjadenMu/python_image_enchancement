import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import main

# Initiate Tkinter
root = tkinter.Tk()
root.title("python_image_enhancement")

# Function for file upload handling
file_selected = ""
def UploadAction(event=None):
    global file_selected
    filename = tkinter.filedialog.askopenfilename()
    print("Selected:", filename)
    file_selected = filename

# Build display

fileselect = tkinter.Button(root, text="Select file", command=UploadAction)
fileselect.pack()

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