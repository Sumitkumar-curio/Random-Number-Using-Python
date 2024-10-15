import time
import random

seed = int(time.time() * 1000) % 1000  # Milliseconds since epoch
random.seed(seed)
print(random.randint(1, 100))  # Generate a random number between 1 and 100
