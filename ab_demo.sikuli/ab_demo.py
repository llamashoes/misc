# Starts Angry Birds
s = find("1315859303639.png")
doubleClick(s)

#Clicks the play button
play = "PTIJW.png"
wait(play, 20)
click(play)

# Selects Game Region
r = selectRegion("Select the app area")
r.highlight(2)
wait(5)
# Starts level 1-5
click(r.find("1320348602390.png"))
wait(5)
click(r.find("1320348830291.png"))

wait("1315865530307.png", FOREVER)

pause = r.find("1315936491114.png")
tries = 1


# Main game loop

for x in range(60, 300):
	print tries
	# Fling the bird
	bird = r.find("1318266373260.png")
	dragDrop(bird, [bird.x - 120, bird.y + x])
	wait(2)
	wait(Pattern("ml.png").similar(0.87), 25)
	wait(5)
#	wait(25)

	if exists("1315939723295.png"):
		click(r.find("1315939750314.png"))
		tries = tries + 1 

	if exists("HJ9EL.png"):
		popup("Winner! - after " + str(tries) + " tries")
		exit()