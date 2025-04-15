# pycaret_backend.py
from pycaret.classification import (
    setup as pycaret_setup, 
    compare_models, 
    tune_model, 
)
from base_learner import BaseLearnerBackend

class PyCaretBackend(BaseLearnerBackend):
    def __init__(self, data, target, setup_params=None):
        self.data = data
        self.target = target
        self.setup_params = setup_params if setup_params is not None else {}
        self.best_model = None
        self.initialized = False

    def setup(self):
        params = {'data': self.data, 'target': self.target}
        params.update(self.setup_params)
        pycaret_setup(**params)
        self.initialized = True

    def train(self):
        if not self.initialized:
            self.setup()
        self.best_model = compare_models()
        print(self.best_model)
        print("Best model selected.")
        return self.best_model

    def tune(self):
        if self.best_model is None:
            raise Exception("No model trained yet. Run train() before tuning.")
        self.best_model = tune_model(self.best_model)
        return self.best_model

