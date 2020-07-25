from PIL import ImageTk, Image
import PIL
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("TDC Photo Viewer")

val = []
path = []
count = 0
click = False

initial_image = ImageTk.PhotoImage(PIL.Image.open("Logo.png"))
container = Label(image = initial_image)
container.grid(row = 0, column = 0, columnspan = 3)

def showImage():
    global count, container
    if not click:
        openImage = Button(window, text = "Select Images here...", command = lambda: selectImage())
        openImage.grid(row = 1, column = 1)
    
    if path:
        container.grid_forget()
        image_name = path[count].split('/')

        #setting the name of the image as the window title
        window.title(image_name[-1])

        current_image = ImageTk.PhotoImage(image = PIL.Image.open(path[count]).resize((980, 720)))
        container = Label(image = current_image)
        container.image = current_image
        container.grid(row = 0, column = 0, columnspan = 3)

def selectImage():
    global val, path, click
    
    #Clicked here to select images
    click = True
    val = filedialog.askopenfiles(filetypes = (("png files", "*.png"), ("All Files", "*")))
    if val:
        path = [v.name for v in val]
    else:
        print("Please Select an Image")

def prev_next_trigger(triggered_element):
    global count, click
    #find if the next or prev button is pressed
    if click:
        if triggered_element == "left_click":
            if count == 0:
                count = len(val) - 1
            else:
                count -= 1
        elif triggered_element == "right_click":
            if count == len(val) - 1:
                count = 0
            else:
                count += 1
    
    #Displaying Image on the window
    showImage()

#Buttons
leftButton = Button(window, text = "<", command = lambda: prev_next_trigger("left_click"))
leftButton.grid(row = 1, column = 0)

rightButton = Button(window, text = ">", command = lambda: prev_next_trigger("right_click"))
rightButton.grid(row = 1, column = 2)

showImage()
window.mainloop()