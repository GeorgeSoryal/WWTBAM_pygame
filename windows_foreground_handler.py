import win32gui


def get_front() -> str:
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


class WindowsForegroundHandler:
    # https://stackoverflow.com/questions/63395415/how-to-change-focus-to-pygame-window :+1:
    def __init__(self):
        self.windows = []
        win32gui.EnumWindows(self.windowEnumerationHandler, self.windows)

    def windowEnumerationHandler(self, hwnd, windows):  # NOQA
        windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def front(self, win_name):
        for i in self.windows:
            if i[1] == win_name:
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break
