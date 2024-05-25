from random import randint
import typing

from GameCollections import AnswersEnum
from Questions import Questions

if typing.TYPE_CHECKING:
    import pygame
    import EndGame

import constants


class LevelRenderer:
    # TODO: split this class into question renderer and question list/set renderer
    def __init__(self, question: Questions, font: 'pygame.font', screen_rect, icons_initializer: 'typing.Callable',
                 questions_list: list[tuple['pygame.Surface', 'pygame.Surface']]):
        self.questions = question
        self._questions_list = questions_list
        self._screen_rect = screen_rect
        self._font = font
        self._icons_initializer = icons_initializer

        self.questions_shown: list[tuple['pygame.Rect', AnswersEnum]] = []
        self.rects_shown = []

        self.game_over = False
        self.A_rect = None
        self.B_rect = None
        self.C_rect = None
        self.D_rect = None

    # "public" methods
    def handle_mouse_click(self, answer_clicked: 'AnswersEnum', screen, BG, end_game_handler: 'EndGame', pygame_instance):  # NOQA
        if AnswersEnum.convert_from_char(self.questions.answer_letter) == answer_clicked:  # Answer correct
            if self.questions.num == 14:
                end_game_handler.show_win_screen(pygame_instance)
                self.game_over = True
            else:  # Correct answer, but not the last question
                end_game_handler.show_correct_answer_screen(self._next_question, pygame_instance)
        else:
            self.game_over = True
            end_game_handler.show_wrong_answer_screen(pygame_instance)

    def fiftyfifty_questions(self, screen, bg: 'pygame.Surface'):
        num_of_questions = 4
        self.questions_shown = list(zip(self.rects_shown, [AnswersEnum.A, AnswersEnum.B, AnswersEnum.C, AnswersEnum.D]))
        while num_of_questions > 2:
            for i, question in enumerate(self.questions_shown):
                if randint(0, 1) == 1 and AnswersEnum.convert_from_char(self.questions.answer_letter) != question[1]:
                    screen.blit(bg.subsurface(question[0]), question[0])
                    self.questions_shown.pop(i)
                    num_of_questions -= 1
        self.rects_shown = [i[0] for i in self.questions_shown]

    def render(self, screen, BG):
        question_offset = constants.top_margin
        answers_offset = constants.top_margin
        lines_of_questions = self._calculate_text_wrapping(self.questions.question,
                                                           constants.icons_x - constants.left_margin, self._font)
        lines_of_answers = self._calculate_text_wrapping(self.questions.A, constants.icons_x - constants.left_margin,
                                                         self._font)
        lines_of_answers += self._calculate_text_wrapping(self.questions.B, constants.icons_x - constants.left_margin,
                                                          self._font)
        lines_of_answers += self._calculate_text_wrapping(self.questions.C, constants.icons_x - constants.left_margin,
                                                          self._font)
        lines_of_answers += self._calculate_text_wrapping(self.questions.D, constants.icons_x - constants.left_margin,
                                                          self._font)
        font_surf_list = []
        font_rect_list = []

        # clear surface under question
        for i, line in enumerate(lines_of_questions):
            font_surf = self._font.render(line, True, "White")
            font_rect = font_surf.get_rect(topleft=(constants.left_margin, question_offset))

            _, height = self._font.size(line)
            question_offset += height

            font_surf_list.append(font_surf)
            font_rect_list.append(font_rect)
            screen.blit(BG.subsurface(font_rect), font_rect)

        # clear surface under answers
        for _, choice in enumerate(lines_of_answers):
            font_surf = self._font.render(choice, True, "White")
            font_rect = font_surf.get_rect(topleft=(constants.left_margin, constants.answer_choices_starting_y +
                                                    answers_offset))

            _, height = self._font.size(choice)
            answers_offset += height + constants.space_between_answers

            font_surf_list.append(font_surf)
            font_rect_list.append(font_rect)
            screen.blit(BG.subsurface(font_rect), font_rect)

        # now display on screen
        self.A_rect = font_rect_list[-4]
        self.B_rect = font_rect_list[-3]
        self.C_rect = font_rect_list[-2]
        self.D_rect = font_rect_list[-1]
        self.questions.fill_dicts()
        self.rects_shown = [self.A_rect, self.B_rect, self.C_rect, self.D_rect]
        for i, line in enumerate(font_surf_list):
            screen.blit(line, font_rect_list[i])

        self._display_question_set(screen)

    def mouse_on_answer_choice(self, pygame_instance: 'pygame'):
        for rect in self.rects_shown:
            if rect.collidepoint(pygame_instance.mouse.get_pos()):
                return True

    @staticmethod
    def split_question_list_surfs(surf: 'pygame.Surface') -> list[tuple['pygame.Surface', 'pygame.Surface']]:
        final_list = []
        x = 0
        for i in range(constants.num_of_questions - 1):
            final_list.append((surf.subsurface((x, 0, constants.question_oval_width, 100)),
                               surf.subsurface((x, 103, constants.question_oval_width, 97))))
            x += constants.question_oval_width
        final_list.append((surf.subsurface((x, 0, constants.question_oval_width - constants.oval_space_between, 100)),
                           surf.subsurface((x, 102, constants.question_oval_width - constants.oval_space_between, 98))))

        return final_list

    # private methods
    @staticmethod
    def _calculate_text_wrapping(text: str, allowed_width: int, font: 'pygame.font.Font') -> list:
        words = text.split(' ')
        blocks_of_text: list = []

        # https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font :+1:
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            row_of_text = []
            while len(words) > 0:
                row_of_text.append(words.pop(0))
                fw, fh = font.size(' '.join(row_of_text + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(row_of_text)
            blocks_of_text.append(line)

        return blocks_of_text

    def _next_question(self, screen, BG, end_game_handler: 'EndGame.EndGame'):
        # reset shown rects so they're clickable
        self.questions.num += 1
        self.questions.fill_dicts()
        screen.blit(BG, (0, 0))
        self._display_question_set(screen)
        self._icons_initializer()
        self.render(screen, BG)
        end_game_handler.is_in_between_questions = False

    def _display_question_set(self, screen: 'pygame.Surface'):
        for i in range(constants.num_of_questions):
            if i < self.questions.num:
                screen.blit(self._questions_list[i][0], (i * constants.question_oval_width,
                                                         constants.starting_question_set_y))
            elif i >= self.questions.num:
                screen.blit(self._questions_list[i][1], (i * constants.question_oval_width,
                                                         constants.starting_question_set_y))
