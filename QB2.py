'''
Main QB2 build and experimentation file
'''

import VisualDataParser
import InArray
import Image
from numpy import array

def loadimage(imagelocation):
    print 'loading image'
    I = Image.open(imagelocation)
    B = array(VisualDataParser.BmpToHlMatrix(I))
    return B


print "Start"
I = Image.open('QB2Input/0000.bmp')
print "Initialising Array:"
A = InArray.InputArray(I.size, 1)
Imagesize = I.size
print "     Loading Image"
P = VisualDataParser.BmpToHlMatrix(I)
print '     Image loading subprocess completed'
I = array(P)
print "     Pushing image into array"
A.load(I)
print "-----Init cycle complete-----"

for X in range(0,10):#number of images in Input Folder
    A.load(loadimage('QB2Input/000{0}.bmp'.format(X)))
    print "Checking image motion status ({0})".format(X)
    O = A.checkstatus()
    print"Saving images"
    for I in O:
        I.save('QB2Output/{0}output{1}.bmp'.format(X,O.index(I)))
print "Process Complete"
quit()
