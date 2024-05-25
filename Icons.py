import constants
import typing
if typing.TYPE_CHECKING:
    import pygame


class Icons:

    def __init__(self, pg: 'pygame', screen: 'pygame.Surface'):
        self.pg = pg
        self.screen = screen

        self.fiftyfifty_path = constants.fiftyfifty
        self.phone_a_friend_path = constants.phone_friend
        self.ask_the_audience_path = constants.ask_audience

        self.__fiftyfifty_surf = None
        self.fiftyfifty_rect = None
        self.has_clicked_fiftyfifty = False

        self.__phone_a_friend_surf = None
        self.phone_a_friend_rect = None
        self.has_clicked_phone_a_friend = False

        self.__ask_the_audience_surf = None
        self.ask_the_audience_rect = None
        self.has_clicked_ask_the_audience = False

    def initialize_icons(self):
        self.__fiftyfifty_surf = self.pg.image.load(self.fiftyfifty_path).convert_alpha()
        self.fiftyfifty_rect = self.screen.blit(self.__fiftyfifty_surf,
                                                (constants.icons_x, constants.icons_starting_y))

        self.__phone_a_friend_surf = self.pg.image.load(self.phone_a_friend_path).convert_alpha()
        self.phone_a_friend_rect = self.screen.blit(self.__phone_a_friend_surf,
                                                    (constants.icons_x, constants.icons_starting_y + 100))

        self.__ask_the_audience_surf = self.pg.image.load(self.ask_the_audience_path).convert_alpha()
        self.ask_the_audience_rect = self.screen.blit(self.__ask_the_audience_surf,
                                                      (constants.icons_x, constants.icons_starting_y + 200))

    def mouse_on_icon(self):
        return self.ask_the_audience_rect.collidepoint(self.pg.mouse.get_pos()) or \
            self.fiftyfifty_rect.collidepoint(self.pg.mouse.get_pos()) or \
            self.phone_a_friend_rect.collidepoint(self.pg.mouse.get_pos())

    def gray_out_ask_the_audience_button(self):
        self.ask_the_audience_path = constants.grayed_ask_audience
        self.has_clicked_ask_the_audience = True
        self.__ask_the_audience_surf = self.pg.image.load(constants.grayed_ask_audience).convert_alpha()
        self.screen.blit(self.__ask_the_audience_surf, self.ask_the_audience_rect)

    def gray_out_phone_a_friend(self):
        self.phone_a_friend_path = constants.grayed_phone_friend
        self.has_clicked_phone_a_friend = True
        self.__phone_a_friend_surf = self.pg.image.load(constants.grayed_phone_friend).convert_alpha()
        self.screen.blit(self.__phone_a_friend_surf, self.phone_a_friend_rect)

    def gray_out_fiftyfifty(self):
        self.fiftyfifty_path = constants.grayed_fiftyfifty
        self.has_clicked_fiftyfifty = True
        self.__fiftyfifty_surf = self.pg.image.load(constants.grayed_fiftyfifty).convert_alpha()
        self.screen.blit(self.__fiftyfifty_surf, self.fiftyfifty_rect)
