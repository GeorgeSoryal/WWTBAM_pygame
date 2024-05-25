from enum import Enum
from typing import NamedTuple


class AnswersEnum(Enum):
    """To bridge the gap between answer strings and rectangles."""
    A = 1
    B = 2
    C = 3
    D = 4

    def convert_to_char(self) -> str:
        match self:
            case AnswersEnum.A:
                return 'A'
            case AnswersEnum.B:
                return 'B'
            case AnswersEnum.C:
                return 'C'
            case AnswersEnum.D:
                return 'D'
            case _:
                raise ValueError("Did not input an answer choice rect.")

    def convert_to_int(self) -> int:
        match self:
            case AnswersEnum.A:
                return 0
            case AnswersEnum.B:
                return 1
            case AnswersEnum.C:
                return 2
            case AnswersEnum.D:
                return 3
            case _:
                raise ValueError("Did not input an answer choice rect.")

    @classmethod
    def convert_from_char(cls, string_answer: str) -> 'AnswersEnum':
        # turn self.answer to a new answer_rect
        match string_answer:
            case 'A':
                return AnswersEnum.A
            case 'B':
                return AnswersEnum.B
            case 'C':
                return AnswersEnum.C
            case 'D':
                return AnswersEnum.D
            case _:
                raise ValueError("Did not input an answer choice rect.")


class Money(NamedTuple):
    earned: int = 0
    secured: int = 0
