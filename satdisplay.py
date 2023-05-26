from color_setup import ssd  # Create a display instance
from gui.core.nanogui import refresh
from gui.core.writer import CWriter
from gui.core.colors import *

from gui.widgets.label import Label
import gui.fonts.freesans20 as freesans20
import gui.fonts.font6 as font6
import gui.fonts.font10 as font10

# Initial display setup for nano-gui


refresh(ssd)  # Initialise and clear display.
CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
titlewri = CWriter(ssd, freesans20, GREEN, BLACK, verbose=False)
titlewri.set_clip(True, True, False)

elevwri = CWriter(ssd, font6, GREEN, BLACK, verbose=False)
elevwri.set_clip(True, True, False)

satwri = CWriter(ssd, font10, GREEN, BLACK, verbose=False)
satwri.set_clip(True, True, False)
