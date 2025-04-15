# main.py
import pandas as pd
from pycaret_backend import PyCaretBackend
from tabular_learner import TabularLearner

if __name__ == "__main__":
    
    df = pd.read_csv("Chowell_train.csv")

    backend = PyCaretBackend(data=df, target="Response")
    learner = TabularLearner(backend=backend)
    
    learner.setup()
    learner.train()
    learner.tune()

