# MSPaint Test
myApp = App.open("mspaint")
wait("IIEIEIEIEIII.png", 20)

#locate corners
topLeft = find(Pattern("1315415458910.png").similar(0.00).targetOffset(-6,-3))
topRight = find(Pattern("1315415491403.png").similar(0.00))
bottomLeft = find(Pattern("1315415515736.png").similar(0.00).targetOffset(-1,-1))
bottomRight = find(Pattern("1315415538989.png").similar(0.00).targetOffset(1,-2))
centerX = ((topLeft.getTarget().getX())+(bottomRight.getTarget().getX()))/2


print topLeft.getTarget()
print bottomLeft.getTarget()
print bottomRight.getTarget()
print centerX

click("1315415967452.png")
# Start Drawing
def createBox():
	i = 0
	print bottomLeft.getTarget().offset(i, -i).getY()
	print topLeft.getTarget().offset(i, i).getY()
	print (bottomLeft.getTarget().offset(i, -i).getY())-(topLeft.getTarget().offset(i, i).getY())
	while (bottomLeft.getTarget().offset(i, -i).getY())-(topLeft.getTarget().offset(i, i).getY()) > 50:
		print (bottomLeft.getTarget().offset(i, -i).getY())-(topLeft.getTarget().offset(i, i).getY())
		# Left Line
		hover(bottomLeft.getTarget().offset(i, -i))
		mouseDown(Button.LEFT)
		mouseMove(topLeft.getTarget().offset(i, i))
		mouseUp()

		#Bottom Line
		hover(bottomRight.getTarget().offset(-i, -i))
		mouseDown(Button.LEFT)
		mouseMove(bottomLeft.getTarget().offset(i, -i))
		mouseUp()

		#Right Line
		hover(topRight.getTarget().offset(-i, i))
		mouseDown(Button.LEFT)
		mouseMove(bottomRight.getTarget().offset(-i, -i))
		mouseUp()

		#Top line
		hover(topLeft.getTarget().offset(i, i))
		mouseDown(Button.LEFT)
		mouseMove(topRight.getTarget().offset(-i, i))
		mouseUp()
		i = i+5

createBox()
# Exit when done
#myApp.close()