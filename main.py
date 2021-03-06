import time
t_start=time.time()
import cell
import random
import matplotlib.animation as animation
import pylab as plt

# --- variables -------------------------------------

dim=(100,100)
time_steps=75
perc=0.5		#percentage of initially living cells

# --- methods ---------------------------------------

def initialize_cells(width,length, perc):
	# how do you want to initialize the state of the cell?
	area=[[cell.cell((x,y), random_state(perc)) for x in range(width)] for y in range(length)]
	return area

def initialize_neighbors(area):
	for y in range(len(area)):
		for x in range(len(area[0])):
			coo=[	(x-1,y-1),(x,y-1),(x+1,y-1),	# 012 
					(x-1,y  ),        (x+1,y  ),	# 3 4
					(x-1,y+1),(x,y+1),(x+1,y+1)]	# 567
			for i in range(8):
				pos_x=coo[i][0]%len(area[0])
				pos_y=coo[i][1]%len(area)
				area[x][y].neighbors[i]=area[pos_x][pos_y]

def random_state(perc):
	return random.randint(0,100)<perc*100
		

def update(area):
	#updating each cell for live or die in the next time step
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].stay_alive()

	#collective update of all pointers
	for y in range(len(area)):
		for x in range(len(area[0])):
			area[x][y].update_pointer()

def plotvecs(areas,dim):    

    # figure initialization
    fig = plt.figure()
    ax = plt.axes(xlim=(0, dim[0]), ylim=(0, dim[1]))
    
    def animate(i): 
        ax.imshow(areas[i], cmap='Greys', interpolation='none')

    anim = animation.FuncAnimation(fig, animate, frames=time_steps+1, interval=10, blit=False,repeat=False)

    plt.xlim(-1, len(area[0])+1)
    plt.ylim(-1, len(area)+1)
    plt.axis("off")
    plt.show()


def convert_area(area):
	states=[[0 for x in range(len(area[0]))] for y in range(len(area))]
	for y in range(len(area)):
		for x in range(len(area[0])):
			if area[x][y].get_state():
				states[x][y]=1
	return states
	

# --- main process -----------------------------------

area=initialize_cells(dim[0],dim[1], perc)
initialize_neighbors(area)
areas=[]
areas.append(convert_area(area))

for t in range(time_steps):
	update(area)
	areas.append(convert_area(area))
	#time.sleep(0.5) #why?

plotvecs(areas, dim)

print "program finished. ("+str(int((time.time()-t_start)*1000))+" ms)"
