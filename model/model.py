import torch.nn as nn
from transformers import AutoModelForSequenceClassification
from transformers import AutoConfig, RobertaConfig

class TransformerMultiClassifier(nn.Module):
    def __init__(self, pretrain_model_name='roberta-large', num_labels=5):
        super(TransformerMultiClassifier, self).__init__()
        model_config = AutoConfig.from_pretrained(pretrain_model_name, num_labels=num_labels)
        self.model = AutoModelForSequenceClassification.from_config(model_config)

    def forward(self, input_ids, attention_mask):
        return self.model(input_ids, attention_mask)