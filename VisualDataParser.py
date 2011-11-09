"""
This Module is for pre-AI parsing of image data.
It does a few things:
Takes image, turns it into a matrix of RGB values
Turns each pixel in there from RGB to HL
Finds contiguous shapes of Hue in the image
"""


import Image
import binascii


def group(s, n):
    return [s[i:i+n] for i in xrange(0, len(s), n)]

def BmpToMatrix(image):
    #Returns a list of lists- each sub-list is a horozontal strip of the image
    Height = image.size[0]
    Width = image.size[1]
    Matrix = []
    for Linenum in range(0, Height):
        Line = []
        for Pixel in range(0, Width):
            loc = (Linenum,Pixel)
            Line.append(image.getpixel(loc))
        Matrix.append(Line)
    return Matrix

def RBGtoHL(pixel):
    #Takes in pixel as an RBG 3-tuple, returns Hue.
    R = pixel[0]
    B = pixel[1]
    G = pixel[2]
    if R>=G>=B:
        try:
            Hue = 60*((B-G)/(R-G))
        except ZeroDivisionError:
            Hue = 0
    elif G>R>=B:
        Hue = 60*(2-((R-B)/(G-B)))
    elif G>=B>R:
        Hue = 60*(2+((B-R)/(G-R)))
    elif B>G>R:
        Hue = 60*(4-((G-R)/(B-R)))
    elif B>R>=G:
        Hue = 60*(4+((R-B)/(G-B)))
    elif R>=B>G:
        Hue = 60*(6-((B-G)/(R-G)))
    Lightness = ((R+B+G)/3)
    return (Lightness) #Remember to put hue back in there eventually

    
def ConvertRBGtoHL(Matrix):
    #Does GRBtoHL on the entire bmp matrix
    NewMatrix = []
    for Line in Matrix:
        NewLine = []
        for Pixel in Line:
            OutputPixel = RBGtoHL(Pixel)
            NewLine.append(OutputPixel)
        NewMatrix.append(NewLine)
    return NewMatrix

def BmpToHlMatrix(Image):
    return ConvertRBGtoHL(BmpToMatrix(Image))

def MatrixToXY(Matrix):
    CoordList = []
    x = -1
    y = -1
    for Line in Matrix:
        x = x+1
        for Pixel in Line:
            y = y+1
            Position = (x,y)
            PointCoord = [Pixel,Position,0]
            CoordList.append(PointCoord)
        y = -1
    return CoordList

def FetchPixel(CoordList, Coord):
    for Pixel in CoordList:
        if Pixel[1] == Coord:
            return Pixel
    return False
 
    
def RunAll(Image):
    return MatrixToXY(ConvertRBGtoHL(BmpToMatrix(Image)))

