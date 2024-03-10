from tkinter import* 

class QuizStarter:
    def __init__(self,parent):
        background_colour="Old Lace"
        #Frame set up
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label the widget heading 
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"))
        self.heading_label.grid(row=0)



#*****************Starting point of the program*************#
if __name__ =="part1":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    root.mainloop()