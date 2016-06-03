import time
t_start=time.time()
import cell

# --- methods ---------------------------------------

def initialize_cells(width,length):
	pass
	# TODO!!!!!!!!
	area=[[cell.cell(pos=(x,y)) for x in range(width)] for y in range(length)]
	return area

def initialize_neighbors(area):
	# TODO!!!!!!!!
	pass

def update(area):
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].update()

def output():
	pass

# --- variables -------------------------------------

width=10
length=10
time_steps=10

# --- main process -----------------------------------

area=initialize_cells(width,length)
initialize_neighbors(area)

for t in range(time_steps):
	update(area)

output()




print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"