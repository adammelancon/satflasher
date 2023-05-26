from color_setup import ssd  # Create a display instance
from gui.core.nanogui import refresh
from gui.core.writer import CWriter
from gui.core.colors import *

from gui.widgets.label import Label
import gui.fonts.freesans20 as freesans20
import gui.fonts.font6 as font6
import gui.fonts.font10 as font10




refresh(ssd)  # Initialise and clear display.
CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
titlewri = CWriter(ssd, freesans20, GREEN, BLACK, verbose=False)
titlewri.set_clip(True, True, False)

elevwri = CWriter(ssd, font6, GREEN, BLACK, verbose=False)
elevwri.set_clip(True, True, False)

satwri = CWriter(ssd, font10, GREEN, BLACK, verbose=False)
satwri.set_clip(True, True, False)

# # End of boilerplate code. This is our application:
# Label(titlewri, 1, 20, 'Tracking:', invert=True)
# Label(satwri, 26, 0, sat)
# Label(elevwri, 45, 0, f'-Elev: 22.2')
# refresh(ssd)