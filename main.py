import time
t_start=time.time()
import cell

# --- variables -------------------------------------

dim=(10,10)
time_steps=10

# --- methods ---------------------------------------

def initialize_cells(width,length):
	pass
	# we need to decide whether position will be given to cell or not
	area=[[cell.cell(pos=(x,y)) for x in range(width)] for y in range(length)]
	return area

def initialize_neighbors(area):
	for y in range(len(area)):
		for x in range(len(area[0])):
			for i in range(8):
				coo=[	(x-1,y-1),(x,y-1),(x+1,y-1),	# 012 
						(x-1,y  ),        (x+1,y  ),	# 3 4
						(x-1,y+1),(x,y+1),(x+1,y+1)]	# 567
				pos_x=coo[i][0]%width
				pos_y=coo[i][1]%length
				area[x][y].neighbors[i]=area[pos_x][pos_y]

def update(area):
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].update()

def output():
	for y in range(len(area)):
		out=" "
		for x in range(len(area[0])):
			if area[x][y].get_state():
				out+="X"
			else:
				out+="L"
		print out
# --- main process -----------------------------------

area=initialize_cells(dim[0],dim[1])
initialize_neighbors(area)

for t in range(time_steps):
	update(area)

output()




print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"