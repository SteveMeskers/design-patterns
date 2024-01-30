class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.entry = []
        self.combination = combination

    def reset(self):
        self.status = 'LOCKED'
        self.entry = []

    def enter_digit(self, digit):
        self.entry.append(digit)

        if len(self.combination) == len(self.entry):
            if self.combination == self.entry:
                self.status = 'OPEN'
            else:
                self.status = 'ERROR'
        else:
            self.status = "".join([str(entry) for entry in self.entry])

