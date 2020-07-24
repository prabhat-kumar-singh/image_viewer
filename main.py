from PIL import ImageTk, Image
import PIL
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("TDC Photo Viewer")
window.geometry('1080x740')

initial_image = ImageTk.PhotoImage(PIL.Image.open("c:/Users/MY HP/Downloads/sdf.png"))
val = []
path = []
count = 0
current_image = ""
click = False
#Select Images from a directory

def showImage():
    global count
    if not click:
        openImage = Button(window, text = "Select Images here...", command = lambda: selectImage())
        openImage.grid(row = 1, column = 1)

    if path:
        print(path[count])
        current_image = ImageTk.PhotoImage(PIL.Image.open(path[count]))
        image_container = Label(image = current_image)
        image_container.grid(row = 0, column = 0, columnspan = 3)
    else:
        initial_container = Label(image = initial_image)
        initial_container.grid(row = 0, column = 0, columnspan = 3)

def selectImage():
    global val, path
    val = filedialog.askopenfiles(filetypes = (("png files", "*.png"), ("All Files", "*")))
    if val:
        path = [v.name for v in val]
    else:
        print("Please Select an Image")

def prev_next_trigger(triggered_element):
    global count, click
    #clicked on the button
    click = True
    if triggered_element == "left_click":
        print("Left click")
        if count == 0:
            count = len(val) - 1
        else:
            count -= 1
    elif triggered_element == "right_click":
        print("Right Click")
        if count == len(val) - 1:
            count = 0
        else:
            count += 1
    showImage()

#Buttons
leftButton = Button(window, text = "<", command = lambda: prev_next_trigger("left_click"))
leftButton.grid(row = 1, column = 0)

rightButton = Button(window, text = ">", command = lambda: prev_next_trigger("right_click"))
rightButton.grid(row = 1, column = 2)

showImage()
window.mainloop()