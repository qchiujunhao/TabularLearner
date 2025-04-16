classDiagram
    class BaseLearnerBackend {
      <<interface>>
      +setup()
      +train()
      +tune()
    }
    
    class PyCaretBackend {
      +setup()
      +train()
      +tune()
    }
    
    class TabularLearner {
      +setup()
      +train()
      +tune()
    }
    
    PyCaretBackend ..|> BaseLearnerBackend : implements
    TabularLearner --> BaseLearnerBackend : uses
