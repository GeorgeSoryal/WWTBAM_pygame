""" No particular copyright or license.
    Just a Who Wants To Be A Millionaire Game. """
import time
from sys import exit
import pygame as pg
import pygame.image

import windows_foreground_handler as windows_handler

from new_window_dialogue import AskAudience, PhoneFriend
from LevelRenderer import LevelRenderer
from TitleScreen import TitleScreen
from Icons import Icons
from Questions import Questions
from EndGame import EndGame
from GameCollections import AnswersEnum
import constants

pg.init()

screen = pg.display.set_mode((850, 450))
screen_rect = screen.get_rect()

pg.display.set_caption("Who wants to be a Millionaire!")
window_icon = pg.image.load("Assets/icon.png").convert_alpha()
pg.display.set_icon(window_icon)
clock = pg.time.Clock()

BG = pg.image.load("Assets/bg.jpg").convert_alpha()

screen.blit(BG, (0, 0))
questions_list_surf = pg.image.load('Assets/question_set.png')

started = False
is_title_cleared = False
is_levels_initialized = False
is_pygame_window_focused = False

font = pg.font.Font(constants.std_font, constants.questions_font_size)
largest_font = pg.font.Font(constants.std_font, constants.title_font_size)
larger_font = pg.font.Font(constants.std_font, constants.win_font_size)
small_font = pg.font.Font(constants.std_font, constants.caption_font_size)
questions = Questions(constants.questions_list)
end_game = EndGame(screen, screen_rect, BG, questions, font, larger_font, small_font)
windows = windows_handler.WindowsForegroundHandler()

title_screen = TitleScreen(pg, largest_font, small_font)
icons = Icons(pg, screen)
renderer = LevelRenderer(questions, font, screen_rect, icons.initialize_icons,
                         LevelRenderer.split_question_list_surfs(questions_list_surf))  # NOQA
friend_dialogue = PhoneFriend(questions.answer)
ask_audience = AskAudience(AnswersEnum.convert_from_char(questions.answer_letter))


def reset():
    constants.reset_question_list()
    global started, is_title_cleared, is_levels_initialized, is_pygame_window_focused, font, largest_font, larger_font,\
        small_font, questions, end_game, windows, title_screen, icons, renderer, friend_dialogue, ask_audience
    started = False
    is_title_cleared = False
    is_levels_initialized = False
    is_pygame_window_focused = False
    font = pg.font.Font(constants.std_font, constants.questions_font_size)
    largest_font = pg.font.Font(constants.std_font, constants.title_font_size)
    larger_font = pg.font.Font(constants.std_font, constants.win_font_size)
    small_font = pg.font.Font(constants.std_font, constants.caption_font_size)
    questions = Questions(constants.questions_list)
    end_game = EndGame(screen, screen_rect, BG, questions, font, larger_font, small_font)
    windows = windows_handler.WindowsForegroundHandler()

    title_screen = TitleScreen(pg, largest_font, small_font)
    icons = Icons(pg, screen)
    renderer = LevelRenderer(questions, font, screen_rect, icons.initialize_icons,
                             LevelRenderer.split_question_list_surfs(questions_list_surf))  # NOQA
    friend_dialogue.reset(questions.answer)
    ask_audience.reset(AnswersEnum.convert_from_char(questions.answer_letter))


def clicked(rect, *shown_rects):
    if shown_rects:
        return rect.collidepoint(pg.mouse.get_pos()) and (rect in shown_rects[0])
    return rect.collidepoint(pg.mouse.get_pos())


def next_step(answer_enum: AnswersEnum, end_game_handler: 'EndGame'):
    renderer.handle_mouse_click(answer_enum, screen, BG, end_game_handler, pg)
    if friend_dialogue.open:
        friend_dialogue.del_window()
    if ask_audience.open:
        ask_audience.del_window()


start_time = time.time()
while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if not started:
            if not is_pygame_window_focused:
                windows.front(constants.pg_window_title)
            is_pygame_window_focused = True
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            if event.type == title_screen.add_period_event:
                title_screen.num_of_periods += 1

            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                started = True

        elif started:
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                if renderer.game_over and end_game.is_end_screen_showing:
                    if clicked(end_game.reset_rect):
                        reset()
                        continue
                    if clicked(end_game.screenshot_rect):
                        # https://stackoverflow.com/questions/6087484/how-to-capture-pygame-screen :+1:
                        pygame.image.save(screen, f"screenshots/{time.time()}.jpeg")
                        screenshot_text = font.render(f"Screenshot saved as {time.time()}.jpeg in screenshots folder",
                                                      False, "cyan")
                        screenshot_rect = screenshot_text.get_rect(center=(screen_rect.centerx,
                                                                           constants.screenshot_top_margin))
                        screen.blit(screenshot_text, screenshot_rect)

                    else:
                        exit()

                # Only KEYDOWN has .key attribute
                if event.type == pg.KEYDOWN and event.key == pg.K_F2:
                    renderer.handle_mouse_click(AnswersEnum.convert_from_char(questions.answer_letter), screen, BG,
                                                end_game, pg)

        # To handle clicking on the buttons
        if is_title_cleared:  # if title cleared -> buttons, answer choices loaded on screen

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # if LMB click

                if (clicked(icons.ask_the_audience_rect) and not icons.has_clicked_ask_the_audience and
                        time.time() - start_time > 1) and not end_game.is_in_between_questions:
                    icons.gray_out_ask_the_audience_button()
                    ask_audience.activate(AnswersEnum.convert_from_char(questions.answer_letter))
                    windows.front(constants.phone_friend_title)
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                elif clicked(icons.ask_the_audience_rect) and not time.time() - start_time > 2 and not \
                        end_game.is_in_between_questions:
                    pg.mouse.set_cursor(*pg.cursors.load_xbm("Assets/wait.xbm", "Assets/wait.xbm"))

                if (clicked(icons.phone_a_friend_rect) and not icons.has_clicked_phone_a_friend and
                        time.time() - start_time > 2) and not end_game.is_in_between_questions:
                    icons.gray_out_phone_a_friend()
                    friend_dialogue.activate(questions.answer)
                    windows.front(constants.phone_friend_title)
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                elif clicked(icons.phone_a_friend_rect) and not time.time() - start_time > 2 and not \
                        end_game.is_in_between_questions:
                    pg.mouse.set_cursor(*pg.cursors.load_xbm("Assets/wait.xbm", "Assets/wait.xbm"))

                if clicked(icons.fiftyfifty_rect) and not icons.has_clicked_fiftyfifty and not \
                        end_game.is_in_between_questions:
                    icons.gray_out_fiftyfifty()
                    renderer.fiftyfifty_questions(screen, BG)

                if clicked(renderer.A_rect, renderer.rects_shown) and not end_game.is_in_between_questions:
                    next_step(AnswersEnum.A, end_game)

                if clicked(renderer.B_rect, renderer.rects_shown) and not end_game.is_in_between_questions:
                    next_step(AnswersEnum.B, end_game)

                if clicked(renderer.C_rect, renderer.rects_shown) and not end_game.is_in_between_questions:
                    next_step(AnswersEnum.C, end_game)

                if clicked(renderer.D_rect, renderer.rects_shown) and not end_game.is_in_between_questions:
                    next_step(AnswersEnum.D, end_game)

        if is_levels_initialized and windows_handler.get_front() == constants.pg_window_title:

            # To make cursor into correct button cursor type
            if not end_game.is_in_between_questions and event.type == pg.MOUSEMOTION and (
                    renderer.mouse_on_answer_choice(pg) or icons.mouse_on_icon()):
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)

            if end_game.is_end_screen_showing and event.type == pg.MOUSEMOTION and (
                    end_game.reset_rect.collidepoint(pg.mouse.get_pos()) or end_game.screenshot_rect.collidepoint(pg.mouse.get_pos())):  # NOQA
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)

            if not end_game.is_in_between_questions and event.type == pg.MOUSEMOTION and not (
                    renderer.mouse_on_answer_choice(pg) or icons.mouse_on_icon()):
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

            if end_game.is_end_screen_showing and event.type == pg.MOUSEMOTION and not (
                    end_game.reset_rect.collidepoint(pg.mouse.get_pos()) or end_game.screenshot_rect.collidepoint(pg.mouse.get_pos())):  # NOQA
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    # end of event loop

    if not started:  # show title screen while the user hasn't opened the game yet [clicked a key]
        title_screen.title_screen(screen, screen_rect, BG)

    elif not is_title_cleared:  # else if they have clicked a key and the title screen
        # hasn't been cleared yet, clear the title screen, this runs once
        title_screen.title_clear(screen, BG)
        is_title_cleared = True

    elif not is_levels_initialized:  # if the levels haven't been shown yet and the title is cleared, show the level,
        # and set the level boolean to true so that it will be rendered in the event loop based on inputs now, runs once
        is_levels_initialized = True
        icons.initialize_icons()
        renderer.render(screen, BG)

    clock.tick(60)
    pg.display.update()
    if icons.has_clicked_phone_a_friend:
        friend_dialogue.update()
    if icons.has_clicked_ask_the_audience:
        ask_audience.update()
