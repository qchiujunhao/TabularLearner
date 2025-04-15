# tabular_learner.py
class TabularLearner:
    def __init__(self, backend):
        """
        Initialize TabularLearner with a specified backend.
        :param backend: An instance of a class that implements BaseLearnerBackend.
        """
        self.backend = backend

    def setup(self):
        self.backend.setup()

    def train(self):
        return self.backend.train()

    def tune(self):
        return self.backend.tune()

    def predict(self, new_data):
        return self.backend.predict(new_data)

    def save_model(self, file_path):
        self.backend.save(file_path)

    def load_model(self, file_path):
        return self.backend.load(file_path)
