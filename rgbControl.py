from ardupy import *
from webcolors import name_to_rgb as n2rgb

redPin=9
greenPin=11
bluePin=10

def rgb(board, s):
    r,g,b=0,0,0
    reply=""
    if s.lower()=="off":
        reply="Done"
        pass
    elif s[:3].lower()=="rgb":
        try:
            r,g,b=s[4:].split(" ")
            if r.isdigit() and g.isdigit() and b.isdigit():
                reply="Done"
                print "is correct"
            else:
                print "is not correct"
                reply = "Kuch bhi likhoge"
        except:
            reply= "Kuch bhi likhoge"
    else:
        try:
            r,g,b=n2rgb(s)
            reply="Done"
        except:
            reply="Kuch bhi likhoge!"
    if reply=="Done":
        # Next line is for common anode RGB LEDs. Comment/Uncomment
        # it depending upon the type of LED you have.
        #r, g, b = 255-r, 255-g, 2s55-b
        board.analogWrite(redPin, r)
        board.analogWrite(greenPin, g)
        board.analogWrite(bluePin, b)
    return reply
