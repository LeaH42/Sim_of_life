import time
t_start=time.time()
import cell
import random
import pylab as plt

# --- variables -------------------------------------

dim=(10,10)
time_steps=5

# --- methods ---------------------------------------

def initialize_cells(width,length):
	# how do you want to initialize the state of the cell?
	area=[[cell.cell((x,y), random_state()) for x in range(width)] for y in range(length)]
	return area

def initialize_neighbors(area, width, length):
	for y in range(len(area)):
		for x in range(len(area[0])):
			coo=[	(x-1,y-1),(x,y-1),(x+1,y-1),	# 012 
					(x-1,y  ),        (x+1,y  ),	# 3 4
					(x-1,y+1),(x,y+1),(x+1,y+1)]	# 567
			for i in range(8):
				pos_x=coo[i][0]%width
				pos_y=coo[i][1]%length
				area[x][y].neighbors[i]=area[pos_x][pos_y]

def random_state():
	return random.randint(0,1)==0
		

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
			if area[x][y].get_state():
				out+=" "
			else:
				out+="X"
		print out
	print('')

def plot():
	for y in range(len(area)):	
		for x in range(len(area[0])):
			if area[x][y].get_state():
				plt.plot(x,y,'sk')
	plt.xlim(-1, len(area[0])+1)
	plt.ylim(-1, len(area)+1)
	plt.axis("off")
	plt.show()

# --- main process -----------------------------------

area=initialize_cells(dim[0],dim[1])
initialize_neighbors(area, dim[0],dim[1])
#output()
plot()

for t in range(time_steps):
	update(area)
	#output()
	plot()
	time.sleep(0.5) #why?

print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"
