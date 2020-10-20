import torch.nn as nn
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from config import *
from utils import *
from model import TransformerMultiClassifier
import time

os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
time_stamp = time.strftime("%m%d%H%M", time.localtime())
DEBUG = False

def eval(model, test_loader, cfg):
    # evaluation
    model.eval()
    eval_labels = []
    eval_results = []
    for batch in test_loader:
        # move batch to GPU
        if torch.cuda.is_available() and cfg.use_gpu is True:
            batch = [x.cuda(cfg.device) for x in batch]

        # forward
        classification_logits = model(batch[0], batch[1])[0]
        batch_results = torch.argmax(classification_logits, dim=1).cpu().numpy()

        # add to list
        eval_labels += batch[2].cpu().tolist()
        eval_results += batch_results.tolist()

    print(classification_report(eval_labels, eval_results,
          target_names=[{y: x for x, y in cfg.label_dict.items()}[i] for i in range(len(cfg.label_dict))]))
    print(cfg.label_dict)
    print(confusion_matrix(eval_labels, eval_results))
    model.train()



if __name__ == '__main__':
    # load config
    cfg = CONFIG()

    # load dataset
    print("Loading dataset...")
    # test_data = load_data(cfg.test_path)
    # queries, databases, labels = turn_5type_to_multiclass(get_5type_sequences(test_data), cfg.label_dict)
    queries, databases, labels = load_data(cfg.test_path)
    if DEBUG:
        import random
        index = [i for i in range(len(queries))]
        random.shuffle(index)
        index = index[:500]
        queries = [queries[i] for i in index]
        databases = [databases[i] for i in index]
        labels = [labels[i] for i in index]
    # tokenize
    print("Tokenizing...")
    test_tokens, test_labels = tokenize_sequences(queries, databases, labels, cfg.pretrain_model_name, cfg.max_input_len)

    # load model and the others
    model = TransformerMultiClassifier(cfg.pretrain_model_name, num_labels=len(cfg.label_dict))
    criterion = nn.CrossEntropyLoss(reduction='mean')
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)

    # multi GPU
    if cfg.multi_GPU and torch.cuda.device_count() > 1:
        print(f"Using {torch.cuda.device_count()} GPUs")
        model = nn.DataParallel(model)

    # load model parameters
    if cfg.load_model:
        print("Loading model...")
        params = torch.load(cfg.model_path)
        model.load_state_dict(torch.load(cfg.model_path))

    # move to gpu
    if torch.cuda.is_available() and cfg.use_gpu is True:
        model.cuda(cfg.device)
        criterion.cuda(cfg.device)

    # use data loader (not in GPU)
    test_loader = DataLoader(TensorDataset(*test_tokens.values(), test_labels),
                             batch_size=cfg.batch_size, shuffle=False, num_workers=4)
    # start training
    print("starting evaluation")
    eval(model, test_loader, cfg)


