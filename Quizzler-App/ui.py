from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(x=150, y=125, width=280, text="Question text", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage('Users/finneassensiba/pystuff/100_days/day_34/true.png')
        false_img = PhotoImage('Users/finneassensiba/pystuff/100_days/day_34/false.png')
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_click)
        self.false = Button(image=false_img, highlighthickness=0, command=self.false_click)
        self.true.grid(row= 2, column=0)
        self.false.grid(row=2, column=1)
        
        self.score = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Quiz Over')
            self.canvas.config(bg='white')
            self.true.config(state='disabled')
            self.false.config(state='disabled')
    def true_click(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        
    def false_click(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')