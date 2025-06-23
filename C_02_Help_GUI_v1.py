from tkinter import *
from functools import partial # To preven unwated windows

class Quiz:
    """
    Quiz Program
    """

    def __init__(self):
        """
        Quiz program GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp,
            text="Help / Info",
            bg="#CC6600",
            fg="#FFFFFF",
            font=("Arial", "12", "bold"), width=10,
            command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        """
        Open Help dialogue box and disables help button
        (so the user can't create multiple help boxes)
        """
        DisplayHelp(self)




class DisplayHelp:
    """
    Displays dialogue box
    """

    def __init__(self,partner):
        # setup dialogue box and background color
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disables help button
        partner.to_help_button.config(state=DISABLED)

        # if user presses cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_help, partner))
        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)


        help_text = "To use the program enter the number of rounds you wish to do " \
                    "(Please note you will be able to quit even if you don't finish).  \n\n" \
                    "Please note that letters and numbers below 1 will result in "
                    "an error message.  \n\n" \
                    "To see your " \
                    "attempt history and export it to a text " \
                    "file, please click 'History' button"
        self.help_text_label = Label(self.help_frame,
                                        text=help_text, wraplength=350,
                                        justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Dismiss", bg="#CC6600",
                                    fg="#FFFFFF", 
                                    command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)
