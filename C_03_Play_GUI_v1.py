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


        # buttons(True, False, stats, hints, quit)
        self.button_frame = Frame(self.play_frame)
        self.button_frame.grid(row=6)

        # button list (Button text | bg colour | command | row | column)
        button_details_list = [
            ["True", "#004C99", "", 0, 0],
            ["False", "#990099", "", 0, 2],
            ["Hint", "#CC6600", "", 2, 0],
            ["Quit", "#990000", "", 2, 1],
            ["Stats", "#2C9C00", "", 2, 2]
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




# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Play")
    play()
    root.mainloop()