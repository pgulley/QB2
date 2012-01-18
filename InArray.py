''' 
Another experiment for the QAI idea- this will function as a better
input method for a few reasons. built in pixel-memory means we have a 
'hardware' method for finding motion that is in line with neurology
will be more easily indexible when done, too. just need to do some 
research into how best to impliment it
'''
from numpy import empty, dtype
import Image

class InputArray:
	def __init__(self, size, memdepth):
		self.matrix = empty(size, dtype=dtype(object))
                self.coords = coords2(size)
                self.size = size
		for coord in self.coords:
			self.matrix[coord] = ArrayNode(array=self, memdepth=memdepth, position=coord)
	def __repr__(self):
		return self.matrix.__repr__().replace(' ','')[7:][:-15]
		
	def __getitem__(self,i):
                try:
                        return self.matrix[i]
                except IndexError:
                        return False
	def load(self,data):
                for coord in self.coords:
                        self.matrix[coord].updatevalue(data[coord])
                        
        def checkstatus(self):
                shapes = []
                for coord in self.coords:
                        if not self[coord].checked:
                                if self[coord[0],coord[1]+1]:
                                        if self[coord[0],coord[1]+1].currentval == self.matrix[coord].pastvals[0]:
                                                if self[coord[0],coord[1]+1].checked:
                                                     self[coord[0],coord[1]+1].checked.points.append(coord)
                                                     self[coord[0],coord[1]+1].checked.direction['N'] += 1
                                                     self[coord].checked = self[coord[0],coord[1]+1].checked
                                if self[coord[0]+1,coord[1]]:
                                        if self[coord[0]+1,coord[1]].currentval == self.matrix[coord].pastvals[0]:
                                                if self[coord[0]+1,coord[1]].checked:
                                                     self[coord[0]+1,coord[1]].checked.points.append(coord)
                                                     self[coord[0]+1,coord[1]].checked.direction['E'] += 1
                                                     self[coord].checked = self[coord[0]+1,coord[1]].checked
                                if self[coord[0],coord[1]-1]:
                                        if self[coord[0],coord[1]-1].currentval == self.matrix[coord].pastvals[0]: 
                                                if self[coord[0],coord[1]-1].checked:
                                                     self[coord[0],coord[1]-1].checked.points.append(coord)
                                                     self[coord[0],coord[1]-1].checked.direction['S'] += 1
                                                     self[coord].checked = self[coord[0],coord[1]-1].checked
                                if self[coord[0]-1,coord[1]]:
                                        if self[coord[0]-1,coord[1]].currentval == self.matrix[coord].pastvals[0]:
                                                if self[coord[0]-1,coord[1]].checked:
                                                     self[coord[0]-1,coord[1]].checked.points.append(coord)
                                                     self[coord[0]-1,coord[1]].checked.direction['W'] += 1
                                                     self[coord].checked = self[coord[0]-1,coord[1]].checked

				if not self[coord].checked:
					self[coord].checked = Shape()
					shapes.append(self[coord].checked)
                return (shapes)
                


	
class ArrayNode:
	def __init__(self, array, memdepth=5, position=[0]): 
		self.currentval = 0
		self.pastvals = []
		for a in range(0,memdepth):
                        self.pastvals.append(0)
		self.valdepth = memdepth
		self.position = position
		self.parent = array
		self.status = [0,0,0,0,0] #N,E,S,W,Self
                self.checked = 0

	def __repr__(self):
		return '<{0}>'.format(self.currentval)
		
	def __getitem__(self,i):
		if i == 0:
			return self.currentval
		else:
			return self.pastvals[i-1]	
				
	def updatevalue(self, newval): 
		#update currenval to newval, slide history up a bit
		self.pastvals.reverse() 
		self.pastvals.append(self.currentval)
		self.currentval = newval
                self.checked = 0
		if len(self.pastvals) >= self.valdepth:
			self.pastvals = self.pastvals[1:]
		self.pastvals.reverse()

class Shape:
	def __init__(self):
		self.points = []
                self.direction = {"N":0,"E":0,"S":0,"W":0}



def coords2(size):
        coordinates = []
        for x in range(0,size[0]):
                for y in range(0,size[1]):
                        coordinates.append((x,y))
        return coordinates

