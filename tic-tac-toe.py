# file: tic-tac-toe.py
# author: Nathan Kutomi


def main():

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


    game_status = False
    which_player = False
    while (game_status == False):
        which_player = not which_player
        player = "X" if (which_player) else "O"




        choice = get_input(player)

        # check if place has already been taken
        

            
              

            

        


        
        game_status = isGameOver()
        if game_status == True:
            print(f"\nThe game is over. And the winner is {player}")


def get_input(player):
    choice = 0
    while choice not in range(1,10):
        try:
            user_input = input(f"{player}'s turn to choose a square [1-9]: ")
            choice = int(user_input)
            if choice not in range(1,10):
                print("Pick one number from 1 through 9.\n")
        except ValueError as e:
            print(f"'{user_input}' is not a digit.")
            print("Make sure to pick a digit from 1 through 9.\n")

    return choice


def isGameOver():
    # this will check if game is over
    
    pass


if __name__ == "__main__":
    main()


