"""
racingShapes.py
A game where shapes race froma start line to a finish line.
The movements are randomised, so different shapes can win in different runs.
"""

import turtle, time, random


def drawShape(sides, color):
    """Draws a shape with the specified number of sides and color.
    If sides is None, then a circle is drawn."""
    turtle.pencolor(color)
    turtle.pensize(5)
    turtle.left(90) # Draw the right-hand edge first, vertically
    if sides is None:
        turtle.circle(50)
    else:
        for i in range(sides):
            turtle.forward(50)
            turtle.left(360/sides)
    turtle.right(90)  # Reverses the turn left above (restores original direction)

def drawVerticalLine(x):
    """Draws a vertical line at the specified x coordinate."""
    turtle.pencolor("white")
    turtle.pensize(8)
    moveTo(x,300)
    turtle.goto(x,-300)

def moveTo(x,y):
    """Moves the turtle to a new x and y coordinate without drawing a line."""
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

class Player:
    """Class representing each player (shape)"""
    
    def __init__(self, name, sides, color, x, y):
        """Constructor. Name is a string, sides is the number of sides for the shape
        (or None for a circle), color is the shape's color, x and y are the starting 
        coordinates of the shape."""
        self.name = name
        self.sides = sides
        self.color = color
        # Coordinates for the current position of the shape
        self.x = x
        self.y = y

    def draw(self):
        """Draws the shape at its current x and y coordinates."""
        moveTo(self.x, self.y)
        drawShape(self.sides, self.color)

    def move(self):
        """Moves the shape horizontally by a small, random amount."""
        self.x = self.x + random.randrange(2,8)

class Game:
    """Class representing an instance of a game"""

    # x coordinates for the start and finish lines
    finishLineX = 300
    startLineX = -300
    
    def __init__(self):
        """Constructor - initialses the window and creates 4 players."""
        self.window = turtle.Screen()
        self.window.bgcolor("yellow")
        turtle.pensize(5)
        turtle.tracer(0, 0) # Turns off auto-updating of screen when the turtle is moved.
        self.players = [
            Player("triangle", 3, "blue", self.startLineX, 250),
            Player("sqaure", 4, "green", self.startLineX, 100),
            Player("hexagon", 6, "aqua", self.startLineX, -100),
            Player("circle", None, "purple", self.startLineX, -250)
        ]

    def winner(self):
        """Gets the winning player if there is one, otherwise returns None."""
        # Get the player with the largest x value
        firstPlace = sorted(self.players, key=lambda p:p.x, reverse=True)[0]
        if firstPlace.x > self.finishLineX:
            # Passed the finish line, so is the winner
            return firstPlace
        # Otherwise there isn't a winner yet
        return None

    def playMoves(self):
        """Moves each player by a small rnadom amount."""
        for player in self.players:
            player.move()

    def writeWinner(self):
        """Writes the winner at the bottom of the sreen."""
        moveTo(0, -350)
        turtle.pencolor("black")
        turtle.write("The winner is " + self.winner().name, font=('Arial', 30, 'bold'), align="center")
        moveTo(0, -385)
        turtle.write("Click the screen to play again", font=('Arial', 12, 'bold'), align="center")

    def writeTitle(self):
        """Writes the title at the top of the screen."""
        moveTo(0, 330)
        turtle.pencolor("black")
        turtle.write("Racing shapes!", font=('Courier', 50, 'italic'), align="center")

    def writeCountDown(self, num):
        """Writes a large countdown number in the middle of the screen."""
        moveTo(0, 0)
        turtle.pencolor("red")
        turtle.write(
            str(num)+" ", # extra space to prevent italic number being partially cut off 
            font=('Arial black', 100, 'italic'),
            align="center"
        )
    
    def drawFrame(self):
        """Blanks the window and redraws everything, based on the current state of the game."""
        self.window.reset()
        self.writeTitle()
        drawVerticalLine(self.finishLineX)
        drawVerticalLine(self.startLineX)
        for player in self.players:
            player.draw()
        
        # Hide the small shape indicating the turtle's position
        turtle.hideturtle()
        # Manually update the screen (draw the lines), since tracer(0,0) was used in constructor
        turtle.update()
        
    def play(self):
        """Plays the game."""

        # Refresh rate. 25 to 30 fps is fast enough that the human eye percieves movement
        # rather than still images.
        framesPerSec = 1/30

        # Begin with the countdown
        for i in range(3, 0, -1):
            self.drawFrame()
            self.writeCountDown(i)
            time.sleep(1)

        # Loop through the players making their moves until there is a winner.
        while self.winner() is None:
            self.playMoves()
            self.drawFrame()
            time.sleep(framesPerSec)
        self.writeWinner()
        
        ''' For debugging purposes, write the final x coordinate for each player
        for player in self.players:
            moveTo(player.x, player.y)
            turtle.write(str(player.x))'''
        
        # Restart if/when screen is clicked 
        self.window.onscreenclick(self.restart)

    def restart(self, _1, _2):
        """Resets each player and plays the game again."""
        self.window.onscreenclick(None) # Disable click events
        for player in self.players:
            player.x = self.startLineX
        self.play()

# Create a new game and play it
game = Game()
game.play()
