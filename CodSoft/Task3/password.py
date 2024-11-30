# Basic Password Generator

import random  
import string  
def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
length_of_string = 10
random_string = generate_random_string(length_of_string)
print("Your password is= ",random_string)