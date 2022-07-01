

import random
from time import sleep




class Human:

    def __init__(self,name):
        super().__init__()
        self.score =0
        self.name = name 

    def user_input(self):
        user_pick=input (f"enter('0 for rock,1 for paper,2 for sissors,3 for lizard,4 for spock')")
        self.user_input=str(user_pick.randint(0,4))
        gesture_list = ["Rock","Paper","Sissors","Lizard","Spock"]
        sleep(1)
        print(f"{self.name} has picked{user_pick[int(self.choose_gesture)]}")