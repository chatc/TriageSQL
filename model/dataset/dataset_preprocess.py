import json
import re
from models.input_multi_classification.utils import *
from models.input_multi_classification.config import *

ablation = False

def analyse(data1, data2):
    for i in range(3):
        overlap = set(data1[0]).intersection(set(data2[0]))
        print(overlap.__len__())

def ramdon_select(data, max_size=1e4):
    np.random.seed(42)
    dataset_size = int(min(max_size, len(data)))
    index = np.arange(0, len(data))
    np.random.shuffle(index)
    index = index[: dataset_size]
    data = [data[i] for i in index]
    return data


if __name__ == '__main__':
    cfg = CONFIG()
    # [type,query,db,schema_name,schema]
    data_type = 'testset'
    data = []

    # for i in range(1, 6):
    #     type_data = load_data(os.path.join(data_type, "type{}.json".format(i)))
    #     if i == 5 and ablation: type_data = [x for i, x in enumerate(type_data) if i % 2 == 0]
    #     type_data = ramdon_select(type_data, max_size=1e9)
    #     data += type_data
    #     print("type{}".format(i), len(type_data))

    data = load_data('testset/human_annotated/test.json')

    # hacking dataset contruction
    query = []
    dataset = []
    label = []
    cnt = 0
    delete_table = re.compile("[0-9]+-[0-9]+-[0-9]+")

    for sample in data:
        if len(sample['question']) == 0: continue
        schema_list = []
        for table_name, columns in sample['tables'].items():
            schema_list += [column_name if delete_table.match(table_name)
                            else table_name + '.' + column_name for column_name in columns]
        if not len(schema_list): continue
        # no numbers in schema list
        # all in lower case
        query.append(sample['question'].lower())
        dataset.append(' | '.join(schema_list).lower())
        label.append(cfg.label_dict[sample['type']])

    json.dump([query, dataset, label], open('final_turncated_{}.json'.format(data_type), 'w'))




