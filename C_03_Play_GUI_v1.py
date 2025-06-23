from tkinter import *

class play():
    """
    A Quiz Program
    """

    def __init__(self):

        """
        Play game GUI
        """

        self.play_frame = Frame(padx=30, pady=30)
        self.play_frame.grid()

        self.play_heading = Label(self.play_heading,
            text="Play",
            font= ("Arial", "24", "bold"))
        self.play_heading.grid(row=0)
