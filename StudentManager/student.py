from tkinter import* 

class Student ():
    def _init_(self):
        self.first_name = "John"


    def display_name(self):
        print(self.first_name)
  
    def set_grade(self,grade):
        self.grade = grade 

    def get_grade(self):
        return self.grade

def show_grade():
    #show the grade using a label
    grade_label.config(text=csc_2[0].grade())
    pass

csc_2 = []

csc_2.append(Student("Anna"))
csc_2[0].set_grade("Excellence")

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
