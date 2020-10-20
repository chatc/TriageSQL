## A Multi-class query classification model

This model is designed to classify the queries of the users as described in task 1 of the [document](https://docs.google.com/document/d/10szA5EJz7tYpyUjA3aXaXEFSjOJZ37Ni0ynAS270ksw/edit#). '0' represents answerable, '1'-'4' represent distinct types of unanswerable questions.

### Usage and explaination
- usage: ```python train.py```
- config.py hyper parameters (doesn't support argparse yet, supports GPU)
- train.py training and evaluation of the model
- utils.py loading the dataset and tokenization
- model.py the RoBERTa classification model we used

### TODOs
- Change to a complete dataset
- Modify the model
