import graphics
from graphics import *


# In class char, the variable name is character's name.
# Name is the character's name, imgpath is the filepath for their images, speechboxcolor is their "image color" (eg rin is yellow), textcolor is the color for text that you can see on top of the imagecolor.
class char:
    def __init__(self, name, imgpath, imgcolor, textcolor):
        self.name = name
        self.imgpath = imgpath
        self.speechboxcolor = imgcolor
        self.textcolor = textcolor


#Characters:
Rin = char("Rin", "rin1.png", "speechbox.png", "black")
char01 = char("uname", "placeholder.png", "white", "black")


#Functions:
def nextbutton(window):
    clickpos = window.getMouse()
    clickposx = float(str(clickpos)[6:11])
    clickposy = float(str(clickpos)[13:18])
    if (1249 < clickposx < 1336) and (781 < clickposy < 817):
        return "next"
    else:
        nextbutton(window)
def speech(character, message, window):
    spktxt = Text(Point(720, 700), message)
    spktxt.setSize(20)
    charname = character.name
    namedraw = Text(Point(720,623), charname)
    namedraw.setSize(36)
    namedraw.setFace("courier")
    spktxt.draw(window)
    namedraw.draw(window)
    nextbutton(window)
    namedraw.undraw()
    spktxt.undraw()
def userentry(prompt, extratext, window):
    uentry = Entry(Point(720, 700), 60)
    promptdraw = Text(Point(720, 623), prompt)
    promptdraw.setSize(36)
    promptdraw.setFace("courier")
    extratext = Text(Point(720, 670), extratext)
    extratext.setSize(20)
    extratext.draw(window)
    promptdraw.draw(window)
    uentry.draw(window)
    nextbutton(window)
    textentered = uentry.getText()
    promptdraw.undraw()
    uentry.undraw()
    extratext.undraw()
    return textentered
def setemotion(emotion, window, img, speechbox, clicktocontinue):
    imgret = Image(Point(720,427), str(emotion) + ".png")
    speechbox.undraw()
    img.undraw()
    clicktocontinue.undraw()
    imgret.draw(window)
    speechbox.draw(window)
    clicktocontinue.draw(window)