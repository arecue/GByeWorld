# G'Bye World
import random
import string
 
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
 
chars = string.ascii_letters
size = 3
 
print("Goodbye World" + " " + random_string_generator(size, chars))