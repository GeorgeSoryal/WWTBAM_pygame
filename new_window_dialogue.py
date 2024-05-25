import tkinter as tk
from tkinter import ttk
from abc import abstractmethod
from random import randint, choice, choices
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image

from PhonedFriend import PhonedFriend
from GameCollections import AnswersEnum
import constants


class NewWindowDialogue(tk.Tk):
    def __init__(self, title: str):
        super().__init__()
        self.open = False
        self.title(title)
        self.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.del_friend_window)
        self.resizable(False, False)

    def del_friend_window(self):
        self.open = False
        self.destroy()

    @abstractmethod
    def activate(self, correct_answer: AnswersEnum):
        pass


class AskAudience(NewWindowDialogue):
    def __init__(self, correct_answer: AnswersEnum):
        super().__init__(constants.ask_audience_title)
        self.correct_answer: AnswersEnum = correct_answer
        self.geometry('500x450')

    def activate(self, correct_answer: AnswersEnum):
        self.correct_answer = correct_answer.convert_to_char()
        self.plot_audience(self.correct_answer)
        self.deiconify()
        self.open = True

    def plot_audience(self, answer_letter: str):
        # https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/ :+1:
        # https://stackoverflow.com/questions/31549613/displaying-a-matplotlib-bar-chart-in-tkinter :+1:
        fig = Figure(figsize=(5, 5), dpi=100)
        answer_index = AnswersEnum.convert_from_char(answer_letter).convert_to_int()

        # adding the subplot
        plot1: 'Figure' = fig.add_subplot(111, xlabel='Choices', ylabel='Number of audience members')

        plot1.set_title(f'Out of {constants.number_of_audience_members} audience members, people \n'
                        f'believed the answer was:')
        audience_answers = self.generate_answers_frequencies(answer_index, randint(35, 65))
        plot1.bar(('A', 'B', 'C', 'D'), audience_answers, 0.5)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

    @staticmethod
    def generate_answers_frequencies(correct_answer_index: int, prb_correct_answer: int):
        answers = [0, 0, 0, 0]
        set_of_incorrect_indices = {0, 1, 2, 3} ^ {correct_answer_index}
        for i in range(constants.number_of_audience_members):
            if randint(0, 100) < prb_correct_answer:
                answers[correct_answer_index] += 1
            else:
                # random incorrect choice gets chosen and added its frequency is added to by one
                answers[choice(tuple(set_of_incorrect_indices))] += 1
        return answers


class PhoneFriend(NewWindowDialogue):
    def __init__(self, correct_answer: str):
        super().__init__(constants.phone_friend_title)
        self.geometry('450x150')
        self.correct_answer: str = correct_answer
        self.img = None
        # TODO: Instead of letter make it the actual answer
        self.people_list = [
            PhonedFriend('Santa', 'Ho! Ho! Ho! The answer must be ', '#F5A2A2', '#F53232', 99,
            ImageTk.PhotoImage(Image.open('Assets/santa.png'))),
            PhonedFriend('Mom', 'If I had to guess I think it would be ', '#FAE879', '#f9f8d9', 75,
                         ImageTk.PhotoImage(Image.open('Assets/mom.png'))),
            PhonedFriend('Dad', 'Well I suppose the answer would be ', '#33A19D', '#13B1FD', 70,
                         ImageTk.PhotoImage(Image.open('Assets/dad.png')))]

        # 18 columns, 450 px => 25px per col
        self.columnconfigure(0, weight=1)  # Padding
        self.columnconfigure(1, weight=8)  # Text
        self.columnconfigure(2, weight=2)  # Padding
        self.columnconfigure(3, weight=1)  # Image
        self.columnconfigure(4, weight=4)  # Image, Caption
        self.columnconfigure(5, weight=1)  # Image
        self.columnconfigure(5, weight=1)  # Padding
        # 30 rows, out of 150 px => 5px per row
        self.rowconfigure(0, weight=6)   # Padding
        self.rowconfigure(1, weight=10)  # Text, Image
        self.rowconfigure(2, weight=1)   # Caption, Image
        self.rowconfigure(3, weight=7)   # Caption
        self.rowconfigure(4, weight=6)   # Padding

    def activate(self, correct_answer: str):
        self.correct_answer = correct_answer
        self.phone_friend()
        self.deiconify()
        self.open = True

    def phone_friend(self):
        chosen_person = choices(self.people_list, k=1, weights=(5, 45, 50))[0]

        s = ttk.Style()
        s.theme_use('clam')
        s.configure('s.TLabel', font=('Verdana', 14), foreground=chosen_person.color_theme2)
        m = ttk.Style()
        m.theme_use('clam')
        m.configure('s.TFrame')
        self['bg'] = '#' + ('23' * 3)

        text_frm = ttk.Label(self, text=chosen_person.dialogue + self.correct_answer,
                             style='s.TLabel', justify='left', wraplength=300)
        text_frm.grid(row=1, column=1, rowspan=2, sticky='nesw')

        panel = tk.Label(self, image=chosen_person.img, relief='flat', highlightbackground='#' + ('A1' * 3),
                         highlightthickness=2, bg=chosen_person.color_theme1, border=0)
        panel.grid(row=1, column=3, columnspan=3, rowspan=2, sticky='nesw')

        caption_frm = ttk.Label(self, text=chosen_person.name, style='s.TLabel', anchor='center', )
        caption_frm.grid(row=2, column=4, rowspan=2, sticky='nesw')

    @staticmethod
    def choose_answer(correct_index: int, prb_correct: int):
        if randint(0, 100) < prb_correct:
            return correct_index
        else:
            return choice(tuple({0, 1, 2, 3} ^ {correct_index}))
