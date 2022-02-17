import random
import time
from termcolor import colored

def dice():
    print(colored("The dice are rolling...", "green"))
    time.sleep(2)
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    print(f"Die 1: {die_1}")
    print(f"Die 2: {die_2}")
    print(f"Total: {die_1 + die_2}")
dice()
 