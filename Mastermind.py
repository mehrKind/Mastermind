""""
    Alireza Mehraban
    https://github.com/mehrKind
    Jahrom University
    2024-08-20
"""

import pygame as pg
from sys import exit
from tkinter import messagebox
from itertools import product
import random
from time import sleep

# start the game
pg.init()
WIDTH = 600
HEIGHT = 730
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Mastermind Game")


# colors
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
dark_blue = (4, 0, 117)
white = (255, 255, 255)
purple = (109, 38, 164)
light_pink = (250, 72, 132)
gray = (66, 61, 67)
Love_pink = (255, 0, 51)
red = (255, 0, 0)
light_gray = (93,93,93)

# fonts
font_q = pg.font.SysFont(None,30)
font_a = pg.font.SysFont(None,25)
undoBtn = font_q.render("Undo", True, white)
submitBtn = font_q.render("Submit", True, white)

# ai board
ai_board = [[0 for _ in range(4)] for _ in range(10)]
hint_board = [[0 for _ in range(4)] for _ in range(10)]

main_nuts = [0, 0, 0, 0]
previous_guesses = {
    "guess": [],
    "feedback": []
}
rand = 1
end_rand = 10
is_start = False

# game logics
# all nuts
nuts = {
    "white": 0,
    "blue": 1,
    "red": 2,
    "yellow": 3,
    "green": 4,
}

hint_nuts = {
    "black": 1,
    "white": 2,
    "dark_blue": 3
}

# nuts


def is_finish(guess: list, rand: int):
    global main_nuts
    if rand>10:    
        if guess == tuple(main_nuts):
            sleep(5)
            print("ai wins")
            exit()
        else:
            print("you wone")
            exit()
    
    else:
        if guess == tuple(main_nuts):
            print("ai wins")
            exit()


#! =========== ai part start ========
def generate_combinations(colors):
    return list(product(colors, repeat=4))

# get possible moves
possible_combinations = generate_combinations([nuts["blue"], nuts["green"], nuts["red"], nuts["yellow"]])
# make a geuss
guess = random.choice(possible_combinations)

def analyze_feedback(guess, feedback, possible_combinations):
    global rand
    
    new_possible_combinations = []

    for combination in possible_combinations:
        # Convert tuple to list for mutability
        temp_comb = list(combination)
        temp_guess = list(guess)

        # Count white (correct color and correct position)
        white = sum([1 for i in range(4) if temp_comb[i] == temp_guess[i]])

        # Count black (correct color but wrong position)
        black = 0

        # Remove white hits from temporary lists to avoid double counting
        for i in range(4):
            if temp_comb[i] == temp_guess[i]:
                temp_comb[i] = temp_guess[i] = None  # Mark as checked

        # Check remaining for black hits
        for i in range(4):
            if temp_guess[i] is not None and temp_guess[i] in temp_comb:
                black += 1
                temp_comb[temp_comb.index(temp_guess[i])] = None  # Mark as checked

        # Convert feedback to the corresponding values: 1 for white, 2 for black, 0 for none
        expected_feedback = [0] * 4
        expected_feedback[:white] = [1] * white  # Fill with whites (correct color & position)
        expected_feedback[white:white + black] = [2] * black  # Fill with blacks (correct color, wrong position)

        # Sort to ignore position; the game logic only cares about counts
        if sorted(expected_feedback) == sorted(feedback):
            new_possible_combinations.append(combination)

    return new_possible_combinations



def ai_guess():
    global rand, guess, previous_guesses, possible_combinations
    if is_start:
        previous_guesses["guess"].append(guess)
        previous_guesses["feedback"].append(hint_board[rand-1])
        

        # Get new possible combinations based on feedback
        possible_combinationss = analyze_feedback(guess, previous_guesses["feedback"][-1], possible_combinations)

        # Choose a new guess from the updated possible combinations
        if possible_combinationss:
            rand += 1
            guess = random.choice(possible_combinationss)
            ai_board[rand-1] = guess
            # if tuple(main_nuts) == ai_board[rand-1]:
            #     pg.time.wait(milliseconds=3000)
            #     print("ai wins")
            #     exit()
            is_finish(guess, rand)
            
        else:
            # possible_combinations.remove()
            for i in previous_guesses["guess"]:
                if isinstance(i, list):
                    possible_combinations.remove(i)
                else:
                    break
            possible_combinationss = possible_combinations
            ai_guess()
            
    else:
        messagebox.showinfo("هشدار", "هنوز بازی شروع نشده")

    

    

#! =========== ai part end ========


def draw_board():
    for row in range(len(ai_board)):
        for col in range(len(ai_board[row])):
            # Calculate the position for each circle
            x = 135+(col*80)  # Adjust for circle center
            y = 20 + row * 50 + 35  # Adjust for circle center
            
            # Get the value from ai_board
            value = ai_board[row][col]
            
            # Determine the color based on the value in ai_board using the nuts dictionary
            if value == nuts["white"]:
                color = (255, 255, 255)  # white
            elif value == nuts["blue"]:
                color = (0, 0, 255)       # blue
            elif value == nuts["red"]:
                color = (255, 0, 0)       # red
            elif value == nuts["yellow"]:
                color = (255, 255, 0)     # yellow
            elif value == nuts["green"]:
                color = (0, 255, 0)       # green
            else:
                color = (0, 0, 0)         # default to black if value is not recognized
            
            # Draw the circle
            pg.draw.circle(screen, color, (x, y), 17)
            pg.draw.circle(screen, black, (x, y), 17, 2)
            
    # pg.display.update()
            
            
def draw_hint_board():
    for row in range(len(hint_board)):
        for col in range(len(hint_board[row])):
            # Calculate the position for each circle
            x = 468+(col*15)  # Adjust for circle center
            y = 20 + row * 50 + 35  # Adjust for circle center
            
            # Get the value from hint_board
            value = hint_board[row][col]
            
            # Determine the color based on the value in ai_board using the nuts dictionary
            if value == hint_nuts["white"]:
                color = white  # white
            elif value == hint_nuts["black"]:
                color = black       # black
            else:
                color = light_gray
                
            # Draw the circle
            pg.draw.circle(screen, color, (x, y), 4)
            # pg.draw.circle(screen, black, (x, y), 17, 2)
    # pg.display.update()


# draw bottom board
def draw_my_color():
    for circle in range(4):
        color = (0, 0, 0)
        if main_nuts[circle] == 0:
            color = (255, 255, 255)
        elif main_nuts[circle] == 1:
            color = (0, 0, 255)
        elif main_nuts[circle] == 2:
            color = (255, 0, 0)
        elif main_nuts[circle] == 3:
            color = (255, 255, 0)
        elif main_nuts[circle] == 4:
            color = (0, 255, 0)
        pg.draw.circle(screen, color, (135+(circle*80), 625), 17)
        pg.draw.circle(screen, black, (135+(circle*80), 625), 17, 2)




# add the color to the main nuts list
def add_my_color(color: str):
    global main_nuts, rand
    if color not in ["black", "white"] and is_start == False:
        if 0 in main_nuts:
            # update the list and put the nuts into it
            main_nuts[main_nuts.index(0)] = nuts[color]
            draw_my_color()
    
    if color in ["black", "white"] and is_start:
        row = rand - 1
        if 0 in hint_board[row]:
            hint_board[row][hint_board[row].index(0)] = hint_nuts[color]
            draw_hint_board()
        

# remove the color to the main nuts list
def remove_my_color():
    global main_nuts
    temp = -1
    for i in range(4):
        if main_nuts[temp] != 0:
            main_nuts[temp] = 0
            break
        else:
            temp -= 1
            

def startGame():
    global is_start
    if all(main_nuts) and is_start == False:
        is_start = True
        ai_board[rand-1] = guess
    else:
        messagebox.showinfo("هشدار", "باید 4 مهره را پر کنید")
        
    
# game keeper
while True:
    screen.fill(white)
    # rect => rect(screen, color, (x,y  , width, height ))
    pg.draw.rect(screen, gray, (80, 20, 350, 550), 0, 5)  # main rect
    pg.draw.rect(screen, gray, (80, 590, 350, 70), 0, 5)  # bottom side rect
    pg.draw.rect(screen, gray, (450, 20, 80, 550), 0, 5)  # right side rect
    # pg.draw.rect(screen, Love_pink, (450,590, 80, 70),0, 5) # stop rect
    pg.draw.rect(screen, green, (450, 590, 80, 70), 0, 5)  # start rect
    pg.draw.rect(screen, Love_pink, (80, 675, 90, 40)) # back button
    pg.draw.rect(screen, dark_blue, (340, 675, 90, 40)) # submit button
    # color choose
    pg.draw.circle(screen, red, (25, 610), 12)  # red circle
    pg.draw.circle(screen, green, (60, 610), 12)  # green circle
    pg.draw.circle(screen, blue, (25, 645), 12)  # blue circle
    pg.draw.circle(screen, yellow, (60, 645), 12)  # yellow circle
    pg.draw.circle(screen, black, (555, 610), 12)  # black circle
    pg.draw.circle(screen, white, (555, 645), 12)  # white circle
    pg.draw.circle(screen, black, (555, 645), 12, 2)  # black circle
    draw_hint_board()
    
    # show boards
    draw_board()
    draw_my_color()
    # display text
    

    
    # settings
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
            

        # add event listener
        mousePos = pg.mouse.get_pos()
        if e.type == pg.MOUSEBUTTONDOWN:
            if 15 <= mousePos[0] <= 37 and 600 <= mousePos[1] <= 622:
                add_my_color("red")
            elif 50 <= mousePos[0] <= 72 and 600 <= mousePos[1] <= 622:
                add_my_color("green")
            elif 15 <= mousePos[0] <= 37 and 635 <= mousePos[1] <= 657:
                add_my_color("blue")
            elif 50 <= mousePos[0] <= 72 and 635 <= mousePos[1] <= 657:
                add_my_color("yellow")
            elif 80 <= mousePos[0] <= 170 and 675 <= mousePos[1] <= 715:
                remove_my_color()
            elif 545 <= mousePos[0] <= 567 and 600 <= mousePos[1] <= 622:
                add_my_color("black")
            elif 545 <= mousePos[0] <= 567 and 635 <= mousePos[1] <= 657:
                add_my_color("white")
            elif 340 <= mousePos[0] <= 430 and 675 <= mousePos[1] <= 715: # todo: submit button
                ai_guess()
            elif 450 <= mousePos[0] <= 530 and 579 <= mousePos[1] <= 660:
                startGame()
                
                
    screen.blit(undoBtn, (100, 686))
    screen.blit(submitBtn, (350, 686))

    pg.display.update()
