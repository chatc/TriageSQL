# TriageSQL
The dataset and source code for our paper: ["Did You Ask a Good Question? A Cross-Domain Question Intention Classification Benchmark for Text-to-SQL"](https://arxiv.org/abs/2010.12634)

# Dataset Download
Due to the size limitation, please download the dataset from [Google Drive](https://drive.google.com/file/d/1w55CaVEuimUlP-jerOCrVHF1iF0FZYKe/view?usp=sharing).

# Citations 

If you want to use TriageSQL in your work, please cite as follows:
```
@article{zhang2020did,
  title={Did You Ask a Good Question? A Cross-Domain Question Intention Classification Benchmark for Text-to-SQL},
  author={Zhang, Yusen and Dong, Xiangyu and Chang, Shuaichen and Yu, Tao and Shi, Peng and Zhang, Rui},
  journal={arXiv preprint arXiv:2010.12634},
  year={2020}
}
```

# Dataset
In each json file of the dataset, one can find a field called `type`, which includes 5 different values, including `small talk`, `answerable`, `ambiguous`, `lack data`, and `unanswerable by sql`, corresponding to 5 different types described in our paper.  Here is the summary of our dataset and the corresponding experiment results:

| Type | Trainset | Devset | Testset | Type Alias | Reported F1 |
| ---- | -------- | ------ | ------- | ---------- | ----------- |
| small talk | 31160 | 7790 | 500 | Improper | 0.88 |
| ambiguous | 48592 | 9564 | 500 | Ambiguous | 0.43 |
| lack data | 90375 | 19566 | 500 | ExtKnow | 0.56 |
| unanswerable by sql | 124225 | 26330 | 500 | Non-SQL | 0.90 |
| answerable | 139884 | 32892 | 500 | Answerable | 0.53 |
| overall | 434236 | 194037 | 2500 | TriageSQL | 0.66 |

The folder `src` contains all the source files used to construct the proposed TriageSQL. In addition, some part of files contains more details about the dataset, such as `databaseid` which is the id of the schema in the original dataset, e.g. "flight_2" in CoSQL, while `question_datasetid` indicates the original dataset name of the questions, e.g. "quac". Some of the samples do not contain these fields because they are either human-annotated or edited.

# Model
We also include the source code for RoBERTa baseline in our project in `/model`. It is a multi-classifer with 5 classes where '0' represents answerable, '1'-'4' represent distinct types of unanswerable questions. Given the dataset from [Google Drive](https://drive.google.com/file/d/1w55CaVEuimUlP-jerOCrVHF1iF0FZYKe/view?usp=sharing), you may need to conduct some preprocessing to obtain train/dev/test set. You can directly download from [here](https://drive.google.com/file/d/1ol1xFpGuH0BdLw26MvQoeCHLOtTqQ60i/view?usp=sharing) or make your own dataset using the following instructions:

## Constructing input file for the RoBERTa model
The same as `/testset/test.json`, our input file is a json list with shape (num_of_question, 3) containing 3 lists: query, schema, and label.
- query: containing strings of questions
- schema: contianing strings of schema for each question, i.e., "table_name.column_name1 | table_name.column_name2 | ... " for multi-table questions, and column_name1 | column_name2 for single-table questions.
- labels of questions, see config.label_dict for the mapping, leave arbitary value if testing is not needed or true labels are not given.

**when preprocessing, please use lower case for all data, and remove the meaningless table names as well, such as T10023-1242. Also, we sample 10k from each type to form the large input dataset**

## Running
After adjusting the parameters in `config.py`, one can simply run `python train.py` or `python eval.py` to train or evaluate the model.

## Explanation of other files
- config.py: hyper parameters
- train.py: training and evaluation of the model
- utils.py: loading the dataset and tokenization
- model.py: the RoBERTa classification model we used
- test.json: sample of test input


