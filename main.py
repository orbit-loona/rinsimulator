import graphics
from graphics import *

#Quick note, i'm centering all text for now bc it makes my life a million times easier,
#but by the time this gets a release version that will have to change.

#Graphics setup:
window = GraphWin("Rin Simulator Beta 0.1", 1440, 855)
rin1 = Image(Point(720,427), "rin1.png")
speechbox = Image(Point(720, 427), "speechbox.png")
betawarning = Text(Point(450,5), "Beta ver 0.1 - WARNING: BETA IS UNSTABLE AND STILL UNDER DEVELOPMENT, ITS NOT MY FAULT IF IT BREAKS YOUR COMPUTER AND YOU LOSE YOUR VBUCKS OR SOMETHING")
betawarning.setSize(10)
betawarning.setTextColor("red")
rinnamedisplay = Text(Point(720,623), "Rin")
rinnamedisplay.setSize(36)
rinnamedisplay.setFace("courier")
uname = "uname"
unamedisplay = Text(Point(720,623), uname)
unamedisplay.setSize(36)
unamedisplay.setFace("courier")
devnotes = Text(Point(1100,200), "devnote")
devnotes.setSize(20)
devnotes.setFill("red")
msgret = Text(Point(720, 700), "Hello Nya~!\n\n")
msgret.setSize(25)

def nextbutton():
    clickpos = window.getMouse()
    clickposx = float(str(clickpos)[6:11])
    clickposy = float(str(clickpos)[13:18])
    if (1249 < clickposx < 1336) and (781 < clickposy < 817):
        return "next"
    else:
        nextbutton()
betawarning.draw(window)

clicktocontinue = Text(Point(1300, 800), "Next")
clicktocontinue.setSize(30)

#startup complete, begin:

rin1.draw(window)
speechbox.draw(window)
rinnamedisplay.draw(window)
sayvar = msgret
sayvar.draw(window)
clicktocontinue.draw(window)
nextbutton()
sayvar.undraw()
clicktocontinue.undraw()
sayvar.setText("A. Hello! (start)\nB. Settings\nC. Info/Credits")
rinnamedisplay.undraw()
rinnamedisplay.setText("Your Response: (menu)")
rinnamedisplay.draw(window)
sayvar.draw(window)
def menusel():
    clickpos = window.getMouse()
    print(clickpos)
    clickposx = float(str(clickpos)[6:11])
    clickposy = float(str(clickpos)[13:18])
    if (804 > clickposx > 633) and (659 < clickposy < 685):
        print("a")
    elif (784 > clickposx > 658) and (713 > clickposy >687):
        bwin = GraphWin("Rin Sim Settings", 500, 500)
        noset = Text(Point(250,250), "There are no settings for this game yet")
        noset.setSize(20)
        noset.draw(bwin)
        menusel()
    elif (799 > clickposx > 638) and (742 > clickposy > 711):
        cwin = GraphWin("Rin Sim Info", 800,800)
        infopage = Image(Point(400,400), "info.png")
        infopage.draw(cwin)
        menusel()
    else:
        menusel()
menusel()
clicktocontinue.draw(window)
#All this under here needs to go inside that if statement I made into a comment.
#Just did it without the if to make it easier as I code. Also this is affeclevel 0.
#What is being said is in comments:
sayvar.undraw()
rinnamedisplay.undraw()
#What's your name?
sayvar.setText("What's your name?\n\n")
rinnamedisplay.setText("Rin")
sayvar.draw(window)
rinnamedisplay.draw(window)
nextbutton()
sayvar.undraw()
rinnamedisplay.undraw()
#Enter your name: (user entry)
rinnamedisplay.setText("Enter your name:")
rinnamedisplay.draw(window)
unameentry = Entry(Point(720, 700), 60)
unameentry.setFill("white")
unameentry.draw(window)
nextbutton()
uname = unameentry.getText()
unameentry.undraw()
rinnamedisplay.undraw()
#Nice to meet ya (uname)! I'm Rin Hoshizora-nya, a high-school idol in a group called (oh fuck python is ASCII)
rinnamedisplay.setText("Rin")
msgret.setText("Nice to meet ya " + uname + "!\nI'm Rin Hoshizora-nya, a high-school idol in a group called μ's!\n")
rinnamedisplay.draw(window)
msgret.draw(window)
nextbutton()
msgret.undraw()
#I like sports, music, and cats! Nya!
msgret.setText("I like sports, music, and cats! Nya!\n\n")
msgret.draw(window)
nextbutton()
msgret.undraw()
#What about you? Nya?
msgret.setText("What about you? Nya?\n\n")
msgret.draw(window)
nextbutton()
msgret.undraw()
rinnamedisplay.undraw()
#I like: (user entry)
rinnamedisplay.setText("Enter what you like: (a few words max, no punctuation)")
rinnamedisplay.draw(window)
userlikesentry = Entry(Point(720, 700), 60)
userlikesentry.setFill("white")
userlikesentry.draw(window)
nextbutton()
userlikes = userlikesentry.getText().lower()
userlikesentry.undraw()
rinnamedisplay.undraw()
#Me too! I love (userlikes), nya~!
msgret.setText("Me too! I love " + userlikes + ", nya~!\n\n")
rinnamedisplay.setText("Rin")
rinnamedisplay.draw(window)
msgret.draw(window)
nextbutton()
msgret.undraw()
rinnamedisplay.undraw()

#End of Beta 0.1
clicktocontinue.undraw()
speechbox.undraw()
rin1.undraw()
endgame = Rectangle(Point(400,100),Point(1040,720))
endgame.setFill("red")
endgame.draw(window)
endgametitle = Text(Point(720,130), "End of Beta 0.1")
endgametitle.setSize(36)
endgametitle.setTextColor("white")
endgametitle.draw(window)
endmsg = """
Hi, thanks for playing the horrible test for this game. My website 
might be one big meme, and this is for fun of course, but outside of the
memes I really do appreciate the support I get from people on projects
like these. This might be really low quality at the moment, but right now
it's just a tech test, and I hope I can turn it into something more.
Yes it was super short but that's because I don't know what to make
Rin say. Speaking of which:

I'm looking for people to write the dialogue and make art
(so I can not use google images for this and have multiple emotions
for Rin) so if you're interested in helping, join the Discord.
I plan on getting a whole team on this and making it a real game.

I'll be doing my best to make this the best I can!

"凛の全力ステージ、見て欲しいにゃ！" - Rin Hoshizora
TL: "I want everyone to see me perform my best onstage!"

ps you might get an error message when you close the app, ignore that
"""
endgamemsg = Text(Point(720,380), endmsg)
endgamemsg.setSize(20)
endgamemsg.setTextColor("white")
discordbutton = Rectangle(Point(500, 620), Point(940,690))
discordbutton.setFill("blue")
discordbuttontext = Text(Point(720,655),"Click me to join the Rin Sim Discord")
discordbuttontext.setSize(25)
discordbuttontext.setFill("white")
endgamemsg.draw(window)
discordbutton.draw(window)
discordbuttontext.draw(window)
def discordbuttonclick():
    clickpos = window.getMouse()
    clickposx = float(str(clickpos)[6:11])
    clickposy = float(str(clickpos)[13:18])
    if (500 < clickposx < 940) and (620 < clickposy < 690):
        import webbrowser
        webbrowser.open('https://discord.gg/kvtVBnC')
    else:
        discordbuttonclick()
discordbuttonclick()

#Keep this at the end
window.mainloop()
