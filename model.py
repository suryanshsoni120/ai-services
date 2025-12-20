from transformers import AutoTokenizer, AutoModel
import torch
from categories import CATEGORY_DESCRIPTIONS

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

category_embeddings = {}

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def embed(text):
    encoded = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded)
    return mean_pooling(model_output, encoded["attention_mask"]).numpy()[0]

# Embed category DESCRIPTIONS instead of labels
for cat, desc in CATEGORY_DESCRIPTIONS.items():
    category_embeddings[cat] = embed(desc)