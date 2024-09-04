import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
MAIN_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.q_canvas = tk.Canvas(bg="#fff", width=300, height=250)
        self.question_text = self.q_canvas.create_text(150, 125, text="", width=280,
                                                       font=MAIN_FONT, fill=THEME_COLOR)
        self.q_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = tk.Label(text="Score: 0", fg="#fff", font=("Arial", 12, "bold"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")
        self.btn_true = tk.Button(image=true_img, width=100, height=97, highlightthickness=0, command=self.true_pressed)
        self.btn_false = tk.Button(image=false_img, width=100, height=97, highlightthickness=0,
                                   command=self.false_pressed)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.q_canvas.config(bg="#fff")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        q_text = self.quiz_brain.next_question()
        self.q_canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))
        # self.get_next_question()

    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.q_canvas.config(bg="green")
        else:
            self.q_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    # def display_score(self, score):
    #     self.score_label.te
