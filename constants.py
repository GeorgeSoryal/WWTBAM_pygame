"""Mostly margins, padding, filepaths, and also the questions list."""
import JsonDataHandler

questions_list = JsonDataHandler.populate_question_list()


def reset_question_list():
    global questions_list
    questions_list = JsonDataHandler.populate_question_list()


std_font = "Assets/Korinna-Regular.otf"
grayed_ask_audience = "Assets/grayed_out_ask_the_audience.png"
grayed_phone_friend = "Assets/grayed_out_phone_a_friend.png"
grayed_fiftyfifty = "Assets/grayed_out_fiftyfifty.png"
ask_audience = "Assets/ask_the_audience.png"
phone_friend = "Assets/phone_a_friend.png"
fiftyfifty = "Assets/fiftyfifty.png"
reset = "Assets/reset.png"
screenshot_button = "Assets/screenshot_button.png"
key_message = "Press any key to exit or the reset button to try again."
pg_window_title = "Who wants to be a Millionaire!"
phone_friend_title = "Phone a friend"
ask_audience_title = "Audience says..."
number_of_audience_members = 250
left_margin = 15
top_margin = 10
title_font_size = 50
win_font_size = 40
caption_font_size = 25
questions_font_size = 30
space_between_answers = 12
game_over_center_margin = 35
answer_choices_starting_y = 115
icons_x = 750
icons_starting_y = 50
question_starting_y = 20
starting_question_set_y = 450 - 100
starting_question_set_x = 20
num_of_questions = 15
question_oval_width = 57
oval_space_between = 5
bottom_buttons_margin_x = 50
bottom_buttons_margin_y = 450 - 10
screenshot_top_margin = 5
