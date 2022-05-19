import turtle
import pandas as pd
import guessthestate

screen = turtle.Screen()
screen.title("IS YOU DUMB?")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer = guessthestate.GuessTheState()


all_states = pd.read_csv("50_states.csv")
# states = all_states.state.str.lower()
# x_cords = all_states.x
# y_cords = all_states.y


states_dict = {}
for i in range(len(all_states)):
   usa_state = all_states.state[i].lower()
   x_coords = all_states.x[i]
   y_coords = all_states.y[i]
   states_dict[usa_state] = {"x": x_coords, "y": y_coords}


# print(states_dict["alabama"]["x"])
# print(states_dict.keys())
game_on = True
score_count = []
while len(score_count) < 50:
    guess = screen.textinput(title=f"{len(score_count)}/50 States Correct", prompt="Name a State: ")
    if guess == "exit":
        states_left = [key for key in states_dict.keys() if key not in score_count]
        new_data = pd.DataFrame(states_left)
        new_data.to_csv("missing_states.csv")       
        break
    if guess in states_dict.keys():
        x = states_dict[guess]["x"]
        y = states_dict[guess]["y"]
        answer.right_answer(guess, x, y)
        if guess not in score_count:
            score_count.append(guess)
    if len(score_count) == 50:
        turtle.write("GOOD JOB! YOU GOT IT ALL", move=False, align="center", font= ("Courier", 50, "normal"))







