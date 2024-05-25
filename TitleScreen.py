import constants


class TitleScreen:
    def __init__(self, pygame_instance, title_font, caption_font):
        self.num_of_periods = 0
        self.add_period_event = pygame_instance.USEREVENT + 1
        pygame_instance.time.set_timer(self.add_period_event, 1050, 6)

        self.title_font = title_font
        self.title_surf = None
        self.title_rect = None

        self.caption_font = caption_font
        self.caption_font_surf = None
        self.caption_font_rect = None

    def title_screen(self, screen, screen_rect, BG):
        screen.blit(BG, (0, 0))
        self.title_surf = self.title_font.render(constants.pg_window_title, True, "White")
        self.title_rect = self.title_surf.get_rect(center=screen_rect.center)

        self.caption_font_surf = self.caption_font.render(f"Press any key to start{self.num_of_periods * '.'}", True,
                                                          "White")
        self.caption_font_rect = self.caption_font_surf.get_rect(center=(screen_rect.centerx - 10,
                                                                         (screen_rect.centery + 70)))
        screen.blit(self.title_surf, self.title_rect)
        screen.blit(self.caption_font_surf, self.caption_font_rect)

    def title_clear(self, screen, BG):
        # for added periods
        self.caption_font_rect.width += 100
        start_subsurface = BG.subsurface(self.caption_font_rect)
        title_subsurface = BG.subsurface(self.title_rect)

        screen.blit(start_subsurface, self.caption_font_rect)
        screen.blit(title_subsurface, self.title_rect)
