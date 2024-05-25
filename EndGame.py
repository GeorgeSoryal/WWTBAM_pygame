from threading import Timer
from typing import TYPE_CHECKING

import constants

if TYPE_CHECKING:
    import pygame
    import Questions


class EndGame:
    # TODO: use dependency injection for the icons at the bottom
    def __init__(self, screen, screen_rect, BG, questions: 'Questions', font: 'pygame.font.Font',
                 win_font: 'pygame.font.Font', key_font: 'pygame.font.Font'):
        self._questions = questions
        self._screen = screen
        self._screen_rect = screen_rect
        self._BG = BG
        self._font = font
        self._win_font = win_font
        self._key_font = key_font
        self.is_in_between_questions = False
        self.is_end_screen_showing = False
        self.reset_rect = None
        self.screenshot_rect = None

    def show_correct_answer_screen(self, next_question_handler, pygame_instance: 'pygame'):
        self.is_in_between_questions = True
        pygame_instance.mouse.set_cursor(pygame_instance.SYSTEM_CURSOR_ARROW)
        right_answer = self._font.render(f"Correct, moving on to question #{self._questions.num + 2}", True, "green")
        right_answer_rect = right_answer.get_rect(center=(self._screen_rect.centerx, self._screen_rect.centery))
        self._screen.blit(self._BG, (0, 0))
        self._screen.blit(self._BG.subsurface(right_answer_rect), right_answer_rect)
        self._screen.blit(right_answer, right_answer_rect)
        Timer(1.0, next_question_handler, [self._screen, self._BG, self]).start()

    def show_win_screen(self, pygame_instance: 'pygame'):

        reset_button_surf: 'pygame.Surface' = pygame_instance.image.load(constants.reset).convert_alpha()
        self.reset_rect = reset_button_surf.get_rect(midbottom=(self._screen_rect.centerx +
                                                 constants.bottom_buttons_margin_x, constants.bottom_buttons_margin_y))

        screenshot_button_surf: 'pygame.Surface' = pygame_instance.image.load(constants.screenshot_button).convert_alpha()  # NOQA
        self.screenshot_rect = screenshot_button_surf.get_rect(midbottom=(self._screen_rect.centerx -
                                                 constants.bottom_buttons_margin_x, constants.bottom_buttons_margin_y))
        self.is_in_between_questions = True
        self.is_end_screen_showing = True
        pygame_instance.mouse.set_cursor(pygame_instance.SYSTEM_CURSOR_ARROW)
        congrats_surf = self._win_font.render(f"Congrats! You won the game and $1,000,000!", True, "#168749")
        congrats_rect = congrats_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.centery))
        self._screen.blit(self._BG, (0, 0))
        self._screen.blit(self._BG.subsurface(congrats_rect), congrats_rect)
        self._screen.blit(congrats_surf, congrats_rect)
        press_key_surf: 'pygame.Surface' = self._font.render(constants.key_message, True, "cyan")
        press_key_rect = press_key_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.
                                                         centery + constants.game_over_center_margin))
        self._screen.blit(reset_button_surf, self.reset_rect)
        self._screen.blit(screenshot_button_surf, self.screenshot_rect)
        self._screen.blit(press_key_surf, press_key_rect)

    def show_wrong_answer_screen(self, pygame_instance: 'pygame'):
        self.is_in_between_questions = True
        pygame_instance.mouse.set_cursor(pygame_instance.SYSTEM_CURSOR_ARROW)
        wrong_answer = self._font.render(f"Wrong! The correct answer was {self._questions.answer_letter}: "
                                         f"{self._questions.answer}", True, "red")
        wrong_answer_rect = wrong_answer.get_rect(center=(self._screen_rect.centerx, self._screen_rect.centery))
        self._screen.blit(self._BG, (0, 0))
        self._screen.blit(self._BG.subsurface(wrong_answer_rect), wrong_answer_rect)
        self._screen.blit(wrong_answer, wrong_answer_rect)
        Timer(2.0, self.show_end_screen, [pygame_instance]).start()

    def show_end_screen(self, pygame_instance: 'pygame'):

        reset_button_surf: 'pygame.Surface' = pygame_instance.image.load(constants.reset).convert_alpha()
        self.reset_rect = reset_button_surf.get_rect(midbottom=(self._screen_rect.centerx +
                                                 constants.bottom_buttons_margin_x, constants.bottom_buttons_margin_y))

        screenshot_button_surf: 'pygame.Surface' = pygame_instance.image.load(constants.screenshot_button).convert_alpha()  # NOQA
        self.screenshot_rect = screenshot_button_surf.get_rect(midbottom=(self._screen_rect.centerx -
                                                 constants.bottom_buttons_margin_x, constants.bottom_buttons_margin_y))
        self.is_in_between_questions = True
        self.is_end_screen_showing = True
        self._screen.blit(self._BG, (0, 0))
        money = self._questions.calculate_earned()
        money_earned_surf: 'pygame.Surface' = self._font.render(f"Game over! You earned a total of "
                                                                f"${money.earned}.", True, "cyan")
        money_earned_rect = money_earned_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.centery -
                                                               constants.game_over_center_margin))
        money_secured_surf: 'pygame.Surface' = self._font.render(f"You secured (will walk away with) "
                                                                 f"a total of ${money.secured}.", True, "cyan")
        money_secured_rect = money_secured_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.centery))
        questions_answered_surf: 'pygame.Surface' = self._font.render(f"You answered a total of "
                                                        f"{self._questions.num} questions correctly.", True, "cyan")
        press_key_surf: 'pygame.Surface' = self._font.render(constants.key_message, True, "cyan")
        questions_answered_rect = questions_answered_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.
                                                                           centery + constants.game_over_center_margin))
        self._screen.blit(money_earned_surf, money_earned_rect)
        self._screen.blit(money_secured_surf, money_secured_rect)
        self._screen.blit(reset_button_surf, self.reset_rect)
        self._screen.blit(screenshot_button_surf, self.screenshot_rect)
        self._screen.blit(questions_answered_surf, questions_answered_rect)
        self._screen.blit(press_key_surf, press_key_surf.get_rect(center=(self._screen_rect.centerx, self._screen_rect.
                                                                        centery + constants.game_over_center_margin*2)))
