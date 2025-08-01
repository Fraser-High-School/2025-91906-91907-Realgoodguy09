from tkinter import *

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
            ["Help", "#CC6600", "", 0, 2],
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
                
            else:
                has_errors = "yes"
        
        except ValueError:
            has_errors = "yes"

        # display error if neccessary
        if has_errors == "yes":
            self.round_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.round_entry.config(bg="#F4CCCC")
            self.round_entry.delete(0, END)


# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    quiz()
    root.mainloop()