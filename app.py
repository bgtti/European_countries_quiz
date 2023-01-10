import turtle
import pandas

# Setting up turtle:
screen = turtle.Screen()
screen.title("European Countries Quiz")
turtle.setup(720, 585)
the_map = "europe_map.gif"
screen.addshape(the_map)
turtle.shape(the_map)
# comment out screen.exitonclick() when using the code to get the coordinates:
# screen.exitonclick()

# Getting map coordinates for eack country:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Getting CSV info:
countries_list = pandas.read_csv(
    "european_countries_list.csv")

country_names = countries_list["Country"].to_list()
alternative_names = countries_list["Alternative name"].to_list()
all_names = country_names.copy()
all_names.extend(alternative_names)
all_names = list(dict.fromkeys(all_names))


# the popup box:
user_entry = screen.textinput(
    "Guess the country", "Guess another country name")

# get country names to show on map
if user_entry in all_names:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    the_country = None
    if user_entry in country_names:
        print("now here")
        the_country = countries_list[countries_list["Country"] == user_entry]
    else:
        the_country = countries_list[countries_list["Alternative name"] == user_entry]

    t.goto(int(the_country["X"]), int(the_country["Y"]))
    t.write(the_country["Alternative name"])

screen.exitonclick()
