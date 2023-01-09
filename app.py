import turtle

# Setting up turtle:
screen = turtle.Screen()
screen.title("European Countries Quiz")
turtle.setup(720, 585)
the_map = "European_countries_quiz\europe_map.gif"
screen.addshape(the_map)
turtle.shape(the_map)
# comment out screen.exitonclick() when using the code to get the coordinates:
# screen.exitonclick()

# Getting map coordinates for eack country:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# the popup box:
answer_country = screen.textinput(
    "Guess the country", "Guess another country name")


print(answer_country)
