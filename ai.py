

import random
from time import sleep
class AI:

    def ai():
            choice = random.randint(1,5)
            if choice == 1:
                print("CPU picked Rock")
            elif choice == 2:
                 print("CPU picked Paper")
            elif choice == 3:
                 print("CPU picked Scissors")
            elif choice == 4:
                 print("CPU picked Lizard")
            elif choice == 5:
                print("CPU picked Spock")
            return choice