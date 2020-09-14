import classesdefs
from classesdefs import *
import graphics
from graphics import *

#setup
window = GraphWin("Rin Simulator Beta 0.2", 1440, 855)
rin1 = Image(Point(720,427), "rin/school_uni/vest/neutral.png")
speechbox = Image(Point(720, 427), "speechbox.png")
betawarning = Text(Point(450,5), "Beta ver 0.2.0 - WARNING: BETA IS UNSTABLE AND STILL UNDER DEVELOPMENT, ITS NOT MY FAULT IF IT BREAKS YOUR COMPUTER AND YOU LOSE YOUR VBUCKS OR SOMETHING")
betawarning.setSize(10)
betawarning.setTextColor("red")
rin1.draw(window)
speechbox.draw(window)
betawarning.draw(window)
clicktocontinue = Text(Point(1300, 800), "Next")
clicktocontinue.setSize(30)
clicktocontinue.draw(window)

window.mainloop()