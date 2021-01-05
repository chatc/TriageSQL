# TriageSQL
The dataset and source code for our paper: "Did You Ask a Good Question? A Cross-Domain Question Intention Classification Benchmark for Text-to-SQL"

# Dataset Download
Due to the size limitation, please download the entire dataset from [Google Drive](https://drive.google.com/file/d/1w55CaVEuimUlP-jerOCrVHF1iF0FZYKe/view?usp=sharing).

# Dataset
In each json file of the root directory, there is a field called `type`, which includes 5 different values, including `small talk`, `answerable`, `ambiguous`, `lack data`, and `unanswerable by sql`, corresponding to 5 different types in our paper.  Here is the summary of our dataset and the corresponding experiment results:

| Type | Trainset | Devset | Testset | Type Alias | Reported F1 |
| ---- | -------- | ------ | ------- | ---------- | ----------- |
| small talk | 31160 | 7790 | 500 | Improper | 0.88 |
| ambiguous | 48592 | 9564 | 500 | Ambiguous | 0.43 |
| lack data | 90375 | 19566 | 500 | ExtKnow | 0.56 |
| unanswerable by sql | 124225 | 26330 | 500 | Non-SQL | 0.90 |
| answerable | 139884 | 32892 | 500 | Answerable | 0.53 |
| overall | 434236 | 194037 | 2500 | TriageSQL | 0.66 |

The folder `src` contains all the source files used to construct the proposed TriageSQL. In addition, some part of files contains more details about the dataset, such as `databaseid` which is the id of the schema in the original dataset, e.g. "flight_2" in CoSQL, while `question_datasetid` indicates the original dataset name of the questions, e.g. "quac". Some of the samples do not contain these fields because they are either human-annotated or edited.

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
