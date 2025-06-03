from tkinter import *

class Converter():
    """
    A Quiz Program
    """

    def __init__(self):

        """
        Quiz program GUI
        """

        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid

    # 
    self.quiz_heading = Label(self.quiz_frame,
                            text="Quiz",
                            font=("Arial","16","bold")
                            )
    self.quiz_heading.grid(row=0)

    # Play, help and history buttons
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    # button list (button text | bg colour | command | row | column)
    button_details_list = [
        ["Play", "#004C99", "", 0, 0],
        ["Help", "#CC6600", "", 0, -1],
        ["History", "#990099", "", 0, 1]
    ]

    # List to hold the buttons once they've been made
    self.button_ref_list = []

    for item in button_details_list:
        self.make_button = Button(self.button_frame,
                                text=item[0], bg=item[1],
                                fg="#FFFFFF", font=("Arial", "12", "bold"),
                                width=12, command=item[2])
        self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)                      

        self.button_ref_list.append(self.make_button)