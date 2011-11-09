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
I = Image.open('3.bmp')
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
A.load(loadimage('4.bmp'))
print "Checking image motion status"
O = A.checkstatus()
print"Saving images"
for I in O:
    I.save('output{0}.bmp'.format(O.index(I)))

print O
quit()
