import torch.nn as nn
from torch.utils.data  import Dataset
from torch.utils.data  import DataLoader
from sklearn import metrics
from config import *
from utils import *
from model import TransformerMultiClassifier
import time

os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
time_stamp = time.strftime("%m%d%H%M", time.localtime())


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

    f1_micro = metrics.f1_score(eval_labels, eval_results, average='micro')
    f1_macro = metrics.f1_score(eval_labels, eval_results, average='macro')
    f1_weighted = metrics.f1_score(eval_labels, eval_results, average='weighted')
    model.train()

    print(f"\n[test] loss:{loss}, f1: micro:{f1_micro}, macro:{f1_macro}, weighted:{f1_weighted}")


if __name__ == '__main__':
    # load config
    cfg = CONFIG()
    # load dataset
    print("Loading dataset...")
    # dataset = load_data(cfg.data_path)
    # queries, databases, labels = turn_5type_to_multiclass(get_5type_sequences(dataset), cfg.label_dict)
    # trainset, testset = split_train_test(queries, databases, labels, max_size=cfg.data_max_size)
    trainset = load_data(cfg.train_path)
    testset = load_data(cfg.dev_path)
    # # turncate
    # trainset, _ = split_train_test(*trainset, max_size=cfg.data_max_size)
    # testset, _ = split_train_test(*testset, max_size=cfg.data_max_size//2)

    print(f"train size:{len(trainset[0])}, test size: {len(testset[0])}.")

    # tokenize
    print("Tokenizing...")
    train_tokens, train_labels = tokenize_sequences(*trainset, cfg.pretrain_model_name, cfg.max_input_len)
    test_tokens, test_labels = tokenize_sequences(*testset, cfg.pretrain_model_name, cfg.max_input_len)

    # load model and the others
    model = TransformerMultiClassifier(cfg.pretrain_model_name, num_labels=len(cfg.label_dict))
    criterion = nn.CrossEntropyLoss(reduction='mean')
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)

    # load model parameters
    if cfg.load_model:
        print("Loading model...")
        model.load_state_dict(torch.load(cfg.model_path))

    # move to gpu
    if torch.cuda.is_available() and cfg.use_gpu is True:
        model.cuda(cfg.device)
        criterion.cuda(cfg.device)
    if cfg.multi_GPU and torch.cuda.device_count() > 1:
        print(f"Using {torch.cuda.device_count()} GPUs")
        model = nn.DataParallel(model)

    # use data loader (not in GPU)
    data_loader = DataLoader(TensorDataset(*train_tokens.values(), train_labels),
                             batch_size=cfg.batch_size, shuffle=True, num_workers=4)
    test_loader = DataLoader(TensorDataset(*test_tokens.values(), test_labels),
                             batch_size=cfg.batch_size, shuffle=False, num_workers=4)

    # start training
    print("Start training...")
    for i in range(cfg.epoch):
        for j, batch in enumerate(data_loader):
            # move batch to GPU
            if torch.cuda.is_available() and cfg.use_gpu is True:
                batch = [x.cuda(cfg.device) for x in batch]

            batch_labels = batch[2]
            classification_logits = model(batch[0], batch[1])[0]
            results = torch.softmax(classification_logits, dim=1).cpu().tolist()
            loss = criterion(classification_logits, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print(f'\r[epoch {i}] [batch {j}/{len(train_labels)//cfg.batch_size}] : loss: {loss}', end='   ')

        if cfg.save is True:
            torch.save(model.state_dict(), f'./checkpoints/{time_stamp}_params{i}.pkl')

        eval(model, test_loader, cfg)



