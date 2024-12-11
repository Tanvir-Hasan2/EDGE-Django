# Importing the tkinter module for creating the GUI
from tkinter import *

# Class definition for creating the calculator window
class MyWindow:
    def __init__(self, win):
        # Labels for input fields and result display
        self.lbl1 = Label(win, text='First number')  # Label for the first number
        self.lbl2 = Label(win, text='Second number') # Label for the second number
        self.lbl3 = Label(win, text='Result')        # Label for the result

        # Entry fields for user input
        self.t1 = Entry(bd=3)  # Entry field for the first number
        self.t2 = Entry()      # Entry field for the second number
        self.t3 = Entry()      # Entry field for displaying the result

        # Buttons for each arithmetic operation
        self.btn1 = Button(win, text='Add')           # Add button
        self.btn2 = Button(win, text='Subtract')      # Subtract button
        self.btn3 = Button(win, text='Multiplication')# Multiplication button
        self.btn4 = Button(win, text='Division')      # Division button

        # Placing the labels and entry fields at specific coordinates in the window
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

        # Buttons with functionality
        self.b1 = Button(win, text='Add', command=self.add)     # Add button with a function call
        self.b2 = Button(win, text='Subtract')                   # Subtract button
        self.b2.bind('<Button-1>', self.sub)                     # Subtract button uses event binding
        self.b3 = Button(win, text="Multiplication")             # Multiplication button
        self.b3.bind('<Button-1>', self.mul)                     # Multiplication button uses event binding
        self.b4 = Button(win, text="Division")                   # Division button
        self.b4.bind('<Button-1>', self.div)                     # Division button uses event binding

        # Placing the operation buttons on the window
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.b4.place(x=400, y=150)

    # Method for addition
    def add(self):
        self.t3.delete(0, 'end')  # Clear any previous result
        num1 = int(self.t1.get())  # Get the first number from the input field
        num2 = int(self.t2.get())  # Get the second number from the input field
        result = num1 + num2  # Perform the addition
        self.t3.insert(END, str(result))  # Insert the result into the result field

    # Method for subtraction, bound to the subtract button
    def sub(self, event):
        self.t3.delete(0, 'end')  # Clear the result field
        num1 = int(self.t1.get())  # Get the first number
        num2 = int(self.t2.get())  # Get the second number
        result = num1 - num2  # Perform subtraction
        self.t3.insert(END, str(result))  # Display the result

    # Method for multiplication, bound to the multiplication button
    def mul(self, event):
        self.t3.delete(0, 'end')  # Clear the result field
        num1 = int(self.t1.get())  # Get the first number
        num2 = int(self.t2.get())  # Get the second number
        result = num1 * num2  # Perform multiplication
        self.t3.insert(END, str(result))  # Display the result

    # Method for division, bound to the division button
    def div(self, event):
        self.t3.delete(0, 'end')  # Clear the result field
        num1 = int(self.t1.get())  # Get the first number
        num2 = int(self.t2.get())  # Get the second number
        result = num1 / num2  # Perform division
        self.t3.insert(END, str(result))  # Display the result

# Setting up the main window for Tkinter
window = Tk()

# Creating an instance of MyWindow
mywin = MyWindow(window)

# Setting the title of the window
window.title('Tkinter Arithmetic Operations')

# Setting the geometry (size) of the window
window.geometry("700x500+10+10")

# Mainloop to keep the window open
window.mainloop()
