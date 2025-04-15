# base_learner.py
from abc import ABC, abstractmethod

class BaseLearnerBackend(ABC):
    @abstractmethod
    def setup(self):
        """Initialize and configure the model environment."""
        pass

    @abstractmethod
    def train(self):
        """Train the model and store the result."""
        pass

    @abstractmethod
    def tune(self):
        """Fine-tune the model parameters."""
        pass

