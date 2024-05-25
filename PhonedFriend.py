from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PIL.ImageTk import PhotoImage


@dataclass
class PhonedFriend:
    """
    name: str \n
    dialogue: str \n
    color_theme1: str - For background, with theme2, forms a palette \n
    color_theme2: str - Should probably be more saturated \n
    prb_correct: int \n
    img: 'PhotoImage' - ImageTk.PhotoImage(Image.open(str_path)) \n
    """
    name: str
    dialogue: str
    color_theme1: str
    color_theme2: str
    prb_correct: int
    img: 'PhotoImage'
