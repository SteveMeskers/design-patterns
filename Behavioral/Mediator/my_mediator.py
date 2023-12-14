class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)

class Mediator:
    def __init__(self):
        self.participants = []

    def broadcast(self, participant, value):
        for p in self.participants:
            if p != participant:
                p.value += value
