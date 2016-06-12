import time
t_start=time.time()
import cell
import random
import matplotlib.animation as animation
import pylab as plt
import copy

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

def plotvecs(areas,dim):    

    # figure initialization
    fig = plt.figure()
    ax = plt.axes(xlim=(0, dim[0]), ylim=(0, dim[1]))

    lines = [ plt.plot([], [], 'sk', ms=10)[0]]

    # empty lines
    def init():    
        for line in lines:
            line.set_data([], [])
        return lines
    
    #lines[] gets x and y list
    def animate(i): 
	xdata=[]
	ydata=[]
	for y in range(len(areas[i])):
		for x in range(len(areas[i][0])):
			if areas[i][x][y]:
				xdata.append(x)
				ydata.append(y)
        lines[0].set_data( xdata, ydata )
        return lines

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=6, interval=500, blit=False,repeat=False)

    plt.xlim(-1, len(area[0])+1)
    plt.ylim(-1, len(area)+1)
    plt.axis("off")
    plt.show()


def convert_area(area):
	states=[[False for x in range(len(area[0]))] for y in range(len(area))]
	for y in range(len(area)):
		for x in range(len(area[0])):
			if area[x][y].get_state():
				states[x][y]=True
	return states
	

# --- main process -----------------------------------

area=initialize_cells(dim[0],dim[1])
initialize_neighbors(area, dim[0],dim[1])
areas=[]
areas.append(convert_area(area))

for t in range(time_steps):
	update(area)
	areas.append(convert_area(area))
	time.sleep(0.5) #why?

plotvecs(areas, dim)

print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"
