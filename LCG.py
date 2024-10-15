class LCG:
    def __init__(self, seed):
        self.m = 2**31
        self.a = 1103515245
        self.c = 12345
        self.state = seed

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

# Example usage
lcg = LCG(seed=42)
print(lcg.random())  # Generate a random number
