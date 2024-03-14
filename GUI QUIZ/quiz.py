from tkinter import* 

names_list = []
global questions_answers

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?",
        'Speed up and get out of the way',
        'Slow down and drive carefully',
        'Slow down and stop',
        "Drive on as usual", 3],

    2: ["You may stop on a motorway only:", 
        'if there is an emergency',
        'To let down or pick up passengers',
        'to make a U turn', 
        'to stop and take a photo', 
        'if there is an emergency', 1],

    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?",
        "Speed up before the pedestrians cross",
        'Stop and give way to pedestrians on any part of the crossing',
        "Sound the horn on your vehicile to warn the pedestrians",
        "Slow down to 30 kmh",
        'Stop and give way to pedestrians on any part of the crossing',2,],

    4: ["Can you stop on a bus stop in a private motor vehicle?", 
        'Only between midnight and 6am',
        "Under no circumstances",
        "When dropping off passengers",
        'Only if it is less than 5 minutes',
        "Under no circumstances", 2],

    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)",
        '70 km/h',
        "100km/h so you do not hold up traffic",
        "80 km/h and if the wheel spacer displays a lower limit that applies",3,],
    
    6: ["When following another vehicle on a dusty road, you should:",
        'Speed up to get passed', 
        "Turn your bechicle's windscreen wipers on",
        "Stay back from the dust cloud",
        'Turn your vehicles headlights on', 
        "Stay back from the dust cloud",3,],

    7: ["What does the sign containing the letters 'LSZ' mean", 
        'Low safety zone', 
        "Low stability zone",
        "Lone star zone",
        'Limited speed zone',
        ""


    ]


}


class QuizStarter:
    def __init__(self,parent):
        background_color="Old Lace"
        #Frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label the widget heading 
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)

        #Label for user name prompt
        self.user_label = Label (self.quiz_frame, text ="Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1)

        #Users input is taken by an Entry Widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)

        #continue button 
        self.continue_button = Button (self.quiz_frame, text="Continue", bg="pink", command=self.name_collection)
        self.continue_button.grid (row=3, pady=20)
    
    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()


#*****************Starting point of the program*************#
if __name__ =="__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop() #so the window doesnt dissapear 

