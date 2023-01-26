import turtle

# Set the turtle's speed to the maximum value
turtle.speed(0)

# Set the turtle's pen color to black
turtle.pencolor('black')

# Set the turtle's pen size to 1 pixel
turtle.pensize(1)

# Set the turtle's pen down
turtle.pendown()

# Set the size of the hexagons in the tessellation
hexagon_size = 50

# Set the angle between sides of the hexagon
hexagon_angle = 60

# Set the distance between adjacent hexagons
hexagon_spacing = hexagon_size * 3**0.5 / 2

# Set the turtle's starting position
turtle.setpos(-hexagon_spacing * 2, 0)

# Set the turtle's heading to the angle between sides of the hexagon
turtle.setheading(hexagon_angle)

# Set the number of rows and columns in the tessellation
rows = 5
columns = 5

# Draw the hexagonal tessellation
for row in range(rows):
    for column in range(columns):
        # Draw a hexagon
        for side in range(6):
            turtle.forward(hexagon_size)
            turtle.left(360 / 6)
        # Move the turtle to the position of the next hexagon
        turtle.forward(hexagon_size / 2)
        turtle.right(60)
        turtle.forward(hexagon_spacing)
        turtle.left(60)
    # Move the turtle to the position of the first hexagon in the next row
    turtle.setheading(60)
    turtle.penup()
    turtle.forward(hexagon_size * 3**0.5)
    turtle.left(60)
    turtle.pendown()

# Keep the window open until it is closed by the user
turtle.exitonclick()
