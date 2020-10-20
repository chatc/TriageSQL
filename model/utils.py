import json
import torch
import numpy as np
from torch.utils.data import Dataset, TensorDataset
from torch.utils.data import DataLoader
from transformers import AutoTokenizer


def load_data(path):
    with open(path, 'r') as file:
        json_str= file.read()
        dataset = json.loads(json_str)
    return dataset


def get_sequences_old(dataset):
    # dataset: {query:{'1':schemas,'0':schemas}}, schemas:{schema_name:{table_name:[column_names]}}
    databases = []
    queries = []
    labels = []
    for query, samples in dataset.items():
        for label, schemas in samples.items():
            schema_list = []
            for schema_name, tables in schemas.items():
                for table_name, column_names in tables.items():
                    schema_list += [table_name+'.'+column_name for column_name in column_names]

            schema_seq = ' | '.join(schema_list)
            databases.append(schema_seq)
            queries.append(query)
            labels.append(label)
    # return : [query(str)], [schema_seq(str)], [label(str)]
    return queries, databases, labels


def get_sequences(dataset):
    # dataset: {'1':[[question,schema]], '0':[{overlap(str):[question,schema]}]},
    # schema:{table_name:[column_names]}
    databases = []
    queries = []
    labels = []
    for label, samples in dataset.items():
        for sample in samples:
            # overlap contains in neg samples
            if label == '0':
                sample = list(sample.items())[-1][1]
            queries.append(sample[0])
            schema_list = []
            for table_name, columns in sample[1].items():
                schema_list += [table_name+'.'+column_name for column_name in columns]
            databases.append(' | '.join(schema_list))
            labels.append(label)

    # return : [query(str)], [schema_seq(str)], [label(str)]
    return queries, databases, labels


def get_5type_sequences(dataset, max_len=1e9):
    # dataset: {'1/0':{type:[[answerable(str), question(str), schema]]}},
    # schema:{table_name:[column_names]}
    # type: small talk, ambiguous, answerable, unanswerable by sql, lack data
    data_dict = {}
    for label, samples in dataset.items():
        for type, questions in samples.items():
            databases = []
            queries = []
            labels = []
            for sample in questions:
                if len(sample[1]) == 0: continue
                schema_list = []
                for table_name, columns in sample[2].items():
                    schema_list += [table_name + '.' + column_name for column_name in columns]
                if not len(schema_list): continue
                queries.append(sample[1])
                databases.append(' | '.join(schema_list))
                labels.append(label)
            #  [query(str)], [schema_seq(str)], [label(str)]
            used_len = min(max_len, len(queries))
            data_dict[type] = (queries[:used_len], databases[:used_len], labels[:used_len])

    # return : {type: dataset}
    return data_dict


def turn_5type_to_multiclass(data_dict, label_dict):
    databases = []
    queries = []
    labels = []
    for type, data in data_dict.items():
        queries += data[0]
        databases += data[1]
        labels += [label_dict[type]]*len(data[2])
    return queries, databases, labels


def tokenize_sequences(queries, databases, labels, model_name="roberta-large", input_max_len=256, label_overwrite=None):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # seq:[label(str), query(str), schema_seq(str)], return: [input(torch.Tensor)], [labels(torch.Tensor)]
    return tokenizer.batch_encode_plus(zip(queries, databases), return_tensors="pt",
                                       pad_to_max_length=input_max_len, max_length=input_max_len, truncation=True), \
           torch.LongTensor([int(label) if label_overwrite is None else label_overwrite for label in labels])


def split_train_test(queries, databases, labels, split_ratio=0.8, max_size=1e9, seed=42):
    np.random.seed(seed)
    dataset_size = int(min(max_size, len(queries)))
    split_point = int(split_ratio * dataset_size)
    index = np.arange(0, len(queries))
    np.random.shuffle(index)
    index = index[: dataset_size]
    trainset = ([queries[i] for i in index[:split_point]],
                [databases[i] for i in index[:split_point]],
                [labels[i] for i in index[:split_point]],)
    testset  = ([queries[i] for i in index[split_point:]],
                [databases[i] for i in index[split_point:]],
                [labels[i] for i in index[split_point:]],)
    return trainset, testset


if __name__ == '__main__':
    # dataset = load_data("./dataset/all_datasets.json")
    # queries, databases, labels = get_sequences(dataset)
    # trainset, testset = split_train_test(queries, databases, labels)
    # train_tokens, train_labels = tokenize_sequences(*trainset, "roberta-large")
    # test_tokens, test_labels = tokenize_sequences(*testset, "roberta-large")
    #
    # data_loader = DataLoader(TensorDataset(*train_tokens.values(), train_labels), batch_size=16, shuffle=True, num_workers=4)
    #
    # for batch in data_loader:
    #     tokens = batch[0]
    #     labels = batch[1]
    #
    # ...
    from config import *
    cfg = CONFIG()
    test_data = load_data(cfg.data_path)

    testset = get_5type_sequences(test_data)
    dataset = turn_5type_to_multiclass(testset, cfg.label_dict)
    ...


