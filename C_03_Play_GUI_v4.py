from tkinter import *
from functools import partial # prevents unwanter windows
import random

# List of True/False questions for the Quiz
# Question list (Question | Answer | explanation)
true_false_question_list = [
    ["An atom is the smallest particle.", False, "False - there are subatomic particles that are smaller"],
    ["Arachnophobia is the fear of bathing.", False, "False - Ablutophobia is the fear of bathing"],
    ["Boiling water is 100 degrees Celsius.", True, "True - that's also 212 degrees Fahrenheit"],
    ["Butterflies taste things with their feet.", False, "False - butterflies taste with their feet"],
    ["Colorblind people can see color.", True, "True - some colorblind poeple can see very narrow ranges of color"],
    ["Family Feud and Jeopardy are among the most-watched game shows of all time", True, "True - The Price is Right is another favourite"],
    ["Golf balls have 300 to 500 dimples", True, "True - all golfs balls don't have the same number of dimples"],
    ["John Glenn was one of the oldest astronauts to travel in space.", True, "True - he was 77 years old"],
    ["Lightning can't strike the same place twice.", False, "False - lightning can actually strike in the same place more than one time."],
    ["NFL teams are divided into three conferences.", False, "False - it's divided into two conferences, the American Football Conference and National Football Conference"],
    ["Scotland's national animal is a unicorn.", True, "True - it's the official animal of Scotland."],
    ["The record for the tallest human in the world is almost 9 feet tall.", True, "True - Robert Wadlow measured 8 feet 11 inches."],
    ["The Statue of Liberty is the world's tallest monument.", False, "False - The State of Unity is the world's tallest monument."],
    ["The sun is not a star.", False, "False - the sun is actually a star."],
    ["Three strikes in a row in bowling is called an eagle.", False, "False - it's called a turkey."],
    ["A cheetah is the fastest animal on the planet.", False, "False - they're just the fastest land animal."],
    ["A dog pants its tongue because it's sweating.", False, "False - dogs sweat through their paws."],
    ["An octopus has one heart.", False, "False - it has three hearts."],
    ["Ants can withstand up to 5,000 times their body weight.", True, "True - they may be small, but they can hold a lot."],
    ["Bats are blind.", False, "False - bats can see, they just use ultrasound to help direct them."],
    ["Dinosaurs are the biggest animals to ever live.", False, "False - it's the blue whale."],
    ["Galapagos tortoises can go up to a year without water or food.", True, "True - they also sleep a lot; up to 16 hours each day."],
    ["Herbivores eat animals.", False, "False - herbivores eat plants."],
    ["Pigs roll in the mud because it helps to keep them cool.", True, "True - pigs don't have many sweat glands to help cool them."],
    ["Pufferfish are always edible.", False, "False - if you don't cook them properly, they can be lethal to eat."],
    ["Sharks are mammals.", False, "False - sharks are considered to be fish."],
    ["Sloths take two weeks to digest food.", True, "True - in fact, they have the slowest digestion of any mammal."],
    ["The blue whale is the biggest animal to have ever lived.", True, "True - they weigh up to 300,000 pounds and can be over 100 feet long."],
    ["The ostrich egg is the world's smallest bird egg.", False, "False - the ostrich egg is the world's largest bird egg."],
    ["The process of creating honey involves bees' waste.", False, "False - it involves bees vomiting."],
    ["Lions are more likely to hunt down a human than a tiger.", False, "False - a tiger is more likely than a lion."],
    ["Apples and pears are a part of the rose family.", True, "True - so are peaches and plums."],
    ["Cake is the most popular dessert.", False, "False - people tend to love pie more than cake."],
    ["Cauliflower is the only vegetable that's also a flower.", False, "False - broccoli also fits this description."],
    ["Dark chocolate is actually good for you.", True, "True - it contains antioxidants that fight disease."],
    ["Drinking too much milk can cause health issues.", True, "True - it can cause problems with gut health, among others."],
    ["France is responsible for giving us French fries.", False, "False - Despite their name, Belgium actually introduced French fries."],
    ["Grasshoppers are mainly eaten in the United States.", False, "False - they're eaten mostly in Mexico and parts of Central America."],
    ["Grilled cheese is the most popular sandwich in the United States.", True, "True - and often enjoyed with tomato soup."],
    ["Ketchup was once used as a medicine.", True, "True - it was used to cure sicknesses like diarrhea and indigestion."],
    ["Mushrooms are the most popular pizza topping in the U.S.", False, "False - it's pepperoni."],
    ["Red wine may be good for your heart.", True, "True - the key word is 'may,' but there are studies that support this."],
    ["Romaine is the best-known lettuce in the U.S.", False, "False - iceberg lettuce is the most well-known in the U.S."],
    ["Saffron is the most expensive spice in the world.", True, "True - to make one pound of saffron spice, it takes 75,000 flowers."],
    ["Soda is the most popular beverage on the planet.", False, "False - water is the most popular drink."],
    ["Snails are safe to eat.", True, "True - as long as they are cooked properly."],
    ["Strawberries are not actually berries.", True, "True - they're called 'false fruits,' with several individual fruits that make it up."],
    ["Tomatoes are vegetables.", False, "False - tomatoes are classified as fruits."],
    ["Yogurt was the first food that astronauts ate in space.", False, "False - applesauce is the first food they ate."],
    ["Boston hosted the first St. Patrick's Day parade.", True, "True - the city hosted the parade in 1737."],
    ["Canada celebrates Thanksgiving on a different day than the United States.", True, "True - the U.S. celebrates in November and Canada celebrates in October."],
    ["Cupid is the god of love.", False, "False - Eros is the god of love in Greek mythology."],
    ["Eating chicken on Christmas is a tradition in Japan.", True, "True - Kentucky Fried Chicken is the food of choice to celebrate the holiday."],
    ["Hanukkah lasts for seven days.", False, "False - it lasts for eight days."],
    ["Juneteenth has been an official holiday since the 1960s.", False, "False - Juneteenth was signed into federal law as a holiday in 2021."],
    ["Kwanzaa is observed for five days.", False, "False - it's celebrated for seven days."],
    ["The Chinese lunar calendar determines when the Chinese New Year is celebrated.", True, "True - usually in January or February."],
    ["The tradition of dyeing Easter Eggs started in France.", False, "False - the tradition started in Ukraine."],
    ["Valentine's Day is named for St. Valentine.", True, "True - his name became synonymous with the day of love."],
    ["Bhutan is the most mountainous country.", True, "True - mountains cover almost 99 percent of its area."],
    ["California is the most populous U.S. state.", True, "True - it has about 39 million people."],
    ["Canada has the longest coastline on Earth.", True, "True - it measures 151,019 miles."],
    ["Delaware is the smallest U.S. state.", False, "False - it's Rhode Island."],
    ["Greenland is three times the size of the state of Texas.", True, "True - it's the largest island in the world."],
    ["Hawaii has more active volcanoes than any other U.S. state.", False, "False - it's actually Alaska, with almost 150 active volcanoes."],
    ["Mount Everest is the tallest mountain on Earth.", True, "True - it has an elevation of over 29,000 feet."],
    ["South Africa has three capitals.", True, "True - Bloemfontein, Cape Town and Pretoria."],
    ["The Chunnel runs between England and Scotland.", False, "False - it connects England and France."],
    ["The Great Wall of China measures the length of the equator.", False, "False - at over 13,000 miles, its distance is actually half of the equator's length."],
    ["The Pacific Ocean is the biggest ocean on Earth.", True, "True - it covers over 60 million square miles."],
    ["The world's highest waterfall is in South Africa.", False, "False - it's in Venezuela."],
    ["Vatican City is almost 100 times smaller than Manhattan.", True, "True - it's the world's smallest country."],
    ["A human brain is the organ with the most fat.", True, "True - about 60 percent of the human brain is fat."],
    ["A person can survive a month without water.", False, "False - people can survive about three days, on average, without water."],
    ["All of your taste buds are on your tongue.", False, "False - you also have taste buds in your nose and sinuses."],
    ["An average human head weighs about 20 pounds.", False, "False - it weighs about 11 pounds on average."],
    ["Humans don't lose hair on a daily basis.", False, "False - humans lose roughly 75 strands of hair every day."],
    ["Humans lose most of their heat through their heads.", True, "True - about 80 percent of heat escapes through the head."],
    ["People are born with more bones than they have in adulthood.", True, "True - babies have 300 bones at birth, but have closer to 200 when they become adults."],
    ["The human body has three lungs.", False, "False - it has two lungs."],
    ["The human body is 20 percent water.", False, "False - the human body is about 60 percent water."],
    ["The liver is the second heaviest organ in the body.", True, "True - the liver comes in second to skin."],
    ["The skin is the body's largest organ.", True, "True - and it regenerates about every month."],
    ["There are five bones in the human ear.", False, "False - there are three bones in the ear."],
    ["You can really die of a broken heart.", True, "True - doctors say it's called broken heart syndrome."],
    ["Cars was Pixar's first movie.", False, "False - it was Toy Story."],
    ["Disney's first full-color animated film was Snow White and the Seven Dwarfs.", True, "True - it was released in 1937."],
    ["Disney's shortest feature film is less than an hour long.", False, "False - the shortest movie, Dumbo, is 64 minutes long."],
    ["Fantasia is Disney's longest animated movie.", True, "True - the movie is 126 minutes long."],
    ["Goofy has had several names over the years.", True, "True - among them, Goofus D. Dawg."],
    ["Minnie Mouse's real name is Minerva Mouse.", True, "True - she does have a real name!"]
    ]
num_round=3
rounds_played = 0
ran_question = random.choice(true_false_question_list)
question = ran_question[0]
answer = ran_question[1]
explanation = ran_question[2]
true_false_question_list.remove(ran_question)
print(ran_question)
print(question)
print(answer)
print(explanation)




# Opening GUI
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


# Play screen GUI
class StartPlay:
    """
    Opens Play GUI
    """

    def __init__(self, partner):
        # set up GUI box and background color
        background = "#ffe6cc"
        self.play_box = Toplevel()
        print(question)

        # disables Play button
        partner.to_play_button.config(state=DISABLED)

        # If user presses the cross at the top, closes Play and 
        # 'releases' play button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play, partner))
        self.play_frame = Frame(self.play_box, width=500, 
                                height=400)
        self.play_frame.grid()
        


        self.answer_explantion = Label(self.play_frame, text="",
                                       fg="#9C0000")
        self.answer_explantion.grid(row=3)


        print(question+"I have no idea")
        self.play_text_question = Label(self.play_frame,
                                     text=question, wraplength=350,
                                     justify="left")
        self.play_text_question.grid(row=1, padx=10)
 
        





        # buttons(True, False, stats, hints, quit)
        self.button_frame_play = Frame(self.play_frame)
        self.button_frame_play.grid(row=6)

        # button list (Button text | bg colour | command | row | column)
        button_details_list_play = [
            ["True", "#004C99", lambda: self.answer_true(answer, explanation, num_round, rounds_played, ran_question), 1, 0],
            ["False", "#990099", lambda: self.answer_false(answer, explanation, num_round, rounds_played, ran_question), 1, 2],
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



    def answer_true(self, answer, explanation, num_round, rounds_played, ran_question):
        choice = True
        correct_answer = ""



        self.answer_explantion.config(fg="#004C99", font=("Arial", "13", "bold"))


        

        if choice == answer:
            correct_answer = "yes"


        elif choice != answer:
            correct_answer = "no"


        # Confrims if answer is correct or incorrect

        if correct_answer == "yes":
            self.answer_explantion.config(text=explanation, fg="#004C99", font=("Arial", "10", "bold"))

            
            # Checks to see if chosen number of rounds have been played
            if rounds_played == num_round:
                quit()
            
            else:
                self.change_variables()


                self.play_text_question.config(text=question, fg="#004C99", font=("Arial", "10", "bold"))   

        elif correct_answer == "no":
            self.answer_explantion.config(text=explanation, fg="#9C0000", font=("Arial", "10", "bold"))
            
            
            # Checks to see if chosen number of rounds have been played
            if rounds_played == num_round:
                quit()
            
            else:
                self.change_variables()


                self.play_text_question.config(text=question, fg="#004C99", font=("Arial", "10", "bold"))     


         
            






    def answer_false(self, answer, explanation, num_round, rounds_played, ran_question):
        choice = False
        correct_answer = ""



        self.answer_explantion.config(fg="#004C99", font=("Arial", "13", "bold"))


        

        if choice == answer:
            correct_answer = "yes"


        elif choice != answer:
            correct_answer = "no"


        # Confrims if answer is correct or incorrect

        if correct_answer == "yes":
            self.answer_explantion.config(text=explanation, fg="#004C99", font=("Arial", "10", "bold"))

            
            # Checks to see if chosen number of rounds have been played
            if rounds_played == num_round:
                quit()
            
            else:
                self.change_variables()


                self.play_text_question.config(text=question, fg="#004C99", font=("Arial", "10", "bold"))   

        elif correct_answer == "no":
            self.answer_explantion.config(text=explanation, fg="#9C0000", font=("Arial", "10", "bold"))
            
            
            # Checks to see if chosen number of rounds have been played
            if rounds_played == num_round:
                quit()
            
            else:
                self.change_variables()
   



    def change_variables(self):
        ran_question = random.choice(true_false_question_list)
        global question
        global answer
        global explanation
        global rounds_played
        question = ran_question[0]
        answer = ran_question[1]
        explanation = ran_question[2]
        true_false_question_list.remove(ran_question)
        rounds_played += 1

        self.play_text_question.config(text=question, fg="#004C99", font=("Arial", "10", "bold"))


    









# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Play")
    quiz()
    root.mainloop()
