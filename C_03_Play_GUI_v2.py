from tkinter import *
from functools import partial # prevents unwanter windows

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


        # buttons(True, False, stats, hints, quit)
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=6)

        self.to_play_button = Button(self.quiz_frame,
                                     text="Play",
                                     bg="#004C99",
                                     fg="#FFFFFF",
                                     font=("Arial", "12", "bold"), width=10,
                                     command=self.to_play)
        self.to_play_button.grid(row=1, padx=5, pady=5)


    def to_play(self):
        """
        Opens Play GUI and disables / hides first GUI
        """
        StartPlay(self)



class StartPlay:
    """
    Opens Play GUI
    """

    def __init__(self, partner):
        # set up GUI box and background color
        background = "#ffe6cc"
        self.play_box = Toplevel()

        # disables Play button
        partner.to_play_button.config(state=DISABLED)

        # If user presses the cross at the top, closes Play and 
        # 'releases' play button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play, partner))
        self.play_frame = Frame(self.play_box, width=300, 
                                height=200)
        self.play_frame.grid()





        # buttons(True, False, stats, hints, quit)
        self.button_frame_play = Frame(self.play_frame)
        self.button_frame_play.grid(row=6)

        # button list (Button text | bg colour | command | row | column)
        button_details_list_play = [
            ["True", "#004C99", "", 1, 0],
            ["False", "#990099", "", 1, 2],
            ["Hint", "#CC6600", "", 3, 0],
            ["Quit", "#990000", partial(self.close_play, partner), 3, 1],
            ["Stats", "#2C9C00", "", 3, 2]
        ]

        # List to hold the buttons once they've been made
        self.button_ref_list = []

        for item in button_details_list_play:
            self.make_button = Button(self.button_frame_play,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=5, height=2, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=20)

            self.button_ref_list.append(self.make_button)

    def close_play(self, partner):
        """
        Close Play GUI (and enable help button)
        """
        # Put help button back to normal
        partner.to_play_button.config(state=NORMAL)
        self.play_box.destroy()


        







# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Play")
    quiz()
    root.mainloop()