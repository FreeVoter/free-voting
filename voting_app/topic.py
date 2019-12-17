from voting_app import models


class Topic:
    def __init__(self):
        self.id = 0
        self.question = ""
        #self.author = None
        self.options = []
        self.votes = []
        self.total_votes = 0
        self.percentages = []
        self.model = None

    def load_from_model(self, topic_model):
        if topic_model != self.model:
            self.model = topic_model
        self.id = topic_model.id
        self.question = self.model.question
        #self.author = topic_model.author
        option_models = self.model.get_options()
        self.options = []
        self.votes = []
        for option in option_models:
            self.options.append(option.option_name)
            self.votes.append(option.votes)
        self.total_votes = 0
        self.percentages = [0] * len(self.options)
        self.recalculate_percentages_and_total_votes()

    def vote(self, option):
        option_model = self.model.get_option(option)
        option_model.votes += 1
        option_model.save()
        self.load_from_model(self.model)

    def recalculate_percentages_and_total_votes(self):
        self.total_votes = 0
        for i in range(0, len(self.options)):
            self.total_votes += self.votes[i]
        if self.total_votes > 0:
            for i in range(0, len(self.percentages)):
                self.percentages[i] = (self.votes[i] / self.total_votes) * 100