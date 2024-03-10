from tkinter import* 

class QuizStarter:
    def __init__(self,parent):
        background_color="Old Lace"
        #Frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label the widget heading 
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)

        self.user_label = Label (self.quiz_frame, text ="Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1)




#*****************Starting point of the program*************#
if __name__ =="part1":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop() #so the window doesnt dissapear 

