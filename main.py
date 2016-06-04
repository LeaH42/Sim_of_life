import time
t_start=time.time()
import cell
import random

# --- variables -------------------------------------

dim=(10,10)
time_steps=10

# --- methods ---------------------------------------

def initialize_cells(width,length):
	# we need to decide whether position will be given to cell or not
	# how do you want to initialize the state of the cell?
	area=[[cell.cell((x,y), random_state()) for x in range(width)] for y in range(length)]
	return area

def initialize_neighbors(area, width, length):
	for y in range(len(area)):
		for x in range(len(area[0])):
			for i in range(8):
				# is there any reason why you cannot move the list outside the last for-loop?
				coo=[	(x-1,y-1),(x,y-1),(x+1,y-1),	# 012 
						(x-1,y  ),        (x+1,y  ),	# 3 4
						(x-1,y+1),(x,y+1),(x+1,y+1)]	# 567
				pos_x=coo[i][0]%width
				pos_y=coo[i][1]%length
				area[x][y].neighbors[i]=area[pos_x][pos_y]

def random_state():
	state=(False, True)
	return state[random.randint(0,1)]
		

def update(area):
	#updating each cell for live or die in the next time step
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].stay_alive()

	#collective update of all pointers
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].update_pointer()
	

def output():
	for y in range(len(area)):
		out=" "
		for x in range(len(area[0])):
			# I changed the letters. "L" for "living" is more intuitive, isnt it?
			if area[x][y].get_state():
				out+="L"
			else:
				out+="X"
		print out
	print('\n')

# --- main process -----------------------------------

area=initialize_cells(dim[0],dim[1])
initialize_neighbors(area, dim[0],dim[1])
output()

for t in range(time_steps):
	update(area)
	output()

print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"
