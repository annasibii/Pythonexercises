from tkinter import* 

class Student:
    def __init__(self, name):
        self.first_name = name

    def display_name(self):
        print(self.first_name)
  
    def set_grade(self,grade):
        self.grade = grade 

    def get_grade(self):
        return self.grade

def show_grade():
    #show the grade using a label
    grade_label.config(text=csc_2[0].get_grade())

csc_2 = []

csc_2.append(Student("Anna"))
csc_2[0].set_grade("Excellence")

csc_2.append(Student("Rehaan"))
csc_2[0].set_grade("Excellence")

csc_2.append(Student("Aaran"))
csc_2[0].set_grade("Excellence")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Anna")
students_listbox.insert(1, "Rehaan")
students_listbox.insert(2, "Aaran")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
