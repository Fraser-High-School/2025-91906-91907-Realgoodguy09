from datetime import date

attempts = ["3 correct / 5 questions", "0 correct / 3 questions",
            "10 correct / 10 questions", "2 correct / 3 questions",
            "4 correct / 6 questions", "8 correct / 12 questions"]

# **** Get current date for heading the filename ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"attempts_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("***** Attempts *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your attempt history (oldest to newest)...\n")

    # write the item to file
    for item in attempts:
        text_file.write(item)
        text_file.write("\n")
