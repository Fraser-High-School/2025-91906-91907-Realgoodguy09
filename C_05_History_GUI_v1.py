from tkinter import *
from functools import partial # To prevent unwanted windows


class Quiz:
    """
    Quiz program
    """

    def __init__(self):
        """
        QUiz program GUI
        """

        self.quiz_frame = Frame(padx=30, pady=30)
        self.quiz_frame.grid()


        self.to_history_button = Button(self.quiz_frame,
                                       text="History / Export",
                                       bg="#990099",
                                       fg="#FFFFFF",
                                       font=("Arial", "12", "bold"), width=12,
                                       command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Open History dialogue box and disables History button
        (So the user can't create multiple history boxes)
        """
        HistoryExport(self)


class HistoryExport:
    """
    Displays History box
    """
    
    def __init__(self, partner):
        # setup dialogue box and background color
        green_back = "#D5E8D4"
        peach_back = "#ffe6cc"

        self.history_box = Toplevel()

        # disables history button
        partner.to_history_button.config(state=DISABLED)

        # If user presses cross at the top, closes history and 
        # 'release' history button
        self.history_box.protocol('WM_DELETE_WINDOW', 
                                    partial(self.close_history, partner))
        
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for 'long' labels...
        recent_intro_txt = ("Below are your recent attempt - showing "
                            "3 / 3 attempts.")
        
        export_instructions_txt = ("Please push <Export> to save your attemptin a text "
                                "file. If the file name already exist, it will be overwritten.")
        
        attempts = ""

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt,("Arial", "11"), None],
            ["Attempt list", ("Arial", "14"), green_back],
            [export_instructions_txt,("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box,text=item[0], font=item[1],
                                bg=item[2],
                                wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            # Retrieve Export instruction label so that we can 
            # configure it to show the filename if the user exports the file
            self.export_filename_label = history_label_ref[3]

            # make frame hold buttons (two columns)
            self.hist_button_frame = Frame(self.history_box)
            self.hist_button_frame.grid(row=4)

            button_ref_list = []

            # button list(button text | bg colour | command | row | column)
            button_details_list = [
                ["Export", "#004C99", "", 0, 0]
                ["Close", "#666666", partial(self.close_history, partner), 0, 1]
            ]

            for btn in button_details_list:
                self.make_button = Button(self.hist_button_frame,
                                            font=("Arial", "12", "bold"),
                                            text=btn[0], bg=btn[1],
                                            fg="#FFFFFF", width=12,
                                            command=btn[2])
                self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

        
    def close_history(self, partner):
        """
        Closes the history dialogue box (and enableshistory button)
        """
        # put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()



# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Help")
    Quiz()
    root.mainloop()