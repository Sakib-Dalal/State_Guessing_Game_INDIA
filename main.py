import turtle
import pandas

image = "india.gif"

screen = turtle.Screen()
screen.title("Guess States of INDIA")
screen.setup(width=800, height=900)
screen.addshape(image)
turtle.Turtle(image)

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv('state_data.csv')
all_states = data['states'].to_list()

guess_states = []
missed_states = []

while len(guess_states) < 33:
    user_input = turtle.textinput(f"Guess States {len(guess_states)}/33", "Enter State: ").title()

    if user_input == "Exit":
        for state in all_states:
            if state not in guess_states:
                missed_states.append(state)
        print(missed_states)
        break

    if user_input in all_states:
        guess_states.append(user_input)
        my_pen = turtle.Turtle()
        my_pen.color("blue")
        my_pen.hideturtle()
        my_pen.penup()
        state_data = data[data['states'] == user_input]
        my_pen.goto(int(state_data.X), int(state_data.Y))
        my_pen.pendown()
        my_pen.write(user_input, align='left', font=('Arial', 12, 'normal'))
