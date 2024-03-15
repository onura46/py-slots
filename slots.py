############################
#                          #
# SLOTS by KAELIN BOUGNEIT #
#        "GAMBA Pog"       #
#                          #
############################

from colorama import init,Fore,Back,Style
from time import sleep
import random

MAX_BET = 50000
STARTING_MONEY = 500

TILES = {"$":0.020, "§":0.050, "#":0.070, "Ʊ":0.100, "Ӂ":0.130, "ȸ":0.150, "!":0.18, "&":0.30} # TO-DO: create weighted matrix of win probabilities rather than per-tile probabilities
REWARD_MULTIPLIERS = {"$":100, "§":50, "#":25, "Ʊ":15, "Ӂ":12, "ȸ":8, "!":5, "&":2} # Rewards are created by multiplying bets by this number

NORMAL_STYLE = Fore.GREEN + Back.BLACK + Style.NORMAL
MONEY_STYLE = Fore.BLACK + Back.GREEN + Style.BRIGHT
SLOT_STYLE = Fore.CYAN + Back.BLACK + Style.NORMAL
WIN_STYLE = Fore.BLACK + Back.LIGHTMAGENTA_EX + Style.BRIGHT
LOSS_STYLE = Fore.RED + Back.BLACK + Style.NORMAL
RESET_STYLE = Fore.RESET + Back.RESET + Style.RESET_ALL

class Game:
    def __init__(self) -> None:
        # Colorama Initialize
        init()

    def intro():
        # Flashes the title
        for i in range(1,6):
            print(Fore.GREEN + Back.RED + Style.BRIGHT + "SLOTS SLOTS SLOTS SLOTS SLOTS SLOTS", end="\r")
            sleep(0.25)
            print(Fore.RED + Back.GREEN + Style.BRIGHT + "SLOTS SLOTS SLOTS SLOTS SLOTS SLOTS", end="\r")
            sleep(0.25)
        for i in range (1,2):
            print(RESET_STYLE + "\n")  

    def main():
        player_money = STARTING_MONEY
        while player_money > 0:
            print(MONEY_STYLE + "YOU HAVE " + Fore.RED + str(player_money) + Fore.GREEN + " MONEYS")
            print(NORMAL_STYLE) # This just resets the terminal style

            bet = Slots.bet(player_money)
            print(NORMAL_STYLE + f"YOU BET: {bet}")
            player_money = player_money - bet # Subtract the bet from player money

            reward_multiplier = Slots.spin(bet) # SPIN
            if reward_multiplier != None: # PAYOUT
                player_money = player_money + (bet * reward_multiplier)
        else:
            pass # Moves on to Game Over
    
    def over():
        # Game Over; just flashes up some text to taunt you before quitting
        for i in range(1,20):
            print(Fore.RED + Back.BLACK + Style.BRIGHT + "GAME OVER! YOU LOSE! HUGE L! SO BAD!", end="\r")
            sleep(0.10)
            print(Fore.BLACK + Back.RED + Style.BRIGHT + "GAME OVER! YOU LOSE! HUGE L! SO BAD!", end="\r")
            sleep(0.10)
            print(Fore.RED + Back.WHITE + Style.BRIGHT + "GAME OVER! YOU LOSE! HUGE L! SO BAD!", end="\r")
            sleep(0.10)
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "GAME OVER! YOU LOSE! HUGE L! SO BAD!", end="\r")
            sleep(0.10)
        print(NORMAL_STYLE)
        print(f"\n")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "GOODBYE! :)")
        sleep(4)

class Slots:
    def bet(player_money):
        while True:
            try: # Error handling for bet inputs
                bet = int(input(NORMAL_STYLE + f"INPUT YOUR BET (MAX {MAX_BET}): "))
                if bet > player_money:
                    print(LOSS_STYLE + f"YOU'RE TOO POOR FOR A BET THAT BIG!")
                    continue
                elif 1 <= bet <= MAX_BET:
                    return bet
                else:
                    print(LOSS_STYLE + f"PLEASE BET A NUMBER BETWEEN 1 AND {MAX_BET}")
                    continue
            except ValueError:
                print(LOSS_STYLE + f"THAT'S NOT A NUMBER, DOOFUS. PLEASE CHOOSE A NUMBER BETWEEN 1 AND {MAX_BET}.")

    def spin(bet):
        # Spin animation
        print(SLOT_STYLE)
        for i in range(1,100):
            print(Slots.choose_tile() + Slots.choose_tile() + Slots.choose_tile(),end="\r")
            sleep(0.01)

        # Roll the real slot values, save, and display them
        slot1, slot2, slot3 = Slots.choose_tile(), Slots.choose_tile(), Slots.choose_tile()
        print(slot1 + slot2 + slot3)
        sleep(0.5)
        print(f"\n")

        # Evaluate slots and determine reward
        reward_multiplier = Slots.evaluate(slot1,slot2,slot3)
        if reward_multiplier != None:
            print(WIN_STYLE + f"WINNER!! YOU WON {reward_multiplier} TIMES YOUR BET FOR {reward_multiplier * bet} MONEYS!!")
            return reward_multiplier
        else:
            print(LOSS_STYLE + "NO MATCH ||| PLEASE SPIN AGAIN")

    def evaluate(slot1, slot2, slot3):
        if slot1 == slot2 == slot3:
            reward_multiplier = REWARD_MULTIPLIERS[slot3[0]] # Read any slot value, since you're in the loop where you won...
            return reward_multiplier
        elif [slot1[0],slot2[0],slot3[0]].count(slot1[0]) == 2:
            reward_multiplier = REWARD_MULTIPLIERS[slot1[0]] / 2
            return reward_multiplier
        elif [slot1[0],slot2[0],slot3[0]].count(slot2[0]) == 2:
            reward_multiplier = REWARD_MULTIPLIERS[slot2[0]] / 2
            return reward_multiplier
        elif [slot1[0],slot2[0],slot3[0]].count(slot3[0]) == 2:
            reward_multiplier = REWARD_MULTIPLIERS[slot3[0]] / 2
            return reward_multiplier
        else:
            return None # ...or else there is no win
    
    def choose_tile():
        # Tile choice logic
        slot = random.choices(list(TILES.keys()),weights=TILES.values()) # Choose a random tile by weight
        return slot

Game()
Game.intro()
Game.main()
Game.over()