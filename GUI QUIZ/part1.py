from tkinter import* 

names_list = []
global questions_answers

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?",
        'Speed up and get out of the way',
        'Slow down and drive carefully',
        'Slow down and stop',
        "Drive on as usual"
        "Slow down and stop" 
        
        ,3],

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

