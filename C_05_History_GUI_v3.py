from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c
from datetime import date

class Quiz:
    """
    Quiz program
    """

    def __init__(self):
        """
        QUiz program GUI
        """

        #self.all_attempts_list = ["3 correct / 5 questions", "0 correct / 3 questions",
        #                          "10 correct / 10 questions", "2 correct / 3 questions",
        #                          "4 correct / 6 questions", "8 correct / 12 questions"]

        self.all_attempts_list = ["3 correct / 5 questions", "0 correct / 3 questions",
                                  "10 correct / 10 questions", "2 correct / 3 questions",
                                  "4 correct / 6 questions", "This is a test"]


        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()


        self.to_history_button = Button(self.quiz_frame,
                                       text="History / Export",
                                       bg="#990099",
                                       fg="#FFFFFF",
                                       font=("Arial", "14", "bold"), width=12,
                                       command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Open History dialogue box and disables History button
        (So the user can't create multiple history boxes)
        """
        HistoryExport(self, self.all_attempts_list)

class HistoryExport:
    """
    Displays History box
    """  
    def __init__(self, partner, attempts):

        self.history_box = Toplevel()

        # disables history button
        partner.to_history_button.config(state=DISABLED)

        # If user presses cross at the top, closes history and 
        # 'release' history button
        self.history_box.protocol('WM_DELETE_WINDOW', 
                                    partial(self.close_history, partner))
        
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background color and text for attempt area
        if len(attempts) <= c.MAX_ATTS:
            att_back = "#D5E8D4"
            att_amount = "all your"
        else:
            att_back = "#ffe6cc"
            att_amount = (f"Your recent attempts - "
                           f"showing {c.MAX_ATTS} / {len(attempts)}")

        # strings for 'long' labels...
        recent_intro_txt = (f"Below are {att_amount} attempts.")
        newest_first_string = ""
        newest_first_list = list(reversed(attempts))

        if len(newest_first_list) <= c.MAX_ATTS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # if we have more than five items
        else:
            for item in newest_first_list[:c.MAX_ATTS - 1]:
                newest_first_string += item + "\n"
        
            newest_first_string += newest_first_list[c.MAX_ATTS - 1]

            
        # create string from attempt list (newest attempts first)
        export_instructions_txt = ("Please push <Export> to save your attempt in a text "
                                "file. If the file name already exist, it will be overwritten.")
        


        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt,("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), att_back],
            [export_instructions_txt,("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                                bg=item[2],
                                wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # Retrieve Export instruction label so that we can 
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        

        # button list(button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(attempts), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                        font=("Arial", "12", "bold"),
                                        text=btn[0], bg=btn[1],
                                        fg="#FFFFFF", width=12,
                                        command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

        
    def export_data(self, attempts):

        # **** Get current date for heading the filename ****
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"attempts_{year}_{month}_{day}"

        # edit label so users know that their export has been done 
        success_string = ("Export Successful!   The file is called "
                          f"{file_name}.text")
        self.export_filename_label.config(fg="#009900", text = success_string,
                                          font=("Arial", "12", "bold"))

        # write data to a text file
        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:

            text_file.write("***** Attempts *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your attempt history (oldest to newest)...\n")

            # write the item to file
            for item in attempts:
                text_file.write(item)
                text_file.write("\n")

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
    root.title("Quiz")
    Quiz()
    root.mainloop()