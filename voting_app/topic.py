class Topic:
    def __init__(self, id, name, options):
        self.id = id
        self.name = name
        self.user = None
        self.options = options
        self.votes = [0] * len(options)
        self.total_votes = 0
        self.percentages = [0] * len(options)
        self.recalculate_percentages_and_total_votes()

    def vote(self, option):
        self.votes[option] += 1
        self.recalculate_percentages_and_total_votes()

    def recalculate_percentages_and_total_votes(self):
        self.total_votes = 0
        for i in range(0, len(self.options)):
            self.total_votes += self.votes[i]
        if self.total_votes > 0:
            for i in range(0, len(self.percentages)):
                self.percentages[i] = (self.votes[i] / self.total_votes) * 100
