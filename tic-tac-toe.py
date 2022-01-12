# file: tic-tac-toe.py
# author: Nathan Kutomi
# assignment: To build a tic-tac-toe game.

ANSWERS_FOR_X = [
    {
        1: "X",
        2: "X",
        3: "X"
    },
    {
        4: "X",
        5: "X",
        6: "X"
    },
    {
        7: "X",
        8: "X",
        9: "X"
    },
    {
        1: "X",
        4: "X",
        7: "X"
    },
    {
        2: "X",
        5: "X",
        8: "X"
    },
    {
        3: "X",
        6: "X",
        9: "X"
    },
    {
        1: "X",
        5: "X",
        9: "X"
    },
    {
        3: "X",
        5: "X",
        7: "X"
    }
]

ANSWERS_FOR_O = [
    {
        1: "O",
        2: "O",
        3: "O"
    },
    {
        4: "O",
        5: "O",
        6: "O"
    },
    {
        7: "O",
        8: "O",
        9: "O"
    },
    {
        1: "O",
        4: "O",
        7: "O"
    },
    {
        2: "O",
        5: "O",
        8: "O"
    },
    {
        3: "O",
        6: "O",
        9: "O"
    },
    {
        1: "O",
        5: "O",
        9: "O"
    },
    {
        3: "O",
        5: "O",
        7: "O"
    }
]

def main():

    game_table = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: ""
        }
    
    # print("\033[92m" + "Some text"+"\x1b[0m")  
    # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    # for style in range(8):
    #     for fg in range(30,38):
    #         s1 = ''
    #         for bg in range(40,48):
    #             format = ';'.join([str(style), str(fg), str(bg)])
    #             s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
    #         print(s1)
    #     print('\n')

    print("############## Tic-Tac-Toe ###################\n")

    print("Welcome to the game!\n")
    
    game_status = False
    which_player = False
    round = 1
    while (game_status == False and round <= 9):
        print("Round: ", round)
        which_player = not which_player
        player = "X" if (which_player) else "O"

        print_table(game_table)

        get_input(player, game_table)

        print_table(game_table)

        check = check_answer(player, game_table)
        if (check == False):
            round += 1
            if round > 9:
                print("There's no winner. Play again.")
        else:
            print(f"\nThe game is over. And the winner is {player}")
            show_final_result(check, game_table)
            game_status = True
        


def get_input(player, game_table):
    """A function to ask the user for an input for the game, with all the pertaining validations

    Parameters: 
    -----------
    player : str
        Either 'X' or 'O', indicating which player's turn this is.
    game_table: dictionary
        A dictionary containing the current state of the game.

    Returns: 
    -----------
        It doesn't return anything, but it updates the game_table
    """
    choice = 0
    while choice not in range(1,10):
        try:
            user_input = input(f"{player}'s turn to choose a square [1-9]: ")
            choice = int(user_input)
            if choice not in range(1,10):
                print("Pick one number from 1 through 9.\n")
            elif game_table[choice] == "":
                game_table[choice] = player
            else:
                print("Place has alreay been taken. Pick another one")
        except ValueError as e:
            print(f"'{user_input}' is not a digit.")
            print("Make sure to pick a digit from 1 through 9.\n")

def check_answer(player, game_table):
    """It checks the current game state for a correct answer.
    
    Parameters: 
    -----------
    player : str
        Either 'X' or 'O', indicating which player's turn this is.
    game_table: dictionary
        A dictionary containing the current state of the game.

    Returns: 
    -----------
    answer : dictionary
        The correct resolution for this turn, if there is a correct answer.
    False : boolean
        If there isn't a correct answer it returns False.
    """
    ANSWERS = ANSWERS_FOR_X if (player == "X") else ANSWERS_FOR_O
    for answer in ANSWERS:
        # check if one answer dictionary is contained inside our game_table for the player
        if answer.items() <= game_table.items():
            return answer
    return False        

def print_table(game_table):
    """It prints on the console the current table for the game.

    Parameters: 
    -----------
    game_table: dictionary
        A dictionary containing the current state of the game.

    Returns: 
    -----------
        It doesn't return anything.
    """
    vals_list = []
    for key, value in game_table.items():
        val = key if (value == "") else value
        vals_list.append(val)
    table = """
     {} | {} | {}
    ---|---|---
     {} | {} | {}
    ---|---|---
     {} | {} | {}
    ---|---|---
    """
    print(table.format(*vals_list))

def show_final_result(check, game_table):
    """It prints on the console the current game, highlighting the winner!.

    Parameters: 
    -----------
    check: dictionary
        A dictionary containing the correct answer /resolution for the game.

    game_table: dictionary
        A dictionary containing the current state of the game.

    Returns: 
    -----------
        It doesn't return anything.
    """
    for key, value in check.items():
        new_value = f"\033[92m{value}\x1b[0m"
        game_table[key] = new_value
    
    print_table(game_table)
    


if __name__ == "__main__":
    main()


