# from turtle import Turtle, Screen

# jonhny = Turtle()
# print(jonhny)
# jonhny.shape("turtle")
# jonhny.color("red")
# jonhny.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Charmamber"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)