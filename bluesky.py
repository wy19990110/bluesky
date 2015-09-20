import sys

from bluesky.ui import Gui
from bluesky.sim import Simulation, MainLoop

# =============================================================================
# Create gui and simulation objects
# =============================================================================
gui = Gui(sys.argv)
sim = Simulation()


# =============================================================================
# Start the mainloop (and possible other threads)
# =============================================================================
MainLoop(gui, sim)

print 'BlueSky normal end.'
