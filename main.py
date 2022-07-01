from ast import Break
from game import Game

if __name__ == "___main___":
    game= Game()
    game.run_game()



    play_again = input('Do you want to play again? (y/n): ')

   # if user enter any other character other than y, the game ends
    if play_again != 'y':
     print('Thank You ! See you again')
    Break