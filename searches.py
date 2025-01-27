
import random

class searchAlgorithm():
    def __init__(self, seed):
        self.index= 0
        self.array = list(range(1, 51))
        self.complete = False
        random.seed(seed)
        random.shuffle(self.array)
        self.search_val = random.choice(self.array)
class linear_search(searchAlgorithm):
    def __init__(self, seed):
        super().__init__(seed)
    
    def step(self):
        if self.array[self.index] == self.search_val:
            self.complete = True
            return True
        else:
            self.index += 1
            self.complete = False
            return False