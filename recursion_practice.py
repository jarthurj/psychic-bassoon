def rsigma(number):#recursively adds all numbers up to and including the number given
	number = int(number)
	if number == 1:
		return 1
	elif number < 1:
		return 0
	else:
		return number + rsigma(number-1)

def rfact(number):
	number = int(number)
	if number <= 1:
		return 1
	else:
		return number * rfact(number-1)

def flood_filler(canvas_2d,start_xy, new_color):
	x = start_xy[0]
	y = start_xy[1]
	current_color = canvas_2d[x][y]
	print("x:",x," y:",y, " cc:", current_color)
	# if canvas_2d
	if x-1 >= 0 and canvas_2d[x - 1][y] == current_color:
		print(1)
		canvas_2d[x][y] = new_color
		return flood_filler(canvas_2d, [x - 1, y], new_color)
	if x+1 < len(canvas_2d) and canvas_2d[x + 1][y] == current_color:
		print(2)
		canvas_2d[x][y] = new_color
		return flood_filler(canvas_2d, [x + 1, y], new_color)
	if y-1 >= 0 and canvas_2d[x][y - 1] == current_color:
		print(3)
		canvas_2d[x][y] = new_color
		return flood_filler(canvas_2d, [x, y - 1], new_color)
	if y+1 < len(canvas_2d[0]) and canvas_2d[x][y + 1] == current_color:
		print(4)
		canvas_2d[x][y] = new_color
		return flood_filler(canvas_2d, [x, y + 1], new_color)
	if x==0:
		return flood_filler(canvas_2d, [x+1, y], new_color)
	if x==len(canvas_2d):
		return flood_filler(canvas_2d, [x-1, y], new_color)
	if y==0:
		return flood_filler(canvas_2d, [x, y+1], new_color)
	if y==len(canvas_2d):
		return flood_filler(canvas_2d, [x, y-1], new_color)
	# if True :
	# 	print(5)
	# 	canvas_2d[x][y] = new_color
	# 	return canvas_2d

canvas = [[3,2,3,4,3],
		 [2,3,3,4,0],
		 [7,3,3,5,3],
		 [6,5,3,4,1],
		 [1,2,3,3,3]]

starter = [2,2]
new = 1
ret = flood_filler(canvas, starter, new)
for x in ret:
	print(x)