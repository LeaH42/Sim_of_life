
class cell:

	def __init__(self, pos, state):
		self.pos=pos
		self.state=[state, 0]
		self.neighbors=[]
		
		for n in range(8):
			self.neighbors.append(None)
		
		self.pointer=0

	def update_pointer(self):
		if self.pointer==0:
			self.pointer=1
		else:
			self.pointer=0

	def get_state(self):
		return self.state[self.pointer]


	def stay_alive(self):
		'''check the rules: will the cell survive?'''

		self.state[self.pointer-1]=self.state[self.pointer]

		living_neighbors=0
		for n in self.neighbors:
			if n.state[n.pointer]==True:
				living_neighbors+=1

		##### Rules of the game of life ####

		if self.state[self.pointer]==True:
			if living_neighbors<2 or living_neighbors>3:
				self.state[self.pointer-1]=False
		else:
			if living_neighbors==3:
				self.state[self.pointer-1]=True

		#####################################



			
		
