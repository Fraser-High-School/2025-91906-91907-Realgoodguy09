from tkinter import *
from functools import partial # To prevent unwanted tabs

min_rounds = 1


class quiz():
    """
    A Quiz Program
    """

    def __init__(self):

        """
        Quiz program GUI
        """

        self.quiz_frame = Frame(padx=30, pady=30)
        self.quiz_frame.grid()

    
        self.quiz_heading = Label(self.quiz_frame,
                                text="Quiz",
                                font=("Arial","24","bold")
                                )
        self.quiz_heading.grid(row=0)

        instructions = ("Enter the number of rounds you wish to play.")
        self.quiz_instructions = Label(self.quiz_frame,
            text=instructions,
            wraplength=250, width=40,
            justify="left")
        self.quiz_instructions.grid(row=1)

        self.round_entry = Entry(self.quiz_frame, 
            font=("Arial","14"))
        self.round_entry.grid(row=3, padx=10, pady=10)

        error = "Please enter a whole number"
        self.round_error = Label(self.quiz_frame, text=error,
            fg="#9C0000")
        self.round_error.grid(row=2)

        # Play, help and history buttons
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=6)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Play", "#004C99", lambda:self.check_rounds(min_rounds), 0, 1],
            ["Help", "#CC6600", self.to_help, 0, 2],
            ["History", "#990099", "", 0, 0]
        ]

        # List to hold the buttons once they've been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                    text=item[0], bg=item[1],
                                    fg="#FFFFFF", font=("Arial", "12", "bold"),
                                    width=10, height=2, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=20)                      

            self.button_ref_list.append(self.make_button)

        # retieve 'history / export' button and disable it at the start
        self.to_histroy_button = self.button_ref_list[2].config(state=DISABLED)

        # retrive 'help' button so it can be disabled later
        self.to_help_button = self.button_ref_list[1]

    def to_help(self):
        """
        Open Help dialogue box and disables help button
        (so the user can't create multiple help boxes)
        """
        DisplayHelp(self)


    def check_rounds(self, min_rounds):
        """
        Checks the selected number of rounds is a whole number and either continues to the 
        next GUI of shows custom error
        """

        # Retrieves rounds
        round_num = self.round_entry.get()

        # Resets label and entry box (if there was an error)
        self.round_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.round_entry.config(bg="#FFFFFF")

        error = f"Enter a whole number equal or higher than {min_rounds}"
        has_errors = "no"
        # checks that the number of rounds is a whole number
        try:
            round_num = int(round_num)
            if round_num >= min_rounds:
                error = ""
                play(self, round_num)
                
                
            else:
                has_errors = "yes"
        
        except ValueError:
            has_errors = "yes"

        # display error if neccessary
        if has_errors == "yes":
            self.round_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.round_entry.config(bg="#F4CCCC")
            self.round_entry.delete(0, END)

    def to_play(self):
        """
        Opens Play GUI and disables or hides initial GUI
        """
        play(self)




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
                    "Please note that letters and numbers below 1 will result in "  \
                    "an error message..   \n\n" \
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
        
        # List and loop to set background color on
        # everything except buttons
        recolor_list = [self.help_frame, self.help_heading_label,
        self.help_text_label]

        for item in recolor_list:
            item.config(bg=background)

    
    def close_help(self, partner):
        """
        Close help dialogue box (and enable help button)
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

class play:
    """
    A Quiz Program
    """

    def __init__(self, round_num):

        """
        Play game GUI
        """

        self.play_frame = Frame(padx=30, pady=30)
        self.play_frame.grid()


        # buttons(True, False, stats, hints, quit)
        self.button_frame = Frame(self.play_frame)
        self.button_frame.grid(row=6)

        # button list (Button text | bg colour | command | row | column)
        button_details_list = [
            ["True", "#004C99", "", 1, 0],
            ["False", "#990099", "", 1, 2],
            ["Hint", "#CC6600", "", 3, 0],
            ["Quit", "#990000", "", 3, 1],
            ["Stats", "#2C9C00", "", 3, 2]
        ]

        # List to hold the buttons once they've been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=5, height=2, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=20)

            self.button_ref_list.append(self.make_button)



if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    quiz()
    root.mainloop()