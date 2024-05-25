from GameCollections import Money


class Questions:
    def __init__(self, question_dict: list[dict[str, str]]):
        self.__question_dict = question_dict
        self.num = 0
        self.question = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.answer_letter = None
        self.fill_dicts()

    def fill_dicts(self):
        self.question = self.__question_dict[self.num]['question']
        self.A = 'A)\t' + self.__question_dict[self.num]['A']
        self.B = 'B)\t' + self.__question_dict[self.num]['B']
        self.C = 'C)\t' + self.__question_dict[self.num]['C']
        self.D = 'D)\t' + self.__question_dict[self.num]['D']
        self.answer_letter = self.__question_dict[self.num]['answer']

    @property
    def answer(self):
        return self.__question_dict[self.num][self.answer_letter]

    # https://wwbm.com/rules
    def calculate_earned(self) -> Money:
        match self.num:
            case 0:
                return Money(0)
            case 1:
                return Money(100)
            case 2:
                return Money(200)
            case 3:
                return Money(300)
            case 4:
                return Money(400)
            case 5:
                return Money(1_000, 1_000)
            case 6:
                return Money(2_000, 1_000)
            case 7:
                return Money(4_000, 1_000)
            case 8:
                return Money(8_000, 1_000)
            case 9:
                return Money(16_000, 1_000)
            case 10:
                return Money(32_000, 32_000)
            case 11:
                return Money(64_000, 32_000)
            case 12:
                return Money(125_000, 32_000)
            case 13:
                return Money(250_000, 32_000)
            case 14:
                return Money(500_000, 32_000)
            case 15:
                return Money(1_000_000, 1_000_000)
            case _:
                raise ValueError("Question Number is not between 1 and 15")
