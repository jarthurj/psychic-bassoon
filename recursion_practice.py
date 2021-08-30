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

def flood_filler(canvas_2d, start_xy, old_color, new_color):
	x = start_xy[0]
	y = start_xy[1]
	if (x < 0 or x == len(canvas_2d) or 
		y < 0 or y == len(canvas_2d[x]) or
		canvas_2d[x][y] != old_color or
		canvas_2d[x][y] == new_color):
		return
	if canvas_2d[x][y] == old_color:
		canvas_2d[x][y] = new_color
	flood_filler(canvas_2d, [x-1, y], old_color, new_color)
	flood_filler(canvas_2d, [x+1, y], old_color, new_color)
	flood_filler(canvas_2d, [x, y-1], old_color, new_color)
	flood_filler(canvas_2d, [x, y+1], old_color, new_color)
	return canvas_2d
canvas = [[3,2,3,4,3],
		  [2,3,3,4,0],
		  [7,3,3,5,3],
		  [6,5,3,4,1],
		  [1,2,3,3,3]]

starter = [2,2]
new = 1
old = 3
ret = flood_filler(canvas, starter,old, new)
for x in ret:
	print(x)