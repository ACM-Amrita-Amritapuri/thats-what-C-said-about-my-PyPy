import random
from itertools import permutations
def play_again():
    print("Do you want to play again (Yes or No)")
    response = input(">").upper()
    if response.startswith("Y"):
        return True
    else:
        return False
def start():
    win = False
    player_moves = []
    computer_moves = []
    attempt = []
    turns = 0
    tic_tac_screen = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
    list_1 = [5]
    list_2 = [1, 3]
    list_3 = [5]
    list_4 = [1, 7]
    list_5 = [1, 3, 7, 9]
    list_6 = [3, 9]
    list_7 = [5]
    list_8 = [7, 9]
    list_9 = [5]
    winning_combinations = {(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)}
    def comp():
        computer_check = str(computer_moves[-1])
        if "1" in computer_check:
            tic_tac_screen[0][0] = "o"
        elif "2" in computer_check:
            tic_tac_screen[0][1] = "o"
        elif "3" in computer_check:
            tic_tac_screen[0][2] = "o"
        elif "4" in computer_check:
            tic_tac_screen[1][0] = "o"
        elif "5" in computer_check:
            tic_tac_screen[1][1] = "o"
        elif "6" in computer_check:
            tic_tac_screen[1][2] = "o"
        elif "7" in computer_check:
            tic_tac_screen[2][0] = "o"
        elif "8" in computer_check:
            tic_tac_screen[2][1] = "o"
        elif "9" in computer_check:
            tic_tac_screen[2][2] = "o"
    def turn_1():
        if 1 in player_moves:
            computer_moves.append(random.choice(list_1))
            comp()
        elif 2 in player_moves:
            computer_moves.append(random.choice(list_2))
            comp()
        elif 3 in player_moves:
            computer_moves.append(random.choice(list_3))
            comp()
        elif 4 in player_moves:
            computer_moves.append(random.choice(list_4))
            comp()
        elif 5 in player_moves:
            computer_moves.append(random.choice(list_5))
            comp()
        elif 6 in player_moves:
            computer_moves.append(random.choice(list_6))
            comp()
        elif 7 in player_moves:
            computer_moves.append(random.choice(list_7))
            comp()
        elif 8 in player_moves:
            computer_moves.append(random.choice(list_8))
            comp()
        elif 9 in player_moves:
            computer_moves.append(random.choice(list_9))
            comp()
    def comp_game():
        if (1 in computer_moves) and (2 in computer_moves) and (3 not in player_moves):
            computer_moves.append(3)
            comp()
        elif (1 in computer_moves) and (3 in computer_moves) and (2 not in player_moves):
            computer_moves.append(2)
            comp()
        elif (2 in computer_moves) and (3 in computer_moves) and (1 not in player_moves):
            computer_moves.append(1)
            comp()
        elif (4 in computer_moves) and (5 in computer_moves) and (6 not in player_moves):
            computer_moves.append(6)
            comp()
        elif (4 in computer_moves) and (6 in computer_moves) and (5 not in player_moves):
            computer_moves.append(5)
            comp()
        elif (5 in computer_moves) and (6 in computer_moves) and (4 not in player_moves):
            computer_moves.append(4)
            comp()
        elif (7 in computer_moves) and (8 in computer_moves) and (9 not in player_moves):
            computer_moves.append(9)
            comp()
        elif (7 in computer_moves) and (9 in computer_moves) and (8 not in player_moves):
            computer_moves.append(8)
            comp()
        elif (8 in computer_moves) and (9 in computer_moves) and (7 not in player_moves):
            computer_moves.append(7)
            comp()
        elif (1 in computer_moves) and (4 in computer_moves) and (7 not in player_moves):
            computer_moves.append(7)
            comp()
        elif (1 in computer_moves) and (7 in computer_moves) and (4 not in player_moves):
            computer_moves.append(4)
            comp()
        elif (4 in computer_moves) and (7 in computer_moves) and (1 not in player_moves):
            computer_moves.append(1)
            comp()
        elif (2 in computer_moves) and (5 in computer_moves) and (8 not in player_moves):
            computer_moves.append(8)
            comp()
        elif (2 in computer_moves) and (8 in computer_moves) and (5 not in player_moves):
            computer_moves.append(5)
            comp()
        elif (5 in computer_moves) and (8 in computer_moves) and (2 not in player_moves):
            computer_moves.append(2)
            comp()
        elif (3 in computer_moves) and (6 in computer_moves) and (9 not in player_moves):
            computer_moves.append(9)
            comp()
        elif (3 in computer_moves) and (9 in computer_moves) and (6 not in player_moves):
            computer_moves.append(6)
            comp()
        elif (6 in computer_moves) and (9 in computer_moves) and (3 not in player_moves):
            computer_moves.append(3)
            comp()
        elif (1 in computer_moves) and (5 in computer_moves) and (9 not in player_moves):
            computer_moves.append(9)
            comp()
        elif (1 in computer_moves) and (9 in computer_moves) and (5 not in player_moves):
            computer_moves.append(5)
            comp()
        elif (5 in computer_moves) and (9 in computer_moves) and (1 not in player_moves):
            computer_moves.append(1)
            comp()
        elif (3 in computer_moves) and (5 in computer_moves) and (7 not in player_moves):
            computer_moves.append(7)
            comp()
        elif (3 in computer_moves) and (7 in computer_moves) and (5 not in player_moves):
            computer_moves.append(5)
            comp()
        elif (5 in computer_moves) and (7 in computer_moves) and (3 not in player_moves):
            computer_moves.append(3)
            comp()
        else:
            if (1 in player_moves) and (2 in player_moves) and (3 not in computer_moves):
                computer_moves.append(3)
                comp()
            elif (1 in player_moves) and (3 in player_moves) and (2 not in computer_moves):
                computer_moves.append(2)
                comp()
            elif (2 in player_moves) and (3 in player_moves) and (1 not in computer_moves):
                computer_moves.append(1)
                comp()
            elif (4 in player_moves) and (5 in player_moves) and (6 not in computer_moves):
                computer_moves.append(6)
                comp()
            elif (4 in player_moves) and (6 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (5 in player_moves) and (6 in player_moves) and (4 not in computer_moves):
                computer_moves.append(4)
                comp()
            elif (7 in player_moves) and (8 in player_moves) and (9 not in computer_moves):
                computer_moves.append(9)
                comp()
            elif (7 in player_moves) and (9 in player_moves) and (8 not in computer_moves):
                computer_moves.append(8)
                comp()
            elif (8 in player_moves) and (9 in player_moves) and (7 not in computer_moves):
                computer_moves.append(7)
                comp()
            elif (1 in player_moves) and (4 in player_moves) and (7 not in computer_moves):
                computer_moves.append(7)
                comp()
            elif (1 in player_moves) and (7 in player_moves) and (4 not in computer_moves):
                computer_moves.append(4)
                comp()
            elif (4 in player_moves) and (7 in player_moves) and (1 not in computer_moves):
                computer_moves.append(1)
                comp()
            elif (2 in player_moves) and (5 in player_moves) and (8 not in computer_moves):
                computer_moves.append(8)
                comp()
            elif (2 in player_moves) and (8 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (5 in player_moves) and (8 in player_moves) and (2 not in computer_moves):
                computer_moves.append(2)
                comp()
            elif (3 in player_moves) and (6 in player_moves) and (9 not in computer_moves):
                computer_moves.append(9)
                comp()
            elif (3 in player_moves) and (9 in player_moves) and (6 not in computer_moves):
                computer_moves.append(6)
                comp()
            elif (6 in player_moves) and (9 in player_moves) and (3 not in computer_moves):
                computer_moves.append(3)
                comp()
            elif (1 in player_moves) and (5 in player_moves) and (9 not in computer_moves):
                computer_moves.append(9)
                comp()
            elif (1 in player_moves) and (9 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (5 in player_moves) and (9 in player_moves) and (1 not in computer_moves):
                computer_moves.append(1)
                comp()
            elif (3 in player_moves) and (5 in player_moves) and (7 not in computer_moves):
                computer_moves.append(7)
                comp()
            elif (3 in player_moves) and (7 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (5 in player_moves) and (7 in player_moves) and (3 not in computer_moves):
                computer_moves.append(3)
                comp()
            elif (2 in player_moves) and (6 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (2 in player_moves) and (4 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (4 in player_moves) and (8 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (6 in player_moves) and (8 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (1 in player_moves) and (8 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (3 in player_moves) and (8 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (2 in player_moves) and (7 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (2 in player_moves) and (9 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (3 in player_moves) and (4 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (4 in player_moves) and (9 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (1 in player_moves) and (6 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (6 in player_moves) and (7 in player_moves) and (5 not in computer_moves):
                computer_moves.append(5)
                comp()
            elif (5 in player_moves) and (1 in player_moves) and (9 in computer_moves) and (7 not in computer_moves):
                computer_moves.append(7)
                comp()
            elif (5 in player_moves) and (3 in player_moves) and (7 in computer_moves) and (9 not in computer_moves):
                computer_moves.append(9)
                comp()
            elif (5 in player_moves) and (9 in player_moves) and (1 in computer_moves) and (3 not in computer_moves):
                computer_moves.append(3)
                comp()
            elif (5 in player_moves) and (7 in player_moves) and (3 in computer_moves) and (1 not in computer_moves):
                computer_moves.append(1)
                comp()

            else:
                comp_gen = False
                while not comp_gen:
                    if (2 not in player_moves) and (2 not in computer_moves):
                        computer_moves.append(2)
                        comp()
                        comp_gen = True
                    elif (4 not in player_moves) and (4 not in computer_moves):
                        computer_moves.append(4)
                        comp()
                        comp_gen = True
                    elif (6 not in player_moves) and (6 not in computer_moves):
                        computer_moves.append(6)
                        comp()
                        comp_gen = True
                    elif (8 not in player_moves) and (8 not in computer_moves):
                        computer_moves.append(8)
                        comp()
                        comp_gen = True
                    elif (1 not in player_moves) and (1 not in computer_moves):
                        computer_moves.append(1)
                        comp()
                        comp_gen = True
                    elif (3 not in player_moves) and (3 not in computer_moves):
                        computer_moves.append(3)
                        comp()
                        comp_gen = True
                    elif (5 not in player_moves) and (5 not in computer_moves):
                        computer_moves.append(5)
                        comp()
                        comp_gen = True
                    elif (7 not in player_moves) and (7 not in computer_moves):
                        computer_moves.append(7)
                        comp()
                        comp_gen = True
                    elif (9 not in player_moves) and (9 not in computer_moves):
                        computer_moves.append(9)
                        comp()
                        comp_gen = True
                    else:
                        comp_gen = True
    while not win:
        tic_tac_screen1 = [["1", "2", "3"],
                          ["4", "5", "6"],
                          ["7", "8", "9"]]
        for row in tic_tac_screen1:
            print(row)
        print()
        for row in tic_tac_screen:
            print(row)
        attempt = int(input("Input the number that corresponds to the area: "))
        player_check = str(attempt)
        if attempt in player_moves:
            print("That area is occupied. Try again.")
        elif attempt in computer_moves:
            print("That area is occupied. Try again.")
        elif attempt not in player_moves:
            player_moves.append(attempt)
            turns += 1
            if "1" in player_check:
                tic_tac_screen[0][0] = "x"
            elif "2" in player_check:
                tic_tac_screen[0][1] = "x"
            elif "3" in player_check:
                tic_tac_screen[0][2] = "x"
            elif "4" in player_check:
                tic_tac_screen[1][0] = "x"
            elif "5" in player_check:
                tic_tac_screen[1][1] = "x"
            elif "6" in player_check:
                tic_tac_screen[1][2] = "x"
            elif "7" in player_check:
                tic_tac_screen[2][0] = "x"
            elif "8" in player_check:
                tic_tac_screen[2][1] = "x"
            elif "9" in player_check:
                tic_tac_screen[2][2] = "x"
            for moves in permutations(player_moves, 3):
                if moves in winning_combinations:
                    for row in tic_tac_screen:
                        print(row)
                    print("You win")
                    win = True
                    break
            else:
                if turns == 1:
                    turn_1()
                    for moves in permutations(computer_moves, 3):
                        if moves in winning_combinations:
                            for row in tic_tac_screen:
                                print(row)
                            print("You Lose!")
                            win = True
                            break
                elif turns == 2:
                    comp_game()
                    for moves in permutations(computer_moves, 3):
                        if moves in winning_combinations:
                            for row in tic_tac_screen:
                                print(row)
                            print("You Lose!")
                            win = True
                            break
                elif turns == 3:
                    comp_game()
                    for moves in permutations(computer_moves, 3):
                        if moves in winning_combinations:
                            for row in tic_tac_screen:
                                print(row)
                            print("You Lose!")
                            win = True
                            break
                elif turns == 4:
                    comp_game()
                    for moves in permutations(computer_moves, 3):
                        if moves in winning_combinations:
                            for row in tic_tac_screen:
                                print(row)
                            print("You Lose!")
                            win = True
                            break
                else:
                    for row in tic_tac_screen:
                        print(row)
                    print("Tie Game")
                    win = True

while True:
    start()
    if play_again():
        continue
    else:
        break
